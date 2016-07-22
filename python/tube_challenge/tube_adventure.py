from data_js import StationData
from pprint import pprint
from sys import stdin
from autocomplete import get_autocomplete_string

class GetStation:
  def __init__(self, stationData):
    self.stationData = stationData
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
    ac = get_autocomplete_string( lambda x : self.autocomplete_fn(x) )
    return self.stationData.LookupStation(ac, True)


def GetHHMM(prompt = "Enter Time (hh:mm - mm *can* be >=60): "):
  for x in range(0,10000):
    import re
    print(prompt if x==0 else "Try again - "+prompt)
    s = stdin.readline()
    match = re.match(r"""([0-9][0-9]*)\:([0-9][0-9])""", s)
    if match:
      hh = int(match.group(1))
      mm = int(match.group(2))
      if hh>=0 and mm>=0 : return (hh,mm)

def WhatNextAutocomplete():
  def autocomplete_fn(x):
    return ["go", "status", "completed", "remaining"]
  return get_autocomplete_string( autocomplete_fn )

def EnterGoLoop(stationList, stationData):
  print("\nGo where?")
  station = getStation.get()
  if stationData

stationData = StationData()
getStation = GetStation(stationData)

#print(stationData.routes)
# print(stationData.AllStations())

print("Start Station:")
stationList = [ getStation.get() ]

print("")
stationList[0] = [ ( stationList[0], GetHHMM() ) ]

while(True):
  print("\nWhat next?")
  command = WhatNextAutocomplete()
  if command=="go":
    stationList = EnterGoLoop(stationList, stationData)


# print(stationData.LookupStation("Edgware Road", True))
