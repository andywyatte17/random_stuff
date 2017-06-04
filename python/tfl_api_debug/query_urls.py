#!/usr/bin/env python

StopPoints = "https://api.tfl.gov.uk/Line/piccadilly/stoppoints"""

Arrivals = "https://api.tfl.gov.uk/line/victoria/arrivals"

appId, appKey = None, None

def AddAppId(url):
  import pickle
  global appId, appKey  
  try:
    if not appId:
      appId, appKey = pickle.load( open("app.p", "rb") )
  except:
      print("appId? ")
      appId = raw_input()
      print("appKey? ")
      appKey = raw_input()
      pickle.dump( (appId, appKey), open("app.p", "wb") )
  if url.find('?')>=0:
    url = url + "&appId={}&appKey={}".format(appId, appKey)
  else:
    url = url + "?appId={}&appKey={}".format(appId, appKey)
  return url

def Timetable(naptanFrom="940GZZLUMPK", naptanTo="940GZZLUAMS", line="metropolitan"):
  return "https://api.tfl.gov.uk/Line/{}/Timetable/{}/to/{}" \
         .format(line, naptanFrom, naptanTo)

def JourneyResults(naptanFrom="940GZZLUMPK", naptanTo="940GZZLUAMS", line="metropolitan"):
  return "https://api.tfl.gov.uk/Journey/JourneyResults" + \
         "/{}/to/{}".format(naptanFrom, naptanTo)

def JourneyResultsEx(naptanFrom="940GZZLUMPK", naptanTo="940GZZLUAMS", \
                     fromName="Moor Park", toName="Amersham", \
                     yyyyMMdd="20170608", departTime_hhmm="0830" \
                     ):
  import urllib
  q = urllib.quote
  url = "https://api.tfl.gov.uk/Journey/JourneyResults/{naptanFrom}/to/{to}" \
         + "?date={yyyyMMdd}&time={time}&timeIs=Departing&mode=tube&" \
         + "fromName={fromName}&toName={toName}"
  return url.format(naptanFrom=q(naptanFrom), to=q(naptanTo), yyyyMMdd=q(yyyyMMdd), \
                    fromName=q(fromName), toName=q(toName), time=q(departTime_hhmm))

StopPoints2 = "https://api.tfl.gov.uk/StopPoint/940GZZLUEUS/Arrivals?mode=tube&line=northern"

def ArrivalsByVehicle(line, vehicleId):
  return "https://api.tfl.gov.uk/{}/victoria/arrivals?vehicleId={}" \
         .format(line, vehicleId)
 
