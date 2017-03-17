#!/bin/python

import get_links
from util import the_urllib2 as urllib2
from util import subprocess_grab
import os, sys
from os import path
from pprint import pprint
import time
import argparse
import datetime as dt
from get_links import get_links
from util import ensure_str

def get_nearest_week(day_of_year = None):
  FIRST_DAY = dt.datetime(2017, 2, 2, 0, 0, 0, 0).timetuple().tm_yday
  if day_of_year==None:
    day_of_year = dt.datetime.now().timetuple().tm_yday
  n = int((day_of_year - FIRST_DAY + 7)/7)
  return 1 if n<1 else n

def extract_youtube_http(x):
  x = urllib2.unquote(x)
  n = x.find("https://www.youtube.com")
  end = x.find("&sa=")
  if n<0: n = x.find("http://www.youtube.com")
  yt_watch = x.find("watch")
  if n < 0 or yt_watch < 0: return None
  return x[n:] if end<0 else x[n:end]

args_ = argparse.ArgumentParser(description='Get Premier League darts videos.')
args_.add_argument('--week', dest='week', action='store_const',
                   const=sum, default=-1,
                   help='Choose week of Premier League to search for. Default = -1, current week')
args_.add_argument('--test', dest='test', action='store_const',
                   const=True, default=False,
                   help='Run unit tests.')
args_.add_argument('--restrict_searches', nargs='?',
                   help='Restrict number of links searched for. Usually for testing only.')
args = args_.parse_args()

if args.test:
  import sys
  from tests import *
  unittest.main(argv=sys.argv[:1], exit=True)

output = ""
#output = TEST
week = args.week
if week<0 : week = get_nearest_week()
start = 0
user_agent = ""

# Run multiple searches to grab all possible links. This also extracts only the unique links.
if not output or output=="":
  for names in ("", "Barneveld", "Wade",
                "Taylor", "Anderson",
                "Thornton", "van Gerwen",
                "Lewis", "Wright",
		"Klaasen", "Huybrechts"):
    got = get_links("youtube premier league darts 2017 {} week {}".format(names, week))
    try: output += got
    except: output += got.decode('utf-8')
output = [ x for x in output.split("\n") ]
output = [ extract_youtube_http(x) for x in output if extract_youtube_http(x) ]
output = list(set(output))
# pprint(output); sys.exit(0);
lines = output

def yt_title(yt_link):
  result = subprocess_grab(["python", "-m", "youtube_dl", "--get-title", yt_link])
  result = ensure_str(result).replace('\n', '')
  return (yt_link, result)

from joblib import Parallel, delayed
lines = [ str(x) for x in lines ]
# pprint(lines); sys.exit(0)

if args.restrict_searches:
  lines = lines[:int(args.restrict_searches)]
lines = Parallel(n_jobs=1, verbose=10)(delayed(yt_title)(i) for i in lines)
# pprint(lines); sys.exit(0);
week_str = str(week)
lines = [ x for x in lines \
           if (u"2017" in ensure_str(x[1]) and \
                week_str in ensure_str(x[1]))
        ]
# pprint(lines); # sys.exit(0);

# Show numbered list of links
for n in range(0,len(lines)):
  yt_link = lines[n][0]
  print("{:3d} - {}\n\t{}".format(n, yt_link, lines[n][1]))

print("Which videos? ")

nums = [int(x.strip("\n")) for x in sys.stdin.readline().split(" ")]
for x in nums:
  os.system('python -m youtube_dl --restrict-filenames --format 18 "{}"'.format(lines[x][0]))
