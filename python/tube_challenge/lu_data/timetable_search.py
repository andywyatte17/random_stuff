import sys
import urllib
import json
from pprint import pprint
import os

'''
Read TFL data about the timetable on an underground line from- and to- two stations.
'''

sys.path.append( os.path.join(os.path.dirname(os.path.realpath(__file__)), "..") )

url = R"https://api.tfl.gov.uk/Line/{line}/Timetable/{from_id}/to/{to_id}?app_id={app_id}&app_key={app_key}"
import data.data_js as data_js


def LookupStation(station_id):
  for k in data_js.stations.keys():
    v = data_js.stations[k]
    if v.lower()==station_id.lower():
      return k
  raise KeyError


def EnvOrKey(envKey, getter):
  if envKey in os.environ : return os.environ[envKey]
  return getter()


from_id = LookupStation(sys.argv[2])
to_id = LookupStation(sys.argv[3])

url = url.format(line=sys.argv[1], from_id=from_id, to_id=to_id, \
                 app_id=EnvOrKey('TFL_APP_ID', lambda : sys.argv[4]), \
                 app_key=EnvOrKey('TFL_APP_KEY', lambda : sys.argv[5]))

f = urllib.urlopen(url)
js = json.loads( f.read() )

print(json.dumps(js, indent=2, sort_keys=False))

