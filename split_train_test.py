#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 16:04:46 2018

@author: yjiang
"""

import csv
from os.path import isfile, join
from shutil import copyfile

#==============================================================================
# indir = '/Users/yjiang/Documents/pythonWorkspace/raccoon_dataset/images/'
# outdir = '/Users/yjiang/Documents/pythonWorkspace/raccoon_dataset/data/test_image/'
# with open('/Users/yjiang/Documents/pythonWorkspace/raccoon_dataset/data/test_labels.csv') as fh:
#        for line in fh:
#            row = line.split(',')
#            if 'jpg' in row[0]:
#                print line
#                copyfile(indir+row[0], outdir+row[0])
#==============================================================================

indir = '/Users/yjiang/Documents/pythonWorkspace/raccoon_dataset/annotations/'
outdir = '/Users/yjiang/Documents/pythonWorkspace/raccoon_dataset/data/train_anno/'
with open('/Users/yjiang/Documents/pythonWorkspace/raccoon_dataset/data/train_labels.csv') as fh:
       for line in fh:
           row = line.split(',')
           if 'jpg' in row[0]:
               print line
               filename = row[0].replace('jpg','xml')
               copyfile(indir+filename, outdir+filename)
