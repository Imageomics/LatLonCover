# import libraries

import geopandas as gpd
import pandas as pd


def format_bounds_str(polygon):
    if polygon.is_empty:
        return ''
    x1,y1,x2,y2 = polygon.bounds
    return f"{x1},{y1},{x2},{y2}"


def add_albers_bounding_boxes(df, lat_column, lon_column):
    # Convert lat and long to point geometry
    gdf = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(df[lon_column], df[lat_column]), crs= 4326)

    # ## Convert to Albers Equal Area
    gdf['geometry_albers'] = gdf['geometry'].to_crs(epsg=5070)

    ## Create buffer round the point geometry for quarter mile radius

    gdf['polygon_quartermile'] = gdf['geometry_albers'].buffer(402.336)  # buffer func - buffer(buffer_value)

    # Create buffer round the point geometry for one mile radius

    gdf['polygon_onemile'] = gdf['geometry_albers'].buffer(1609.34)  # buffer func - buffer(buffer_value)

    df['bb_small'] = gdf['polygon_quartermile'].apply(format_bounds_str)
    df['bb_big'] = gdf['polygon_onemile'].apply(format_bounds_str)


if __name__ == "__main__":
    df = pd.read_csv('https://raw.githubusercontent.com/Imageomics/LatLonCover/main/someCoordinates.csv')
    add_albers_bounding_boxes(df, lat_column='Lat', lon_column='Lon')
    print(df.head(2))
    print('bb_small')
    print(df.head()['bb_small'][0])
    print('bb_big')
    print(df.head()['bb_big'][0])
