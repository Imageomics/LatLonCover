# LatLonCover
Land usage descriptions for neighborhoods around given lat/long

## Data Sources

### iNaturalist

We use locations from citizen science organism reporting.

"iNaturalist is a global community of naturalists, scientists, and members of the public sharing over a million wildlife sightings to teach one another about the natural world while creating high-quality citizen science data for science and conservation". [1]
[iNaturalist API](https://api.inaturalist.org/v1/docs/)

### Cropland Data Layer (CDL)

"The geospatial data product called the Cropland Data Layer (CDL) is hosted on CropScape (https://nassgeodata.gmu.edu/CropScape/). The CDL is a raster, geo-referenced, crop-specific land cover data layer created annually for the continental United States using moderate resolution satellite imagery and extensive agricultural ground truth [2]." All historical CDL products are available for use and free for download through [CropScape](https://nassgeodata.gmu.edu/CropScape/devhelp/help.html).

We are using the web service "GetCDLStat" to supply a csv with count and acrage of various crop and land use categories.  The inputs we are supplying are year, bounding box, and format which then supplies the a csv file with these data. Bounding boxes use coordinates in the projection of USA Contiguous Albers Equal Area,USGS version [see WSDL](https://nassgeodata.gmu.edu/axis2/services/CDLService?wsdl)

Example:
* `https://nassgeodata.gmu.edu/axis2/services/CDLService/GetCDLStat?year=2018&bbox=130783,2203171,153923,2217961&format=csv`
* supplies csv: `https://nassgeodata.gmu.edu/webservice/nass_data_cache/CDL_2018_clip_20230815110236_390867377.csv`

<pre>
Value, Category, Count,  Acreage
1, Corn, 184246, 40975.3
5, Soybeans, 133819, 29760.6
28, Oats, 338, 75.2
36, Alfalfa, 691, 153.7
37, Other Hay/Non Alfalfa, 449, 99.9
60, Switchgrass, 1, 0.2
61, Fallow/Idle Cropland, 4, 0.9
111, Open Water, 865, 192.4
121, Developed/Open Space, 19409, 4316.5
122, Developed/Low Intensity, 2736, 608.5
123, Developed/Medium Intensity, 743, 165.2
124, Developed/High Intensity, 109, 24.2
131, Barren, 312, 69.4
141, Deciduous Forest, 1418, 315.4
143, Mixed Forest, 3, 0.7
152, Shrubland, 16, 3.6
176, Grass/Pasture, 20899, 4647.8
190, Woody Wetlands, 8297, 1845.2
195, Herbaceous Wetlands, 5748, 1278.3
</pre>

#### Cropscape category codes

We used the category codes and names used in CropScape ["List of CDL codes, class names, and RGB color values"](https://www.nass.usda.gov/Research_and_Science/Cropland/docs/CDL_codes_names_colors.xlsx) by reducing the full set of provided categories into select categories of interest and groups of combined categories.


### References

[1] iNatualist API.(n.d.). https://api.inaturalist.org/v1/docs/ 

[2] Boryan, Claire, Zhengwei Yang, Rick Mueller, and Mike Craig. 2011. Monitoring US Agriculture: The US Department of Agriculture, National Agricultural Statistics Service, Cropland Data Layer Program. Geocarto International 26 (5): 341–58. https://doi.org/10.1080/10106049.2011.562309.

[3] Han, Weiguo, Zhengwei Yang, Liping Di, and Richard Mueller. 2012. CropScape: A Web Service Based Application for Exploring and Disseminating US Conterminous Geospatial Cropland Data Products for Decision Support. Computers and Electronics in Agriculture 84 (June): 111–23. https://doi.org/10.1016/j.compag.2012.03.005.
