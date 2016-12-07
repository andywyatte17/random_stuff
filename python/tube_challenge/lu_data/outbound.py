from data_js import exports
import sys
import urllib
import json
from pprint import pprint

url = R"https://api.tfl.gov.uk/Line/{line}/Timetable/{from_id}"
app_url = R"?direction=outbound&app_id={app_id}&app_key={app_key}"

def LookupStation(station_id):
  for k in exports.stations.keys():
    v = exports.stations[k]
    if v.lower()==station_id:
      return k
  raise KeyError

from_id = LookupStation(sys.argv[2])

url = url.format(line=sys.argv[1], from_id=from_id)
url = url + app_url.format(app_id=sys.argv[3], app_key=sys.argv[4])
# print(url)

f = urllib.urlopen(url)
js = json.loads( f.read() )

print(json.dumps(js, indent=2, sort_keys=False))

