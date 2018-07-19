#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 14:09:13 2018

@author: yjiang
"""

#==============================================================================
# import numpy as np
# import scipy
# import scipy.ndimage as ndimage
# import scipy.ndimage.filters as filters
# import matplotlib.pyplot as plt
# 
# fname = '/Users/yjiang/Documents/pythonWorkspace/treemap/Data/geoeye_palm/subsets4_nir/0_5500.tif'
# neighborhood_size = 5
# threshold = 55
# 
# data = scipy.misc.imread(fname)
# 
# data_max = filters.maximum_filter(data, neighborhood_size)
# maxima = (data == data_max)
# data_min = filters.minimum_filter(data, neighborhood_size)
# diff = ((data_max - data_min) > threshold)
# maxima[diff == 0] = 0
# 
# labeled, num_objects = ndimage.label(maxima)
# slices = ndimage.find_objects(labeled)
# x, y = [], []
# for dy,dx in slices:
#     x_center = (dx.start + dx.stop - 1)/2
#     x.append(x_center)
#     y_center = (dy.start + dy.stop - 1)/2    
#     y.append(y_center)
# 
# plt.imshow(data)
# #plt.savefig('/tmp/data.png', bbox_inches = 'tight')
# 
# plt.autoscale(False)
# plt.plot(x,y, 'r.')
# # plt.savefig('/tmp/result.png', bbox_inches = 'tight')
#==============================================================================
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
from skimage.feature import peak_local_max
from skimage import data, img_as_float
import skimage.io as io

# im = img_as_float(data.coins())
im = io.imread('/Users/yjiang/Documents/pythonWorkspace/treemap/Data/geoeye_palm/subsets4_nir/500_0.tif')
#500_0

threshold = 10
# image_max is the dilation of im with a 20*20 structuring element
# It is used within peak_local_max function
image_max = ndi.maximum_filter(im, size=threshold, mode='constant')

# Comparison between image_max and im to find the coordinates of local maxima
coordinates = peak_local_max(im, min_distance=threshold)

# display results
fig, axes = plt.subplots(1, 3, figsize=(10, 4), sharex=True, sharey=True)
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

fig.tight_layout()

plt.show()
