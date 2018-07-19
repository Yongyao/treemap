#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 12:09:31 2018

@author: yjiang
"""

import random
from os import listdir
from os.path import isfile, join
from shutil import copyfile

foo = ['a', 'b', 'c', 'd', 'e']
print(random.choice(foo))

indir = '/Users/yjiang/Documents/pythonWorkspace/treemap/Data/geoeye_palm/subsets3/'
files = [f for f in listdir(indir) if isfile(join(indir, f))]

outdir = '/Users/yjiang/Documents/pythonWorkspace/treemap/Data/geoeye_palm/subsets3_500/'
for i in range(590):
    base_name = random.choice(files)
    full_path = indir + base_name
    copyfile(full_path, outdir+base_name)
    