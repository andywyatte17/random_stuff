import underground_gps
import sys
from data.data_routes import routes
from pprint import pprint

'''
This script tries to extract a list of nearby stations that are either on different underground
lines or different branches of the same underground line.
'''

def RoutesForStations(station):
  result = []
  for route in routes.keys():
    if station in routes[route]["stations"]:
      result.append(route)
  return result

stations = []
for station, _, _ in underground_gps.gps:
  stations.append( (station, set(RoutesForStations(station))) )
#pprint(stations)

stations_dist = []
for x in range(0, len(stations)):
  for y in range(x+1, len(stations)):
    from_, fromRoutes = stations[x]
    to_, toRoutes = stations[y]
    intersection = fromRoutes.intersection(toRoutes)
    if len(intersection) == 0:
      # pprint( (from_, to_, intersection, len(intersection)) )
      stations_dist.append( ( from_, to_, underground_gps.distance_lu(from_, to_) ) )

stations_dist = sorted( stations_dist, key = lambda x : x[2] )
stations_dist = [ x for x in stations_dist if x[2]<=2000 ]
pprint( stations_dist )

