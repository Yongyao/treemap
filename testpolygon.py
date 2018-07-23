#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 21:07:15 2018

@author: yjiang
"""
import datetime
import csv

class SceneInfo:
   def __init__ (self, line):
      try:
        self.SCENE_ID, self.FULL_ID, self.SPACECRAFT_ID, self.SENSOR_ID, self.DATE_ACQUIRED, self.COLLECTION_NUMBER, self.COLLECTION_CATEGORY, self.EXACT_TIME, self.DATA_TYPE, self.WRS_PATH, self.WRS_ROW, self.CLOUD_COVER, self.NORTH_LAT, self.SOUTH_LAT, self.WEST_LON, self.EAST_LON, self.TOTAL_SIZE, self.BASE_URL = line.split(',')

        self.DATE_ACQUIRED = datetime.datetime.strptime(self.DATE_ACQUIRED, '%Y-%m-%d')
        self.NORTH_LAT = float(self.NORTH_LAT)
        self.SOUTH_LAT = float(self.SOUTH_LAT)
        self.WEST_LON = float(self.WEST_LON)
        self.EAST_LON = float(self.EAST_LON)
        self.CLOUD_COVER = float(self.CLOUD_COVER)
      except:
        self.DATE_ACQUIRED = None
        # print "WARNING! format error on {", line, "}"        

   def contains(self, lat, lon):
      return (lat > self.SOUTH_LAT) and (lat < self.NORTH_LAT) and (lon > self.WEST_LON) and (lon < self.EAST_LON)

   def intersects(self, slat, wlon, nlat, elon):
      return (nlat > self.SOUTH_LAT) and (slat < self.NORTH_LAT) and (elon > self.WEST_LON) and (wlon < self.EAST_LON)

   def month_path_row(self):
      return '{}-{}-{}'.format(self.yrmon(), self.WRS_PATH, self.WRS_ROW)

   def yrmon(self):
      return '{}-{:02d}'.format(self.DATE_ACQUIRED.year, self.DATE_ACQUIRED.month)
  
   def printInfo(self):
       pass
      # print self.NORTH_LAT, self.SOUTH_LAT, self.WEST_LON, self.EAST_LON
      
class AlosSceneInfo:
   def __init__ (self, line):
      try:
        self.Granule_Name, self.Path_Number,self.Frame_Number,self.Start_Time,self.End_Time,self.Center_Lat,self.Center_Lon,self.Near_Start_Lat,self.Near_Start_Lon,self.Far_Start_Lat,self.Far_Start_Lon,self.Near_End_Lat,self.Near_End_Lon,self.Far_End_Lat,self.Far_End_Lon,self.URL = line.split(',')

        self.Center_Lat = float(self.Center_Lat)
        self.Center_Lon = float(self.Center_Lon)
      except:
        self.Center_Lat = None

def filterByLocation(scene, lat, lon):
   if scene.contains(lat, lon):
      yield scene

def filterByArea(scene, slat, wlon, nlat, elon):
   if scene.intersects(slat, wlon, nlat, elon):
      yield scene

def clearest(scenes):
   if scenes:
      return min(scenes, key=lambda s: s.CLOUD_COVER)
   else:
      return None

# fh = open('/Users/yjiang/Documents/pythonWorkspace/treemap/Data/2015index.txt')
# fh = open('/Users/yjiang/Downloads/index.csv')
# =============================================================================
# f = open('/Users/yjiang/Downloads/index_13_17_small_test.txt','w')
# 
# with open('/Users/yjiang/Downloads/index.csv') as fh:
#        for line in fh:
#            scene = SceneInfo(line)
#            if scene.DATE_ACQUIRED is not None:
#                print line
#                yr = scene.DATE_ACQUIRED.year
#                if yr>=2013 and yr<=2017:
#                    f.write(line)
# =============================================================================

# fh.close()
# f.close()

# =============================================================================
# lat =-1.71; lon = 114.35     # center of Reunion Island
# dlat = 0.5; dlon = 0.5
# with open('/Users/yjiang/Downloads/index.csv') as fh:
#        for line in fh:
#            scene = SceneInfo(line)
#            if scene.DATE_ACQUIRED is not None and \
#            scene.DATE_ACQUIRED.year==2010 and \
#            scene.intersects(lat-dlat,lon-dlon,lat+dlat,lon+dlon):
#                print(line)
# =============================================================================
with open('/Users/yjiang/Documents/pythonWorkspace/treemap/Data/landsat_index_small.txt') as fh:
       for line in fh:
           scene = SceneInfo(line)
           with open('/Users/yjiang/Documents/pythonWorkspace/treemap/Data/alos_index_small.csv') as fa:
               for line_fa in fa:
                   alos = AlosSceneInfo(line_fa)
                   if alos.Center_Lat is not None and scene.contains(alos.Center_Lat, alos.Center_Lon):
                       print(line_fa)


    
