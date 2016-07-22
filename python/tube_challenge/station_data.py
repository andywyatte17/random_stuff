from data_js import _Exports, _exports
import Levenshtein


def FuzzyTextMatch(needle, haystack):
  best = (None, None)
  for test in haystack:
    d = Levenshtein.distance(test, needle)
    #print( (test,needle,d) )
    if not best[1] or d<best[0]:
      best = (d, test)
  return best[1]


class StationData(_Exports):

  def __init__(self):
    self.lines = _exports.lines
    self.routes = _exports.routes
    self.stations = _exports.stations
    self.stationsOnLines = _exports.stationsOnLines
    self.CorrectStations()

  def GoRoutes(self, fromStation, toStation):
    results = []
    for route in self.routes.keys():
      stations = self.routes[route]["stations"]
      if fromStation in stations and toStation in stations:
        results.append(route)
    return None if results==[] else results

  def ExtractJourney(self, fromStation, toStation, route):
    stations = self.routes[route]["stations"]
    fromIx = -1
    toIx = -1
    for i, j in enumerate(stations):
      if j == fromStation:
        fromIx = i
        break
    for i, j in enumerate(stations):
      if j == toStation:
        toIx = i
        break
    if fromIx>=0 and toIx>=0:
      if fromIx<toIx: return stations[fromIx:toIx]
      else: return list(reversed(stations[toIx:fromIx]))
    return []

  def AllStations(self):
    stations = []
    for route in self.routes.keys():
      for station in self.routes[route]["stations"]:
        stations.append(station)
    return list(set(stations)) # unique

  def LookupStation(self, station, allow_fuzzy):
    if allow_fuzzy:
      stations = self.AllStations()
      return FuzzyTextMatch(station, stations)
    for station_key in self.stations.keys():
      if self.stations[station_key] == station:
        return station
    print("!!! " + station + " !!!")
    return None

  def CorrectStations(self):
    for route in self.routes.keys():
      stations = self.routes[route]["stations"]
      stations = stations.replace("\n",";")
      stations = stations.split(";")
      stations_old = stations
      stations = []
      for x in stations_old:
        stations.append( self.LookupStation(x, False) )
      self.routes[route]["stations"] = stations

  def CalculateJourneyTime(self, stationList):
    return "TO:DO"

  def CalculateRemains(self, stationList):
    allStations = self.AllStations()
    completed = self.CalculateCompleted(stationList)
    return list(set(allStations).difference(set(completed)))

  def CalculateCompleted(self, stationList):
    thisStation = stationList[0][0]
    results = [ thisStation ]
    if len(stationList)==1: return results
    for (toStation, time, route) in stationList[1:]:
      routeStations = self.ExtractJourney(thisStation, toStation, route)
      results += routeStations
    return list(set(results)) # unique

  def PrintStatus(self, stationList):
    print("\nStatus:")
    print("Journey time = {}".format(self.CalculateJourneyTime(stationList)))
    remains = self.CalculateRemains(stationList)
    completed = self.CalculateCompleted(stationList)
    print("Completed = {}; Remains = {}".format(len(completed), len(remains)))

  def PrintRemains(self, stationList):
    print("\nRemains:")
    print(self.CalculateRemains(stationList))

  def PrintCompleted(self, stationList):
    print("\nCompleted:")
    print(self.CalculateCompleted(stationList))

  def PrintRoute(self, stationList):
    print("\nRoute:")
    for station, t, by in stationList:
      print("\t{}{}".format("" if not by else (by + " => "), station))

