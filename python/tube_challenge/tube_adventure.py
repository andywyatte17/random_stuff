from data_js import StationData
from pprint import pprint
from sys import stdin
from autocomplete import get_autocomplete_string

class GetStation:
  def __init__(self, stationData):
    self.stations = [(x,x.lower()) for x in stationData.AllStations()]

  def autocomplete_fn(self, test):
    if len(test)<3:
      return None
    test = test.lower()
    result = []
    for x in self.stations:
      if x[1].startswith(test):
        result.append(x[0])
    return result

  def get(self):
    return get_autocomplete_string( lambda x : self.autocomplete_fn(x) )


stationData = StationData()
getStation = GetStation(stationData)

#print(stationData.routes)
# print(stationData.AllStations())

print("Start?")
print(getStation.get())

# print(stationData.LookupStation("Edgware Road", True))
