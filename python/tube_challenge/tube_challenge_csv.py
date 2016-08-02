#!/bin/python

'''
Take a csv file in the format (below) and give a dump of the timings.

station_start
station_next,by_route (includes other),other_timing
...
'''

import data.data_js as data_js
import data.data_routes as data_routes
import my_routes.attempt2 as the_attempt
from tabulate import tabulate

attempt = the_attempt.attempt

from StringIO import StringIO
from pprint import pprint
import sys

sio = None
if len(sys.argv)>1:
  sio = open(sys.argv[1], 'r')
else:
  sio = StringIO(attempt)

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
    raise IndexError
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
result = [ ("at", "total_journey_time", "left", "done") ]
for x in RouteTups:
  to = x[0]
  by = None
  if last!=None:
    actual_by = by
    by = x[1]
    if by=="other":
      other_time = x[2]
      raw_time += ParseTime(other_time)
    else:
      rt, actual_by, visited = TimeBetween(last, to, by)
      old_all_stations = all_stations.copy()
      for v in visited:
        all_stations.discard(v)
      raw_time += rt
  #if not last: print(to)
  #elif by=="other": print("{},{},{}".format(to, actual_by, other_time))
  #else: print("{},{}".format(to, actual_by))
  result.append( (to, "{:02d}:{:02d}".format(raw_time/60, raw_time%60), \
                  len(ALL_STATIONS) - len(all_stations), len(all_stations)) )
  last = x[0]

print(tabulate(result))
if len(all_stations)>0:
  pprint( SetN(all_stations, 10000) )
