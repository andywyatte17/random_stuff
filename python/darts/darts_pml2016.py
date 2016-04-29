#!/bin/python

import os, sys
from os import path
from pprint import pprint
import subprocess

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
  n = x.find("http")
  yt = x.find("youtube.")
  yt_watch = x.find("watch?")
  if n < 0 or yt < 0 or yt_watch < 0: return None
  return x[n:]

output = ""
#output = TEST
week = sys.argv[1]
start = 0
user_agent = ""
#SEARCH = "https://www.google.co.uk/search?q="
SEARCH = "https://www.bing.com/search?q="

# Run multiple searches to grab all possible links. This also extracts only the unique links.
if not output or output=="":
  for names in ("", "Barneveld", "Wade",
                "Taylor", "Anderson",
                "Thornton", "van Gerwen",
                "Lewis", "Wright"):
    search = SEARCH + "youtube premier league darts 2016 {} week {}".format(names, week)
    got = subprocess_grab(["lynx", "-listonly", "-dump", search])
    output += got
output = [ extract_youtube_http(x) for x in output.split("\n") if extract_youtube_http(x) ]
lines = list(set(output))

def yt_title(yt_link):
  return subprocess_grab(["python", "-m", "youtube_dl", "--get-title", yt_link])

lines = [ (x, yt_title(x)) for x in lines ]
lines = [ x for x in lines if ("2016" in x[1] and str(sys.argv[1]) in x[1]) ] 
pprint(lines)
sys.exit(0)

# Show numbered list of links
for n in range(0,len(lines)):
  yt_link = lines[n][0]
  print("{:3d} - {}\n\t{}".format(n, yt_link, lines[n][1]))

print "Which videos? ",

nums = [int(x.strip("\n")) for x in sys.stdin.readline().split(" ")]
for x in nums:
  os.system('python -m youtube_dl --format 18 "{}"'.format(lines[x][0]))

