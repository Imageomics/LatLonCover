# LatLonCover
Land usage descriptions for neighborhoods around given lat/long

## Documentation

## Data Sources

### iNaturalist

We use locations from citizen science organism reporting.

"iNaturalist is a global community of naturalists, scientists, and members of the public sharing over a million wildlife sightings to teach one another about the natural world while creating high-quality citizen science data for science and conservation". [1]
[iNaturalist API](https://api.inaturalist.org/v1/docs/)

### Cropland Data Layer (CDL)

"The geospatial data product called the Cropland Data Layer (CDL) is hosted on CropScape (https://nassgeodata.gmu.edu/CropScape/). The CDL is a raster, geo-referenced, crop-specific land cover data layer created annually for the continental United States using moderate resolution satellite imagery and extensive agricultural ground truth [2]." All historical CDL products are available for use and free for download through [CropScape](https://nassgeodata.gmu.edu/CropScape/devhelp/help.html).

#### Cropscape category codes

We used the category codes and names used in CropScape ["List of CDL codes, class names, and RGB color values"](https://www.nass.usda.gov/Research_and_Science/Cropland/docs/CDL_codes_names_colors.xlsx) by reducing the full set of provided categories into select categories of interest and groups of combined categories.


### References

[1] iNatualist API.(n.d.). https://api.inaturalist.org/v1/docs/ 

[2] Boryan, Claire, Zhengwei Yang, Rick Mueller, and Mike Craig. 2011. Monitoring US Agriculture: The US Department of Agriculture, National Agricultural Statistics Service, Cropland Data Layer Program. Geocarto International 26 (5): 341–58. https://doi.org/10.1080/10106049.2011.562309.

[3] Han, Weiguo, Zhengwei Yang, Liping Di, and Richard Mueller. 2012. CropScape: A Web Service Based Application for Exploring and Disseminating US Conterminous Geospatial Cropland Data Products for Decision Support. Computers and Electronics in Agriculture 84 (June): 111–23. https://doi.org/10.1016/j.compag.2012.03.005.
