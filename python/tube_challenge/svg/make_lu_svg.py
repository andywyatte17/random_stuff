from underground_gps import *
import data_routes
import sys, os
from pprint import pprint


class AxB:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  def __call__(self, x):
    return self.a * x + self.b


def svgize(x): return x.replace("&", "&amp;")


def GetStationGps(station, the_gps):
  for stn, lati, longi in the_gps:
    if stn==station:
      return lati, longi
  return None, None
if __name__=='__main__':
  sew = sys.stderr.write

  magnets = ( \
              ('Oxford Circus', -0.1), \
            )
  magnets = [ (GetStationGps(stn, gps), m) for stn, m in magnets ]
  magnets = [ (float(lati_longi[0]), float(lati_longi[1]), m) for lati_longi, m in magnets ]
  sew( "\n{}\n".format(magnets) )

  def magnetize(lati, longi, some_magnets, stn):
    for mlat, mlon, mstrength in some_magnets:
      dlat, dlon = mlat-lati, mlon-longi
      k = 0.1
      mdist = ((mstrength * k**2) / (hypot(dlat, dlon) + k)**2)
      # sew( "{} {}\n".format(stn, mdist) )
      lati += dlat*mdist
      longi += dlon*mdist
    return lati, longi

  gps = [ x for x in gps ]
  for steps in range(0, 10):
    for i in range(0, len(gps)):
      stn, lati, longi = gps[i]
      lati, longi = magnetize(float(lati), float(longi), magnets, stn)
      gps[i] = (stn, str(lati), str(longi) )

  '''
  Make svg data for the gps data (ie stations and positions).
  '''
  min_lati = float( min(gps, key = lambda x : float(x[1]))[1] )
  max_lati = float( max(gps, key = lambda x : float(x[1]))[1] )
  min_long = float( min(gps, key = lambda x : float(x[2]))[2] )
  max_long = float( max(gps, key = lambda x : float(x[2]))[2] )
  sew( "\n{},{},{},{}\n\n".format(min_lati, max_lati, min_long, max_long) )

  long_fn = AxB( a = 3500.0 / (max_long-min_long),
                 b = 50 + (3500.0 * -min_long) / (max_long-min_long) )
  lati_fn = AxB( a = 2000.0 / (min_lati-max_lati),
                 b = 50 + (2000.0 * -max_lati) / (min_lati-max_lati) )

  def adjust(cx,cy):
    '''
    import math
    rx, ry = 1900, 1100
    dist = math.hypot(cx-rx,cy-ry)
    dist2 = dist ** 0.6
    dist2 *= 15
    cx = rx + (cx-rx) * dist2 / dist
    cy = ry + (cy-ry) * dist2 / dist
    cx *= 1.35
    cy *= 1.2
    cx -= 750
    cy -= 340'''
    return (cx,cy)

  s = '<svg width="3600" height="2100">\n<g>\n';
  s += '<rect x="0" y="0" width="3600" height="2100" style="fill:#ddd"/>\n'

  colors = ( "rgba(128,32,32,25)", "rgba(32,128,32,25)", "rgba(32,32,128,25)" )
  for stn, lati, longi in gps:
    import random
    stn = svgize(stn)
    lati, longi = float(lati), float(longi)
    cx = long_fn(longi)
    cy = lati_fn(lati)
    cx, cy = adjust(cx, cy)
    s += '<ellipse cx="{}" cy="{}" rx="{}" ry="{}" style="fill:#ffa"/>'''.format( \
      cx,cy,4,4 )
    s += '<text x="{}" y="{}" style="font-size: 16px; fill:{}">{}</text>\n' \
      .format(cx-20, cy, colors[random.randint(0,len(colors)-1)], stn)

  for route in data_routes.routes.keys():
    line = []
    stations = data_routes.routes[route]["stations"]
    points = ""
    for station in stations:
      # sys.stderr.write(station + "\n")
      lati, longi = GetStationGps(station, gps)
      lati, longi = float(lati), float(longi)
      cx, cy = long_fn(longi), lati_fn(lati)
      cx, cy = adjust(cx, cy)
      points += "{},{} ".format(cx, cy)
    s += '<polyline points="{}" style="fill:none; stroke:#004; stroke-opacity:0.2; stroke-width:3px"/>\n'.format(points)
  s += '</g>\n</svg>\n'
  print(s)

