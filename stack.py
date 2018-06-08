# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 10:18:01 2018
stack multiple bands into a single TIF (it 
has some projection issue), better to use 
gdal_merge or merge tool in QGIS (processing - toolbox search "merge")
@author: Yongyao Jiang
"""

import rasterio
from osgeo import gdal, gdal_array

# gdal.SetConfigOption("GDAL_DATA", "C:\\Users\\Yongyao Jiang\\AppData\\Local\\Continuum\\anaconda3\\Library\\share\\gdal");

# =============================================================================
# def array_to_raster(array, output_path, ref_path):    
#     Image = gdal.Open(ref_path, gdal.GA_ReadOnly)     
# 
#     Output = gdal.GetDriverByName('GTiff').Create(output_path, Image.RasterXSize, Image.RasterYSize, 1, gdal.GDT_Float32, options=['COMPRESS=DEFLATE'])
#     Output.SetProjection(Image.GetProjectionRef())
#     Output.SetGeoTransform(Image.GetGeoTransform()) 
#     for i in range(array.shape[2]):
#         Output.GetRasterBand(i+1).WriteArray(array[:,:,i])        
#     Output.FlushCache()  # Write to disk.
# =============================================================================

raster  = 'C:\\Users\\Yongyao Jiang\\Downloads\\test\\RT_LC08_L1TP_117056_20180430_20180502_01_T1_B'
file_list = []

for i in range(2, 6):
    file_list.append(raster + str(i) + ".TIF")
    
# Read metadata of first file
with rasterio.open(file_list[0]) as src0:
    meta = src0.meta

# Update meta to reflect the number of layers
meta.update(count = len(file_list))

# Read each layer and write it to stack

with rasterio.open('C:\\Users\\Yongyao Jiang\\Downloads\\test\\stack.tif', 'w', **meta) as dst:
    for id, layer in enumerate(file_list):
        with rasterio.open(layer) as src1:
            dst.write_band(id + 1, src1.read(1))
