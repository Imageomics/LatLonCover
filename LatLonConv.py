# import libraries

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import box  # use shapely to add grid
import os
from fiona.crs import from_epsg
import numpy as np


# read csv and display head

df = pd.read_csv('https://raw.githubusercontent.com/Imageomics/LatLonCover/main/someCoordinates.csv')
df.head(2)


# Convert lat and long to point geometry

gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df['Lon'], df['Lat']), crs= 4326)


# ## Convert to Albers Equal Area
gdf['geometry_albers'] = gdf['geometry'].to_crs(epsg=5070)
gdf.head(2)

## Create buffer round the point geometry for quarter mile radius

gdf['polygon_quartermile'] = gdf['geometry_albers'].buffer(402.336)  # buffer func - buffer(buffer_value)
gdf.head(2)

# Create buffer round the point geometry for one mile radius

gdf['polygon_onemile'] = gdf['geometry_albers'].buffer(1609.34)  # buffer func - buffer(buffer_value)
gdf.head(2)