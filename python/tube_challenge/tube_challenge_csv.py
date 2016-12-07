#!/bin/python

'''
Take a csv file in the format (below) and give a dump of the timings.

station_start
station_next,by_route (includes other),other_timing
...
'''

import importlib
import data.data_js as data_js
import data.data_routes as data_routes
from tabulate import tabulate

from StringIO import StringIO
from pprint import pprint
import sys

the_attempt = None
sio = None
if len(sys.argv)>1:
  if sys.argv[1]=='-1':
    the_attempt = importlib.import_module('my_routes.attempt1')
  elif sys.argv[1]=='-2':
    the_attempt = importlib.import_module('my_routes.attempt2')
  elif sys.argv[1]=='-3':
    the_attempt = importlib.import_module('my_routes.attempt3')
  elif sys.argv[1]=='-4':
    the_attempt = importlib.import_module('my_routes.attempt4')
  else:
    sio = open(sys.argv[1], 'r')
else:
  the_attempt = importlib.import_module('my_routes.attempt1')

if the_attempt != None:
  sio = StringIO(the_attempt.attempt)

RouteTups = []
for line in sio:
  line = line.replace('\n', '')
  if line=="": continue
  RouteTups.append( tuple(line.split(",")) )
#pprint(RouteTups)


def ParseTime(hh_mm):
  ix = hh_mm.find(":")
  return int(hh_mm[:ix])*60 + int(hh_mm[ix+1:])


def TimeBetween(last, to, by):
  for route in data_routes.routes.keys():
    stations = data_routes.routes[route]["stations"]
    timings = data_routes.routes[route]["timings"]
    if last in stations and to in stations and (by==None or route==by):
      if by==None: sys.stderr.write( "{} => {} => ? {}\n".format(last, to, route) )
      lix = stations.index(last)
      tix = stations.index(to)
      dt = abs(timings[tix] - timings[lix])
      return (dt, by, set(stations[min(lix,tix) : max(lix,tix)+1]))
  if by==None:
    raise RuntimeError("Unknown {} => {}".format(last, to))
  return TimeBetween(last, to, None)


def GetAllStations():
  all_stations = set()
  for route in data_routes.routes.keys():
    for station in data_routes.routes[route]["stations"]:
      all_stations.add(station)
  return all_stations


def SetN(a_set, n):
  nv = n
  rv = []
  for sv in a_set:
    rv.append(sv)
    nv -= 1
    if nv<0: break
  return rv


all_stations = GetAllStations()
ALL_STATIONS = all_stations.copy()
#pprint(all_stations)
last = None
raw_time = 0
total_time_3 = 0
total_time_4 = 0
result = [ ("#", "at", "total_journey_time", "left", "done", "sum@3", "sum@4") ]
nCount = 1
for x in RouteTups:
  to = x[0]
  by = None
  if last!=None:
    actual_by = by
    by = x[1]
    if by=="other":
      other_time = x[2]
      rt = ParseTime(other_time)
      raw_time += rt
      total_time_3 += rt + 3
      total_time_4 += rt + 4
    else:
      rt, actual_by, visited = TimeBetween(last, to, by)
      old_all_stations = all_stations.copy()
      for v in visited:
        all_stations.discard(v)
      raw_time += rt
      total_time_3 += rt + 3
      total_time_4 += rt + 4

  def TFmt(mm): return "{:02d}:{:02d}".format(mm/60, mm%60)

  #if not last: print(to)
  #elif by=="other": print("{},{},{}".format(to, actual_by, other_time))
  #else: print("{},{}".format(to, actual_by))
  result.append( (nCount, to, TFmt(raw_time), \
                  len(ALL_STATIONS) - len(all_stations), len(all_stations), \
                  TFmt(total_time_3), TFmt(total_time_4)) )
  last = x[0]
  nCount += 1

print(tabulate(result))
if len(all_stations)>0:
  pprint( SetN(all_stations, 10000) )
