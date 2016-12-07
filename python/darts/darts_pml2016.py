#!/bin/python

import os, sys
from os import path
from pprint import pprint
import subprocess
import urllib2
import time, sys

TEST = R"""

References

   Visible links
   1. http://www.google.co.uk/search?q=hey&um=1&ie=UTF-8&hl=en&tbm=isch&source=og&sa=N&tab=wi
   2. http://maps.google.co.uk/maps?q=hey&um=1&ie=UTF-8&hl=en&sa=N&tab=wl
   3. https://play.google.com/?q=hey&um=1&ie=UTF-8&hl=en&sa=N&tab=w8
   4. http://www.youtube.com/results?q=hey&um=1&ie=UTF-8&gl=GB&sa=N&tab=w1
"""

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

output = ""
#output = TEST
week = sys.argv[1]
start = 0
user_agent = ""
SEARCH = "https://www.google.co.uk/search?q="
#SEARCH = "https://www.bing.com/search?q="

# Run multiple searches to grab all possible links. This also extracts only the unique links.
if not output or output=="":
  for names in ("", "Barneveld", "Wade",
                "Taylor", "Anderson",
                "Thornton", "van Gerwen",
                "Lewis", "Wright"):
    search = SEARCH + "youtube premier league darts 2016 {} week {}".format(names, week)
    got = subprocess_grab(["lynx", "-listonly", "-dump", search])
    output += got
output = [ x for x in output.split("\n") ]
output = [ extract_youtube_http(x) for x in output if extract_youtube_http(x) ]
output = list(set(output))
# pprint(output)
lines = output

def yt_title(yt_link):
  return (yt_link, subprocess_grab(["python", "-m", "youtube_dl", "--get-title", yt_link]))

from joblib import Parallel, delayed
lines = Parallel(n_jobs=8, verbose=10)(delayed(yt_title)(i) for i in lines)
lines = [ x for x in lines if ("2016" in x[1] and str(sys.argv[1]) in x[1]) ]
# pprint(lines)

# Show numbered list of links
for n in range(0,len(lines)):
  yt_link = lines[n][0]
  print("{:3d} - {}\n\t{}".format(n, yt_link, lines[n][1]))

print "Which videos? ",

nums = [int(x.strip("\n")) for x in sys.stdin.readline().split(" ")]
for x in nums:
  os.system('python -m youtube_dl --restrict-filenames --format 18 "{}"'.format(lines[x][0]))

