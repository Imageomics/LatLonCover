#double check classifications and strip white space
setwd("~/Documents/research/imageomics/quest/latLonCover/LatLonCover/cropScapeDocumentation")



sub<-read.table("CDL_subcategories.csv", sep=",", header=TRUE, stringsAsFactors = FALSE)
dim(sub)
table(sub$courseClass, useNA = "always")
table(sub$fineClass, useNA = "always")

#uhoh, has white space
sub$courseClass<-trimws(sub$courseClass, "both")
sub$fineClass<-trimws(sub$fineClass, "both")
table(sub$courseClass, useNA = "always")
table(sub$fineClass, useNA = "always")


crsLeg<-read.table("CDL_subcategories_legendCrse.csv", sep=",", header=TRUE, stringsAsFactors = FALSE)
crsLeg$Class<-trimws(crsLeg$Class, "both")
crsLeg$Definition<-trimws(crsLeg$Definition, "both")
crsLeg

crsFine<-read.table("CDL_subcategories_legendFine.csv", sep=",", header=TRUE, stringsAsFactors = FALSE)
crsFine$Class<-trimws(crsFine$Class, "both")
crsFine$Definition<-trimws(crsFine$Definition, "both")
crsFine

## EXPORT THE CSV FILES

write.table(sub, "CDL_subcategories.csv", quote=FALSE, row.names = FALSE, col.names = TRUE)
write.table(crsLeg, "CDL_subcategories_legendCrse.csv", quote=FALSE, row.names = FALSE, col.names = TRUE)
write.table(crsFine, "CDL_subcategories_legendFine.csv", quote=FALSE, row.names = FALSE, col.names = TRUE)

