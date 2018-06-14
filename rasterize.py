# -*- coding: utf-8 -*-
"""
Convert a shp into a raster image according to a referece raster
"""
# A script to rasterise a shapefile to the same projection & 
# pixel resolution as a reference image.
from osgeo import ogr, gdal
import subprocess

# =============================================================================
# # for test 1
# InputVector = 'C:\\Users\\Yongyao Jiang\\Downloads\\test\\training2\\non-palm.shp'
# OutputImage = 'C:\\Users\\Yongyao Jiang\\Downloads\\test\\training2\\non-palm.tif'
# 
# RefImage = 'C:\\Users\\Yongyao Jiang\\Downloads\\test\\mask.tif'
# =============================================================================

# for test 2
InputVector = 'C:\\Users\\Yongyao Jiang\\Downloads\\test2\\training\\non-palm.shp'
OutputImage = 'C:\\Users\\Yongyao Jiang\\Downloads\\test2\\training\\non-palm.tif'
RefImage = 'C:\\Users\\Yongyao Jiang\\Downloads\\test2\\mask.tif'

gdalformat = 'GTiff'
datatype = gdal.GDT_Byte
burnVal = 2 #value for the output image pixels
##########################################################
# Get projection info from reference image
Image = gdal.Open(RefImage, gdal.GA_ReadOnly)

# Open Shapefile
Shapefile = ogr.Open(InputVector)
Shapefile_layer = Shapefile.GetLayer()

# Rasterise
print("Rasterising shapefile...")
Output = gdal.GetDriverByName(gdalformat).Create(OutputImage, Image.RasterXSize, Image.RasterYSize, 1, datatype, options=['COMPRESS=DEFLATE'])
Output.SetProjection(Image.GetProjectionRef())
Output.SetGeoTransform(Image.GetGeoTransform()) 

# Write data to band 1
Band = Output.GetRasterBand(1)
Band.SetNoDataValue(0)
Band.Fill(0)
gdal.RasterizeLayer(Output, [1], Shapefile_layer, burn_values=[burnVal])

# Close datasets
Band = None
Output = None
Image = None
Shapefile = None

# Build image overviews
subprocess.call("gdaladdo --config COMPRESS_OVERVIEW DEFLATE "+OutputImage+" 2 4 8 16 32 64", shell=True)
print("Done.")
