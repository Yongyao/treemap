# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 14:39:54 2018

@author: Yongyao Jiang
"""

from osgeo import gdal, gdal_array
import numpy as np
import matplotlib.pyplot as plt

# Tell GDAL to throw Python exceptions, and register all drivers
gdal.UseExceptions()
gdal.AllRegister()

def array_to_raster(array, output_path, ref_path):    
    Image = gdal.Open(ref_path, gdal.GA_ReadOnly)     

    Output = gdal.GetDriverByName('GTiff').Create(output_path, Image.RasterXSize, Image.RasterYSize, 1, gdal.GDT_Float32, options=['COMPRESS=DEFLATE'])
    Output.SetProjection(Image.GetProjectionRef())
    Output.SetGeoTransform(Image.GetGeoTransform()) 
    Output.GetRasterBand(1).WriteArray(array)
    Output.FlushCache()  # Write to disk.
    return Output, Output.GetRasterBand(1)

# read landsat image
input_image = '/Users/yjiang/Documents/pythonWorkspace/treemap/Data/geoeye_palm/subsets5_all_bands/500_0.tif'
img_ds = gdal.Open(input_image, gdal.GA_ReadOnly)
img = np.zeros((img_ds.RasterYSize, img_ds.RasterXSize, img_ds.RasterCount),
               gdal_array.GDALTypeCodeToNumericTypeCode(img_ds.GetRasterBand(1).DataType))
for b in range(img.shape[2]):
    img[:, :, b] = img_ds.GetRasterBand(b + 1).ReadAsArray()

mask = np.zeros((img_ds.RasterYSize, img_ds.RasterXSize))
mask[~np.isnan(img[:, :, 1])] = 1
# Display them
# plt.imshow(mask)
# plt.title('mask image')

nir = img[:,:,img_ds.RasterCount-1]
red = img[:,:,img_ds.RasterCount-2]
ndvi = (nir-red)/(nir + red)
plt.imshow(ndvi)

# stack.tif doesn't have CRS/projection info
ref_img = '/Users/yjiang/Documents/pythonWorkspace/treemap/Data/geoeye_palm/subsets5_all_bands/500_0.tif'
array_to_raster(ndvi, '/Users/yjiang/Documents/pythonWorkspace/treemap/Data/geoeye_palm/ndvi.tif' , ref_img)
