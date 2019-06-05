'''
Kyle: This script looks through a gdb and defines the projection for everything in the gdb
Made by Rachel Joseph
Started: 6/5/2019
Last updated: 6/5/2019
'''

import arcpy

#Environmental settings 
arcpy.env.overwriteOutput = True

#variables
spatialRef = "102736" #NAD_1983_2011_StatePlane_Tennessee_FIPS_4100_Ft_US
gdb = arcpy.env.workspace = arcpy.GetParameterAsText(0) #r"D:\ProductionTools\Kyle\TestData\MOBRAN18_TerrainProducts.gdb" #

try:
    fileList = arcpy.ListFeatureClasses()
    arcpy.AddMessage("List of Feature Classes Generated")
    arcpy.AddMessage("Starting to define projection")
    for feature in fileList:
        #featureClass = "{}\{}".format(gdb, feature)
        arcpy.DefineProjection_management (feature, spatialRef)
    arcpy.AddMessage("Projection of all feature classes defined")

except Exception as e:
    print e
    arcpy.AddMessage("e")

else:
    print("Program Completed without Error")
    arcpy.AddMessage("Program Completed without Error")