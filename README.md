# LatLonCover
Land usage descriptions for neighborhoods around given lat/long

## Documentation

## Data Sources

### iNaturalist

We use locations from citizen science organisms reporting.

iNaturalist is a global community of naturalists, scientists, and members of the public sharing over a million wildlife sightings to teach one another about the natural world while creating high-quality citizen science data for science and conservation [1].
[iNaturalist API](https://api.inaturalist.org/v1/docs/)

### Cropland Data Layer (CDL)

CroplandCROS (https://croplandcros.scinet.usda.gov/), the geospatial data product hosts the Cropland Data Layer (CDL).

The [Cropland Data Layer (CDL)](https://www.nass.usda.gov/Research_and_Science/Cropland/sarsfaqs2.php) is a data product produced by the National Agricultural Statistics Service of U.S. Department of Agriculture. It provides geo-referenced, high accuracy, 30 or 56 meter resolution, crop-specific cropland land cover information for up to 48 contiguous states in the U.S. from 1997 to the present. This data product has been extensively used in agricultural research [1].

CropScape is an interactive Web CDL exploring system, and it was developed to query, visualize, disseminate, and analyze CDL data geospatially through standard geospatial Web services in a publicly accessible online environment[2]. The development of the CropScapeR package is to allow R users to easily utilize the geospatial processing services provided by CropScape, so that they can effectively and efficiently access and analyze the CDL data.

### References

[1] iNatualist API.(n.d.). https://api.inaturalist.org/v1/docs/ 
[2] Boryan, Claire, Zhengwei Yang, Rick Mueller, and Mike Craig. 2011. Monitoring US Agriculture: The US Department of Agriculture, National Agricultural Statistics Service, Cropland Data Layer Program. Geocarto International 26 (5): 341–58. https://doi.org/10.1080/10106049.2011.562309.

[3] Han, Weiguo, Zhengwei Yang, Liping Di, and Richard Mueller. 2012. CropScape: A Web Service Based Application for Exploring and Disseminating US Conterminous Geospatial Cropland Data Products for Decision Support. Computers and Electronics in Agriculture 84 (June): 111–23. https://doi.org/10.1016/j.compag.2012.03.005.
