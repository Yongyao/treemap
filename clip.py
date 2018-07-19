#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:55:41 2018

@author: yjiang
"""

from osgeo import gdal, gdal_array
import numpy as np
import matplotlib.pyplot as plt

# Tell GDAL to throw Python exceptions, and register all drivers
gdal.UseExceptions()
gdal.AllRegister()

# read landsat image
def read(path):  
    img_ds = gdal.Open(path, gdal.GA_ReadOnly)
    img = np.zeros((img_ds.RasterYSize, img_ds.RasterXSize, img_ds.RasterCount),
                   gdal_array.GDALTypeCodeToNumericTypeCode(img_ds.GetRasterBand(1).DataType))
    for b in range(img.shape[2]):
        img[:, :, b] = img_ds.GetRasterBand(b + 1).ReadAsArray()
    return img

def array_to_raster(array, output_path, ref_path):    
    Image = gdal.Open(ref_path, gdal.GA_ReadOnly)     

    Output = gdal.GetDriverByName('GTiff').Create(output_path, array.shape[1], array.shape[0], array.shape[2], Image.GetRasterBand(1).DataType, options=['COMPRESS=DEFLATE'])
    Output.SetProjection(Image.GetProjectionRef())
    Output.SetGeoTransform(Image.GetGeoTransform()) 
    # Output.GetRasterBand(1).WriteArray(array)
    for i in range(array.shape[2]):
         Output.GetRasterBand(i+1).WriteArray(array[:,:,i])   
    Output.FlushCache()  # Write to disk.
    
def array_to_raster_1b(array, output_path, ref_path):    
    Image = gdal.Open(ref_path, gdal.GA_ReadOnly)     

    Output = gdal.GetDriverByName('GTiff').Create(output_path, array.shape[1], array.shape[0], 1, Image.GetRasterBand(1).DataType, options=['COMPRESS=DEFLATE'])
    Output.SetProjection(Image.GetProjectionRef())
    Output.SetGeoTransform(Image.GetGeoTransform()) 
    Output.GetRasterBand(1).WriteArray(array)
    Output.FlushCache()  # Write to disk.
    
def normalize(arr):
    ''' Function to normalize an input array to 0-1 '''
    norm = arr
    for i in range(arr.shape[2]):
        arr_min = arr[:,:,i].min()
        arr_max = arr[:,:,i].max()
        norm[:,:,i] = (arr[:,:,i] - arr_min) / (arr_max - arr_min)
    return norm

dg_path = '/Users/yjiang/Documents/pythonWorkspace/treemap/Data/geoeye_palm/058049902010_01/058049902010_01_P001_PSH/18APR30023003-S3DS-058049902010_01_P001.TIF'
img = read(dg_path)

# pairing X and y
rows = img.shape[0]
cols = img.shape[1]
band_num = img.shape[2]

#==============================================================================
# norm = normalize(img)
# plt.imshow(norm)
#==============================================================================

# =============================================================================
# outdir = '/Users/yjiang/Documents/pythonWorkspace/treemap/Data/geoeye_palm/subsets3/'
# size = 260
# for i in range(0, rows, size):
#     for j in range(0, cols, size):
#         subset = img[i:i+size, j:j+size, 0:3]
#         # norm = normalize(subset)
#         array_to_raster(subset, outdir+str(i)+'_'+str(j)+'.tif', dg_path)
# =============================================================================
outdir = '/Users/yjiang/Documents/pythonWorkspace/treemap/Data/geoeye_palm/subsets5_all_bands/'
size = 500
for i in range(0, rows, size):
    for j in range(0, cols, size):
        subset = img[i:i+size, j:j+size, :]
        # norm = normalize(subset)
        # array_to_raster_1b(subset, outdir+str(i)+'_'+str(j)+'.tif', dg_path)
        array_to_raster(subset, outdir+str(i)+'_'+str(j)+'.tif', dg_path)
    