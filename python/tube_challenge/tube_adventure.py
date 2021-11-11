#!/usr/bin/env python3

'''
tube_adventure.py - a text-based tube challenge adventure!

Usage:
  py(thon(3)) tube_adventure.py
    or
  py tube_adventure.py --resume - continue from last dated log
    or
  py tube_adventure.py --debug - debug a route attempt in my_routes.py

'''
from station_data import StationData
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
    result = list(set(result)) # remove duplicates
    return result

  def get(self):
    ac = get_autocomplete_string( lambda x : self.autocomplete_fn(x) )
    return self.stationData.LookupStation(ac, True)


def GetHHMM(prompt = "Enter Time (hh:mm - mm *can* be >=60): "):
  for x in range(0,10000):
    import re
    print(prompt if x==0 else "Try again - "+prompt)
    s = stdin.readline()
    if s.lower().strip()=='undo':
      return 'undo'
    match = re.match(r"""([0-9][0-9]*)\:([0-9][0-9])""", s)
    if match:
      hh = int(match.group(1))
      mm = int(match.group(2))
      if hh>=0 and mm>=0 : return (hh,mm)


def DumpToFile(stationList):
  global FN
  try:
    _ = FN[:]
  except:
    import time, os
    HERE = os.path.dirname(os.path.realpath(__file__))
    FN = os.path.join(HERE, "tube_adventure-{}.txt".format(int(time.time())))
  import os
  with open(FN, "w") as file:
    for st, time, method in stationList:
      if method == "other":
        print("other => {} => {}".format("{.02d}:{.02d}".format(time[0], time[1]), st), file=file)
      elif method == '' or method == None:
        print(st, file=file)
      else:
        print("{} => {}".format(method, st), file=file)


def WhatNextAutocomplete():
  def autocomplete_fn(x):
    return ["go", "status", "completed", "remaining", "route", "undo", "routeEx"]
  return get_autocomplete_string( autocomplete_fn )


def EnterGoLoop(stationList, stationData):
  print("\nGo where?")
  while True:
    station = getStation.get()
    go_routes = stationData.GoRoutes(stationList[-1][0], station)
    go_routes = ["other"] if not go_routes else go_routes + ["other"]
    if go_routes==None:
      print("\nCan't go there... go where?")
    else:
      break
  if len(go_routes)==1:
    go_routes = go_routes[0]
  else:
     print("\nGo how?")
     go_routes = get_autocomplete_string( lambda x : go_routes )
  hh_mm = 0
  if go_routes == "other":
    hh_mm = GetHHMM("""\tThere is no direct route to the station.
\tType 'undo' if this was a mistake or Enter Time (hh:mm) for 'other':""")
  if hh_mm != 'undo':
    stationList = stationList[:]
    stationList.append((station, hh_mm, go_routes))
  return stationList

stationData = StationData()
getStation = GetStation(stationData)

#print(stationData.routes)
# print(stationData.AllStations())

stationList = None


def Resume(stationList):
  import time, os, glob, re, sys
  rx = re.compile(r'tube_adventure-([0-9]*)\.txt')
  HERE = os.path.dirname(os.path.realpath(__file__))
  fn_time = []
  for x in glob.glob(os.path.join(HERE, "tube_adventure-*.txt")):
    match = rx.search(x)
    if match!=None:
      fn_time.append( (x, int(match.group(1)) ) )
  if len(fn_time)<=0:
    return False
  fn_time = sorted(fn_time, reverse=True, key=lambda x: x[1])
  path_to_use = fn_time[0][0]
  rx2 = re.compile("(.*)=>(.*)")
  rx3 = re.compile("(.*)=>(.*)=>(.*)")
  with open(path_to_use, "r") as f:
    for line in f:
      line = line.strip()
      if line=='':
        continue
      found = rx3.match(line)
      if found!=None:
        route, time_str, station = found.group(1).strip(), found.group(2).strip(), found.group(3).strip()
        print(route.encode('ascii'), time_str.encode('ascii'), station.encode('ascii'))
        continue

      found = rx2.match(line)
      if found!=None:
        route, station = found.group(1).strip(), found.group(2).strip()
        print(route.encode('ascii'), station.encode('ascii'))
        continue

      print(line.strip().encode('ascii'))
  return stationList


def InteractiveLoop(resume = True):
  global stationList

  if not resume:
    print("Start Station:")
    stationList = [getStation.get()]
    print("")
    stationList[0] = (stationList[0], GetHHMM(), None)

  while True:
    print("\nWhat next?")
    command = WhatNextAutocomplete()
    if command == "go":
      stationList = EnterGoLoop(stationList, stationData)
      DumpToFile(stationList)
    elif command == "undo":
      if len(stationList)>1:
        stationList = stationList[0:-1]
    elif command == "route":
      stationData.PrintRoute(stationList)
    elif command == "routeEx":
      stationData.PrintRouteEx(stationList)
    elif command == "status":
      stationData.PrintStatus(stationList)
    elif command == "remaining":
      stationData.PrintRemains(stationList)
    elif command == "completed":
      stationData.PrintCompleted(stationList)

      # print(stationData.LookupStation("Edgware Road", True))


def Debug():
  stationList = [ ("High Barnet", (0,0), None), ("Morden", 0, "northern_bank") ]
  #stationData.PrintRoute(stationList)
  #stationData.PrintStatus(stationList)
  #stationData.PrintCompleted(stationList)
  stationData.PrintRemains(stationList)


def MyAttempt():
  import my_routes
  route = my_routes.route1
  route = route.replace(" => ", ";")
  route = route.replace("\t", ";")
  route = route.replace("\n", ";")
  route = route.replace(";;", ";")
  route = route.replace(";;", ";")
  route = route.replace(";;", ";")
  route = route.split(";")
  print(route)
  i = 0
  stationList = []
  while i < len(route):
    if i==0 :
      stationList.append( (route[i], 0, None) )
      i += 1
    else:
      if route[i]=="other":
        stationList.append( (route[i+2], route[i+1], route[i]) )
        i += 3
      else:
        stationList.append( (route[i + 1], 0, route[i]) )
        i += 2
  #stationData.PrintRoute(stationList)
  #stationData.PrintCompleted(stationList)
  # stationData.PrintRouteEx(stationList)
  stationData.PrintRemains(stationList)
  stationData.PrintStatus(stationList)


def Welcome():
  print("""
Tube Challenge - a text-based adventure!

You will be asked a Start Station.

Then you will be asked to perform a series of actions via 'What next?'.
The most common command is 'go' - which invites you to input a next station.

For every station you 'go' to you will also be asked which line/method to take
to get to that line. A special method is 'other' which indicates some
other means of transport such as walking or bus - type in a time in
the format hh:mm for this value.

Tab-key completion is supported - partially type in a station and use tab
to complete the name, including tabbing again to scroll through a list of
several matching stations. Use Tab on the 'What next?' command to see the
full list of actions other than 'go'.
""")


if __name__=='__main__':
  import sys
  if not sys.stdout.isatty() or (len(sys.argv)>=2 and sys.argv[1]=="--debug"):
    # Debug()
    MyAttempt()
  else:
    try:
      if (True or (1 in sys.argv and sys.argv[1]=='--resume')):
        stationList = Resume(stationList)
      if stationList != None:
        InteractiveLoop(resume = True)
      else:
        Welcome()
        InteractiveLoop(resume = False)
    except:
      print(stationList)
      stationData.PrintRoute(stationList)
      raise