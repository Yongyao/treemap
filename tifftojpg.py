#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 10:48:17 2018

@author: yjiang
"""

from PIL import Image
import os

# =============================================================================
# input_dir = '/Users/yjiang/Documents/pythonWorkspace/treemap/Data/geoeye_palm/subsets3_500/'
# output_dir = '/Users/yjiang/Documents/pythonWorkspace/treemap/Data/geoeye_palm/subsets3_500_jpg/'
# 
# for filename in os.listdir(input_dir):
#     if filename.endswith(".tif"):
#         im = Image.open(os.path.join(input_dir, filename))
#         im.save(os.path.join(output_dir, filename.replace('tif', 'jpeg'))) 
# =============================================================================
        
        
output_dir = '/Users/yjiang/Documents/pythonWorkspace/treemap/Data/geoeye_palm/subsets3_500_jpg/'

f = open(os.path.join(output_dir, 's3index.csv'), 'w')

for filename in os.listdir(output_dir):
    if filename.endswith("jpeg"):
        f.write('https://s3.us-east-2.amazonaws.com/palmtreejpg2/'+filename +'\n')
    
f.close()    
