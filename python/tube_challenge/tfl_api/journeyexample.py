#!/usr/bin/env python3
 
import requests
import json
from pprint import pprint

try:
    import tfl_api_env
    env = "&app_id=" + tfl_api_env.app_id + "&app_name=" + tfl_api_env.app_name
except:
    env = ""

url = "https://api.tfl.gov.uk/Journey/JourneyResults/940GZZLULBN/to/940GZZLUBST" + \
      "?date=20211113&time=1110&mode=tube" + env

print(url)
result = requests.get(url)
with open('journeyexample.json', 'wb') as f:
    f.write( json.dumps(result.json()).encode('ascii') )

def IsTube(journey):
    try:
        if len(journey["legs"]) == 1:
            return journey["legs"][0]["mode"]["id"]=="tube"
    except:
        pass
    return False

journeys = result.json()["journeys"]
journeys = [ \
    {
        "startDateTime": journey["startDateTime"],
        "duration": journey["duration"]
    } for journey in journeys if IsTube(journey)]

pprint(journeys)
