# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 16:37:26 2018
This version is not working currently
@author: Yongyao Jiang
"""

import sys
sys.path.append('C:\\Program Files\\GDAL')
import gdal_merge as gm

sys.argv = "-ot Float32 -separate -o \" C:\\\\Users\\\\Yongyao Jiang\\\\Downloads\\\\test\\\\landsat.tif\" -of GTiff \"C:\\\\Users\\\\Yongyao Jiang\\\\Downloads\\\\test\\\\RT_LC08_L1TP_117056_20180430_20180502_01_T1_B5.TIF\" \"C:\\\\Users\\\\Yongyao Jiang\\\\Downloads\\\\test\\\\RT_LC08_L1TP_117056_20180430_20180502_01_T1_B3.TIF\" \"C:\\\\Users\\\\Yongyao Jiang\\\\Downloads\\\\test\\\\RT_LC08_L1TP_117056_20180430_20180502_01_T1_B4.TIF\" \"C:\\\\Users\\\\Yongyao Jiang\\\\Downloads\\\\test\\\\RT_LC08_L1TP_117056_20180430_20180502_01_T1_B2.TIF\"".split()
gm.main()