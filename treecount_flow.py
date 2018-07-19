#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:28:24 2018
ref 1: https://stackoverflow.com/questions/9111711/get-coordinates-of-local-maxima-in-2d-array-above-certain-value
ref 2: http://scikit-image.org/docs/dev/auto_examples/segmentation/plot_peak_local_max.html
@author: yjiang
"""

from scipy import ndimage as ndi
import matplotlib.pyplot as plt
from skimage.feature import peak_local_max
import skimage.io as io
from numpy import array

in_path = '/Users/yjiang/Documents/pythonWorkspace/treemap/Data/geoeye_palm/subsets5_all_bands/500_0.tif'
img = io.imread(in_path)
im = img[:,:,3]


nir = img[:,:,3]
red = img[:,:,2]
ndvi = (nir-red)/(nir + red)

# mask = np.zeros((img_ds.RasterYSize, img_ds.RasterXSize))
mask = (ndvi>0.5)
# im = im*mask
# mask[~np.isnan(img[:, :, 1])] = 1

#0_5500

threshold = 10
# image_max is the dilation of im with a 20*20 structuring element
# It is used within peak_local_max function
image_max = ndi.maximum_filter(im, size=threshold, mode='constant')

# Comparison between image_max and im to find the coordinates of local maxima
coordinates = peak_local_max(im, min_distance=threshold)

# display results
fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharex=True, sharey=True)
ax = axes.ravel()
ax[0].imshow(im, cmap=plt.cm.gray)
ax[0].axis('off')
ax[0].set_title('Original')

ax[1].imshow(image_max, cmap=plt.cm.gray)
ax[1].axis('off')
ax[1].set_title('Maximum filter')

ax[2].imshow(im, cmap=plt.cm.gray)
ax[2].autoscale(False)
ax[2].plot(coordinates[:, 1], coordinates[:, 0], 'r.')
ax[2].axis('off')
ax[2].set_title('Peak local max')

#im_filtered = mask*im
#coordinates_filtered = peak_local_max(im_filtered, min_distance=threshold)

coordinates_filtered_arr = []
for i in range(coordinates.shape[0]):
    col = coordinates[i, 1]
    row = coordinates[i, 0]
    if mask[row, col]:
        coordinates_filtered_arr.append(coordinates[i])
coordinates_filtered = array(coordinates_filtered_arr)
        
        
ax[3].imshow(im, cmap=plt.cm.gray)
ax[3].autoscale(False)
ax[3].plot(coordinates_filtered[:, 1], coordinates_filtered[:, 0], 'r.')
ax[3].axis('off')
ax[3].set_title('Peak local max filtered by NDVI')

fig.tight_layout()

plt.show()
