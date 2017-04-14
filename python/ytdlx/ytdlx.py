#!/usr/bin/env python
import sys, re, os
import pdb
import subprocess
import json
from pprint import pprint

TEST = 'http://www.bbc.co.uk/programmes/b08hyhm9'
if len(sys.argv)>1 : TEST = sys.argv[1]
out = subprocess.check_output( \
        [ 'python', '-m', 'youtube_dl', '-j', TEST ] )
out = out.decode('utf-8')
info = json.loads(out)

def tuplize(x):
  return x['format_id'], x['format'], x['tbr'], x['vcodec'], x['acodec'], \
         x['width'], x['height']

def tuplized_ok(x):
  try:
    res = tuplize(x)
    if "=" in res[0]: return None
    return res
  except:
    return None

formats = [tuplized_ok(x) for x in info['formats'] if tuplized_ok(x)!=None]
formats = list(set(formats))
formats = sorted(formats, key = lambda x: ( x[5], x[6], x[2], x[0] ))

# Reduce formats by width/height
wh = list(set( [ (f[5], f[6]) for f in formats ] ) )
wh = sorted(wh)
n = -1
for f in wh:
  n += 1
  print("{:2d}: {:4d}x{:4d}".format(n, wh[n][0], wh[n][1])) 
x = input('what? ')
wh = wh[int(x)]
formats = [f for f in formats if f[5]==wh[0] and f[6]==wh[1]]

# Choose by (reduced) formats
n = -1
for f in formats:
  n += 1
  print("{:2d}: {:4d}x{:4d} {:6d} {:6s} {:6s} {}".format(n, f[5], f[6], f[2], f[3], f[4], f[0])) 
x = input('what? ')
cmd = "python -m youtube_dl -o '%(title)s.%(ext)s' \
      --restrict-filenames -f {} '{}'".format( \
          formats[int(x)][0], TEST)

print(cmd)
fname = os.popen(cmd + ' --get-filename').read()
print(fname)

try:
  import urllib.request as url
  fname = fname.replace('\n', '')
  htm = url.urlopen(sys.argv[1]).read()
  htm = htm.decode('utf-8') 

  from html_filter import *
  htm2 = filter(htm)

  with open(fname+'.htm', 'wb') as f:
    f.write(htm.encode('utf-8'))
except:
  print("Couldn't download htm.")

print(cmd)
os.system(cmd)
