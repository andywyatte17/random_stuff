#!/bin/python

import os, sys
from os import path
from pprint import pprint
import subprocess
try:
  import urllib2
except:
  import urllib.request as urllib2
import time
import argparse
import datetime as dt

TEST = R"""

References

   Visible links
   1. http://www.google.co.uk/search?q=hey&um=1&ie=UTF-8&hl=en&tbm=isch&source=og&sa=N&tab=wi
   2. http://maps.google.co.uk/maps?q=hey&um=1&ie=UTF-8&hl=en&sa=N&tab=wl
   3. https://play.google.com/?q=hey&um=1&ie=UTF-8&hl=en&sa=N&tab=w8
   4. http://www.youtube.com/results?q=hey&um=1&ie=UTF-8&gl=GB&sa=N&tab=w1
"""

def get_nearest_week(day_of_year = None):
  FIRST_DAY = dt.datetime(2017, 2, 2, 0, 0, 0, 0).timetuple().tm_yday
  if day_of_year==None:
    day_of_year = dt.datetime.now().timetuple().tm_yday
  n = (day_of_year - FIRST_DAY + 7)/7
  return 1 if n<1 else n

def subprocess_grab(args):
  return subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0]

def extract_youtube_http(x):
  x = urllib2.unquote(x)
  n = x.find("https://www.youtube.com")
  end = x.find("&sa=")
  if n<0: n = x.find("http://www.youtube.com")
  yt_watch = x.find("watch")
  if n < 0 or yt_watch < 0: return None
  return x[n:] if end<0 else x[n:end]

# ...

import unittest

class Test(unittest.TestCase):
  def setUp(self):
    pass
    
  def test_get_nearest_week(self):
    yd = lambda y_m_d : dt.datetime(y_m_d[0], y_m_d[1], y_m_d[2], 0, 0, 0, 0).timetuple().tm_yday
    w = get_nearest_week( yd((2017,2,2)) )
    self.assertEqual(w,1)
    w = get_nearest_week( yd((2017,2,2+6)) )
    self.assertEqual(w,1)
    w = get_nearest_week( yd((2017,2,2+7)) )
    self.assertEqual(w,2)
    w = get_nearest_week( yd((2016,1,1)) )
    self.assertEqual(w,1)

# ...

args_ = argparse.ArgumentParser(description='Get Premier League darts videos.')
args_.add_argument('--week', dest='week', action='store_const',
                   const=sum, default=-1,
                   help='Choose week of Premier League to search for. Default = -1, current week')
args_.add_argument('--test', dest='test', action='store_const',
                   const=True, default=False,
                   help='Run unit tests.')
args = args_.parse_args()

if args.test:
  import sys
  unittest.main(argv=sys.argv[:1], exit=True)

output = ""
#output = TEST
week = args.week
if week<0 : week = get_nearest_week()
start = 0
user_agent = ""
SEARCH = "https://www.google.co.uk/search?q="
#SEARCH = "https://www.bing.com/search?q="

# Run multiple searches to grab all possible links. This also extracts only the unique links.
if not output or output=="":
  for names in ("", "Barneveld", "Wade",
                "Taylor", "Anderson",
                "Thornton", "van Gerwen",
                "Lewis", "Wright",
		"Klaasen", "Huybrechts"):
    search = SEARCH + "youtube premier league darts 2017 {} week {}".format(names, week)
    got = subprocess_grab(["lynx", "-listonly", "-dump", search])
    try: output += got
    except: output += got.decode('utf-8')
output = [ x for x in output.split("\n") ]
output = [ extract_youtube_http(x) for x in output if extract_youtube_http(x) ]
output = list(set(output))
# pprint(output)
lines = output

def yt_title(yt_link):
  return (yt_link, subprocess_grab(["python", "-m", "youtube_dl", "--get-title", yt_link]))

from joblib import Parallel, delayed
lines = [ str(x) for x in lines ]
print(lines)
sys.exit(0)
lines = lines[:1]
lines = Parallel(n_jobs=8, verbose=10)(delayed(yt_title)(i) for i in lines)
lines = [ str(x) for x in lines \
           if (u"2017" in str(x[1]) and \
	       str(week) in str(x[1]))
        ]
# pprint(lines)

# Show numbered list of links
for n in range(0,len(lines)):
  yt_link = lines[n][0]
  print("{:3d} - {}\n\t{}".format(n, yt_link, lines[n][1]))

print("Which videos? ")

nums = [int(x.strip("\n")) for x in sys.stdin.readline().split(" ")]
for x in nums:
  os.system('python -m youtube_dl --restrict-filenames --format 18 "{}"'.format(lines[x][0]))
