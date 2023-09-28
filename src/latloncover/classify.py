from io import StringIO
import importlib.resources
from functools import cache
import pandas as pd
import requests
import xml.etree.ElementTree as ET
from latloncover.LatLonConv import add_albers_bounding_boxes

LAND_USE_URL="https://nassgeodata.gmu.edu/axis2/services/CDLService/GetCDLStat"
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
    df = pd.read_csv(path, engine='python', sep=", ")
    # Remove spaces from column headers
    df = df.rename(columns=lambda x: x.strip())
    return df


@cache
def create_name_lookup():
    path = importlib.resources.files('latloncover').joinpath('CDL_subcategories.csv')
    crosswalk_df = pd.read_csv(path, index_col="Codes")
    return crosswalk_df["courseClass"]


def _add_classification_column(df):
    name_lookup = create_name_lookup()
    df["Classification"] = [lookup_classification(name_lookup, x) for x in df["Value"]]


def get_classification_fraction(df):
    total_acreage = df["Acreage"].sum()
    fractions = df.groupby("Classification")["Acreage"].sum()
    return fractions / total_acreage


def get_land_classifications(albers_bounding_box, year):
    if albers_bounding_box:
        land_cover_csv_str = fetch_land_cover_csv_str(year=year, bbox = albers_bounding_box)
        df = read_crop_scape_csv(StringIO(land_cover_csv_str))
        _add_classification_column(df)
        result = get_classification_fraction(df).round(decimals=3).to_dict()
        return result
    else:
        return {}


def classify_row(row, column_name):
    return get_land_classifications(row[column_name], year="2022")


def add_classifications(df:pd.DataFrame, lat_col: str, lon_col: str) -> pd.DataFrame:
    """
    Returns a new dataframe with *_big and *_small land coverage columns added to df.
    Empty lat/lon columns will result in all zeros for the categories.

    :param df: dataframe with latitude and longitude columns
    :param lat_col: name of the latitude column in df
    :param lon_col: name of the longitude column in df
    """
    df_enh = df.copy(deep=True)

    add_albers_bounding_boxes(df_enh, lat_column=lat_col, lon_column=lon_col)

    classification_ary = df_enh.apply(classify_row, axis=1, column_name='bb_small')
    for classificationType in CLASSIFICATION_TYPES:
        df_enh[classificationType + "_small"] = [x.get(classificationType, 0.0) for x in classification_ary]

    classification_ary = df_enh.apply(classify_row, axis=1, column_name='bb_big')
    for classificationType in CLASSIFICATION_TYPES:
        df_enh[classificationType + "_big"] = [x.get(classificationType, 0.0) for x in classification_ary]

    return df_enh


def get_classification(lat, lon):
    """
    Returns a dictionary with *_big and *_small land coverage details for input lat and lon.
    :param lat: name of the latitude value
    :param lon: name of the longitude value
    """
    df = pd.DataFrame.from_records([{
        "lat": lat,
        "lon": lon
    }])
    df = add_classifications(df, lat_col="lat", lon_col="lon")
    df.drop(columns=["lat", "lon"], inplace=True)
    return df.iloc[0].to_dict()
