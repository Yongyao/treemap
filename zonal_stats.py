#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 14:38:07 2018

@author: yjiang
"""

from rasterstats import zonal_stats

# make sure shp has a defined projection, otherwise it is not gonna work
# the shp converted directly from shp woundn't work

# https://gis.stackexchange.com/questions/208441/zonal-statistics-of-a-polygon-and-assigning-mean-value-to-the-polygon 
# https://gis.stackexchange.com/questions/126965/gdal-rasterize-error-attempt-to-create-0x0-dataset-is-illegal 
stats2 = zonal_stats("/Users/yjiang/Downloads/bra_saveasS/bra_saveasS.shp", "Data/zonal_test/bra_ndvi.tiff",
            stats=['count', 'mean'], geojson_out=True)

for stat in stats2:
    print stat['properties']['mean'], stat['properties']['count'], stat['properties']['ID_3']