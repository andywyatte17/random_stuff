import data_js
import data_routes
from pprint import pprint
import Levenshtein

class Printable:
  def __repr__(self):
    from pprint import pformat
    return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=2, width=1)


def FuzzyTextMatch(needle, haystack):
  best = (None, None)
  for test in haystack:
    d = Levenshtein.distance(test, needle)
    #print( (test,needle,d) )
    if not best[1] or d<best[0]:
      best = (d, test)
  return best[1]


class StationData(Printable):

  def __init__(self):
    self.lines = data_js.lines
    self.routes = data_routes.routes
    self.stations = data_js.stations
    self.stationsOnLines = data_js.stationsOnLines
    self.CorrectRoutesEntries()

  def GoRoutes(self, fromStation, toStation):
    results = []
    for route in self.routes.keys():
      stations = self.routes[route]["stations"]
      if fromStation in stations and toStation in stations:
        results.append(route)
    return None if results==[] else results

  def GetStationIDFromName(self, stationName):
    for sid in self.stations.keys():
      if self.stations[sid]==stationName:
        return sid
    return None

  def ExtractJourney(self, fromStation, toStation, route):
    if not route in self.routes.keys():
      return [fromStation, toStation]
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
      if fromIx<toIx:
        return stations[fromIx:toIx+1]
      else:
        return list(reversed(stations[toIx:fromIx+1]))
    return []

  def AllStations(self):
    stations = []
    for identifier in self.stations.keys():
      stations.append(self.stations[identifier])
    return stations

  def LookupStation(self, station, allow_fuzzy):
    if allow_fuzzy:
      stations = self.AllStations()
      return FuzzyTextMatch(station, stations)
    for station_key in self.stations.keys():
      if self.stations[station_key] == station:
        return station
    print("!!! " + station + " !!!")
    return None

  def CorrectRoutesEntries(self):
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
      thisStation = toStation
    return list(set(results)) # unique

  def CalculateRemainsByLine(self, stationList):
    stationsOnLines = self.stationsOnLines
    completed = set(self.CalculateCompleted(stationList))
    for lines in stationsOnLines.keys():
      stationListTmp = stationsOnLines[lines]
      stationListTmp = [ data_js.stations[x] for x in stationListTmp ]
      stationListTmp = [ x for x in stationListTmp if x not in completed ]
      stationsOnLines[lines] = stationListTmp
    return stationsOnLines

  def PrintStatus(self, stationList):
    print("\nStatus:")
    print("Journey time = {}".format(self.CalculateJourneyTime(stationList)))
    remains = self.CalculateRemains(stationList)
    completed = self.CalculateCompleted(stationList)
    print("Completed = {}; Remains = {}".format(len(completed), len(remains)))

  def PrettyPrint3Col(self, items):
    items = items[:]
    while len(items) % 3 != 0:
      items.append(" ")
    split = len(items) / 3
    l1,l2,l3 = items[0:split], items[split:split*2], items[split*2:split*3]
    for _1,_2,_3 in zip(l1,l2,l3):
      print("{0:<24s} {1:<24s} {2:<24s}".format(_1, _2, _3))

  def PrintRemains(self, stationList):
    print("\nRemains:")
    remainsByLine = self.CalculateRemainsByLine(stationList)
    for line in remainsByLine.keys():
      items = [line, "==="] + remainsByLine[line]
      print("")
      self.PrettyPrint3Col(items)

  def PrintCompleted(self, stationList):
    print("\nCompleted:")
    print(self.CalculateCompleted(stationList))

  def PrintRoute(self, stationList):
    print("\nRoute:")
    for station, time, routeName in stationList:
      time_str = "{}:{} => ".format(time[0],time[1]) if time else ""
      print("\t{}{}".format("" if not routeName else (routeName + " => {}".format(time_str)), station))

  def PrintRouteEx(self, stationList):
    last = None
    for station, time, routeName in stationList:
      if last:
        print("{} => {} => {}".format(last, routeName, station))
        print(self.ExtractJourney(last, station, routeName))
      last = station
