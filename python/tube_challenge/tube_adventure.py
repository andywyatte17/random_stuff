from data_js import StationData
from pprint import pprint
from sys import stdin

stationData = StationData()
#print(stationData.routes)

print(stationData.AllStations())

#print("Start?")
#station = stdin.readline()
print(stationData.LookupStation("Edgware Road", True))
