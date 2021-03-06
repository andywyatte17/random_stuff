#!/bin/python
from datetime import date
import datetime
try: import urllib2 as url
except: pass
try: import urllib.request as url
except: pass
import pickle
import sys
from bleb import CHANNELS
import bleb

# print(CHANNELS)
TODAY = date.today()

cache = {}
try:
  import gzip
  with gzip.open('_tvlistings.gz', 'rb') as f:
    cache = pickle.load(f)
except: pass

def store():
  try:
    with gzip.open('_tvlistings.gz', 'wb') as f:
      pickle.dump(cache, f)
  except: pass

def xml_prettify(xmlStr):
  import xml.dom.minidom
  xmlStr = xml.dom.minidom.parseString(xmlStr)
  return xmlStr.toprettyxml()

MAX_DAYS = 7

print("Reading...")
u = None
for day_off in range(0, MAX_DAYS):
  print("Day {} of {}".format(day_off+1, MAX_DAYS))
  for ch in CHANNELS:
    try:
      u = bleb.url(channel = ch, day_off = day_off)
      #print(u)
      cache_ch = (ch, day_off + TODAY.toordinal())
      xml = None
      if cache_ch in cache:
        xml = cache[cache_ch]
      else:
        response = url.urlopen(u)
        xml = response.read()
        cache[cache_ch] = xml
        # print(xml)
    except:
      store()
      print("Problem in url: {}".format(u) )
store()

for day_off in range(0, MAX_DAYS):
  this_day = date.fromordinal( TODAY.toordinal() + day_off )
  print("{} {}".format(this_day, this_day.strftime("%A")))
  for ch in CHANNELS:
    cache_ch = (ch, day_off + TODAY.toordinal())
    xml = cache[cache_ch]
    for x in bleb.find(channel = ch, xml = xml, find_type = "Film"):
      print(x)

