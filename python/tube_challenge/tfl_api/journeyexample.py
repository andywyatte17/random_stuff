#!/usr/bin/env python3
 
import requests
import json
import sys, os
from pprint import pprint
import dateutil.parser
import datetime


def ConvertName(name):
    HERE = os.path.dirname(os.path.realpath(__file__))
    sys.path.append( os.path.join(HERE, "..") )
    import data.data_js as djs
    return djs.stationsR[name]


def GetJourneyTimes(from_station = "940GZZLULBN", to_station = "940GZZLUBST", \
                    yyyymmdd = "20211113",hhmm = "1110"):
    try:
        from . import tfl_api_env
    except:
        import tfl_api_env
    env = "&app_id=" + tfl_api_env.app_id + "&app_name=" + tfl_api_env.app_name

    url = "https://api.tfl.gov.uk/Journey/JourneyResults/{frm}/to/{to}".format(frm=from_station, to=to_station) + \
          "?date={yyyymmdd}&time={hhmm}&mode=tube".format(yyyymmdd=yyyymmdd, hhmm=hhmm)
    url = url + env

    #print(url)
    result = requests.get(url)
    #with open('journeyexample.json', 'wb') as f:
    #    f.write( json.dumps(result.json()).encode('ascii') )

    def IsTube(journey):
        try:
            if len(journey["legs"]) == 1:
                return journey["legs"][0]["mode"]["id"]=="tube"
        except:
            pass
        return False

    def ExtractDateTime(sdt2):
        return sdt2.year, sdt2.month, sdt2.day, sdt2.hour, sdt2.minute

    try:    journeys = result.json()["journeys"]
    except: return []

    journeys = [ \
        {
            "startDateTime": journey["startDateTime"],
            "duration": journey["duration"],
            "startDateTime2": ExtractDateTime(dateutil.parser.isoparse(journey["startDateTime"]))
        } for journey in journeys if IsTube(journey)]

    def Extract10s(val, tens_right_shift, mod_10s):
        return int(val / 10 ** tens_right_shift) % mod_10s

    yyyymmdd2 = int(yyyymmdd)
    hhmm2 = int(hhmm)

    dtIn = datetime.datetime( \
        year = Extract10s(yyyymmdd2, 4, 10000),
        month = Extract10s(yyyymmdd2, 2, 100),
        day = Extract10s(yyyymmdd2, 0, 100),
        hour = Extract10s(hhmm2, 2, 100),
        minute = Extract10s(hhmm2, 0, 100)
    )

    def DateIsGood(journey):
        sdt2 = journey["startDateTime2"]
        yyyy, mm, dd, hh, MM = sdt2
        jdt = datetime.datetime(year = yyyy, month = mm, day = dd, hour = hh, minute = MM)
        return jdt >= dtIn

    journeys = [x for x in journeys if DateIsGood(x)]

    return journeys


if __name__ == '__main__':
    x = sys.argv[1:]
    x[0] = ConvertName(x[0])
    x[1] = ConvertName(x[1])
    print( json.dumps(GetJourneyTimes(*x), indent = 2) )
    