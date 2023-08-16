#double check classifications and strip white space
setwd("~/Documents/research/imageomics/quest/latLonCover/LatLonCover/cropScapeDocumentation")


library(rio)
sub<-import("CDL_subcategories.xlsx", which=3)
dim(sub)
head(sub)
table(sub$courseClass, useNA = "always")
table(sub$fineClass, useNA = "always")

#uhoh, has white space?
sub$courseClass<-trimws(sub$courseClass, "both")
sub$fineClass<-trimws(sub$fineClass, "both")
table(sub$courseClass, useNA = "always")
table(sub$fineClass, useNA = "always")


crsLeg<-import("CDL_subcategories.xlsx", which=4)
crsLeg$Class<-trimws(crsLeg$Class, "both")
crsLeg$Definition<-trimws(crsLeg$Definition, "both")
crsLeg

crsFine<-import("CDL_subcategories.xlsx", which=5)
crsFine$Class<-trimws(crsFine$Class, "both")
crsFine$Definition<-trimws(crsFine$Definition, "both")
crsFine

## EXPORT THE CSV FILES

write.table(sub, "CDL_subcategories.csv", sep=",", quote=FALSE, row.names = FALSE, col.names = TRUE)
write.table(crsLeg, "CDL_subcategories_legendCrse.csv", sep=",", quote=FALSE, row.names = FALSE, col.names = TRUE)
write.table(crsFine, "CDL_subcategories_legendFine.csv", sep=",", quote=FALSE, row.names = FALSE, col.names = TRUE)

