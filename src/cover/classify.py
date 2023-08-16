from io import StringIO
import pandas
import requests
import xml.etree.ElementTree as ET
from cover.LatLonConv import add_albers_bounding_boxes

LAND_USE_URL="https://nassgeodata.gmu.edu/axis2/services/CDLService/GetCDLStat"
SUB_CATEGORIES_CSV_URL="https://raw.githubusercontent.com/Imageomics/LatLonCover/main/cropScapeDocumentation/CDL_subcategories.csv"
CLASSIFICATION_TYPES = ["A", "B", "D", "F", "G", "N", "W", "WL"]


def fetch_land_cover_csv_str(year, bbox):
    xml_resp = requests.post(LAND_USE_URL, data={
        "year":year,
        "bbox": bbox,
        "format": "CSV"
    })
    xml_resp.raise_for_status()
    root = ET.fromstring(xml_resp.text)
    return_url = root.find('returnURL')
    csv_resp = requests.get(return_url.text)
    csv_resp.raise_for_status()
    return csv_resp.text


def lookup_classification(name_lookup, crop_scape_value):
    name = name_lookup.get(crop_scape_value)
    if not name:
        raise ValueError("Unknown CropScape id " + crop_scape_value)
    return name


def read_crop_scape_csv(path):
    df = pandas.read_csv(path, engine='python', sep=", ")
    # Remove spaces from column headers
    df = df.rename(columns=lambda x: x.strip())
    return df


def create_name_lookup(path=SUB_CATEGORIES_CSV_URL):
    crosswalk_df = pandas.read_csv(path, index_col="Codes")
    return crosswalk_df["courseClass"]


def _add_classification_column(df):
    name_lookup = create_name_lookup()
    df["Classification"] = [lookup_classification(name_lookup, x) for x in df["Value"]]


def get_classification_fraction(df):
    total_acreage = df["Acreage"].sum()
    fractions = df.groupby("Classification")["Acreage"].sum()
    return fractions / total_acreage


def get_land_classifications(albers_bounding_box, year):
    land_cover_csv_str = fetch_land_cover_csv_str(year=year, bbox = albers_bounding_box)
    df = read_crop_scape_csv(StringIO(land_cover_csv_str))
    _add_classification_column(df)
    return get_classification_fraction(df).round(decimals=3).to_dict()


def classify_row(row, column_name):
    return get_land_classifications(row[column_name], year="2022")


def add_classifications(df, lat_col, lon_col):
    add_albers_bounding_boxes(df, lat_column=lat_col, lon_column=lon_col)

    classification_ary = df.apply(classify_row, axis=1, column_name='bb_small')
    for classificationType in CLASSIFICATION_TYPES:
        df[classificationType + "_small"] = [x.get(classificationType, 0.0) for x in classification_ary]

    classification_ary = df.apply(classify_row, axis=1, column_name='bb_big')
    for classificationType in CLASSIFICATION_TYPES:
        df[classificationType + "_big"] = [x.get(classificationType, 0.0) for x in classification_ary]
