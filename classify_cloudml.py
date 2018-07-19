#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 14:26:17 2018

@author: yjiang
"""

import skimage.io as io
from osgeo import gdal, gdal_array
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics, cross_validation
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.externals import joblib
import cloudml

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

    Output = gdal.GetDriverByName('GTiff').Create(output_path, Image.RasterXSize, Image.RasterYSize, 1, gdal.GDT_Float32, options=['COMPRESS=DEFLATE'])
    Output.SetProjection(Image.GetProjectionRef())
    Output.SetGeoTransform(Image.GetGeoTransform()) 
    Output.GetRasterBand(1).WriteArray(array)
    Output.FlushCache()  # Write to disk.

landsat_path = '/Users/yjiang/Documents/pythonWorkspace/treemap/Data/landsat_clip.tif'
landsat = read(landsat_path)
img = landsat

# pairing X and y
rows = img.shape[0]
cols = img.shape[1]
band_num = img.shape[2]

# create mask image
mask_landsat = np.zeros((rows, cols))
mask_landsat[~np.isnan(landsat[:, :, 1])] = 1
mask = mask_landsat

# handle missing value
img[np.isnan(img)] = 0

# making prediction, save and print the output

print 'start prediction'

img_list = img.reshape(cols*rows, band_num).tolist()
predict_list = []
for i in range(0, cols*rows, 100):
    predict_list.append(cloudml.predict_json('eotest-207015', 'landsat', img_list[i:i+100]))
    
    
# predict_list = cloudml.predict_json('eotest-207015', 'landsat', img.reshape(cols*rows, band_num).tolist())
predict = np.asarray(predict_list, dtype=np.float32)
output = predict.reshape(rows, cols)*mask

plt.imshow(output, cmap=plt.cm.Spectral)
path = '/Users/yjiang/Documents/pythonWorkspace/treemap/Data/classification_cloud.tif'
# io.imsave(path, output)
array_to_raster(output, path, landsat_path)

