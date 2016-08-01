'''
underground_gps.py
  This is a tuple of tuples - ( station_name, gps-latitude, gps-longitude ).
'''

from underground_gps_data import *
from math import acos, asin, cos, sin, atan2, hypot


def latlon2tileXY(lat, lon, zoom):
  import math
  tileX = (int)(math.floor((lon + 180.0) / 360.0 * math.pow(2.0, zoom)));
  tileY = (int)(math.floor((1.0 - math.log( math.tan(lat * math.pi/180.0) + 1.0 / math.cos(lat * math.pi/180.0)) / math.pi) / 2.0 * math.pow(2.0, zoom)));
  return (tileX, tileY)


def latlon2OpenStreetmapTileUrl(lat, lon, zoom):
  if isinstance(lat, str): lat = float(lat)
  if isinstance(lon, str): lon = float(lon)
  tx, ty = latlon2tileXY(lat, lon, zoom)
  return "http://a.tile.openstreetmap.org/{}/{}/{}.png".format(zoom, tx, ty)


def distance(lati_long1, lati_long2):
  def ToRadians(degreeThings):
    return ( (x*3.141592654)/180.0 for x in degreeThings )
  t1, l1 = ToRadians( lati_long1 )
  t2, l2 = ToRadians( lati_long2 )
  R = 6371 * 1000.0 # metres
  # t = lati, l = long
  dt = (t2-t1)
  dl = (l2-l1)
  a = sin(dt/2)**2 + ( cos(t1) * cos(t2) * sin(dl/2)**2 )
  c = 2 * atan2(a**0.5, (1-a)**0.5);
  return R * c


def distance_lu(fromStation, toStation):
  def find(station):
    for x,lati,longi in gps:
      if x==station : return lati, longi
    return (None, None)
  la1,lo1 = find(fromStation)
  la2,lo2 = find(toStation)
  if not lo1 or not lo2 : return None
  return distance( (float(la1),float(lo1)), (float(la2),float(lo2)) )

