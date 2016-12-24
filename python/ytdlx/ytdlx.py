#!/usr/bin/env python
import sys, re, os
import subprocess
TEST = 'http://www.bbc.co.uk/programmes/b0185cks'
if 1 in sys.argv : TEST = sys.argv[1]
TEST = sys.argv[1]
out = subprocess.check_output( \
        [ 'python', '-m', 'youtube_dl', \
          '--list-formats', TEST ] )
out = out.decode('utf-8')
out = out.split('\n')
n = -1
formats = []
rgx2 = None
for f in out:
  if n<0:
    s = re.search( '(format code *)(extension *)(.*)', f)
    if s:
      rgx2 = '(.{})(.{})(.*)'.format('{'+str(len(s.group(1)))+'}',
                                     '{'+str(len(s.group(2)))+'}')
      print(f)
      n = 0
    continue
  s = re.search(rgx2, f)
  if s:
    g = [ s.group(n) for n in (1,2,3) ]
    print( '{}\t{}{}\n\t{}'.format(
        n, g[0], g[1], g[2] ) )
    formats.append(g[0])
    n+=1

formats = [x.strip() for x in formats]

DST = r'/mnt/sdcard/Music'
x = input('what? ')
cmd = "python -m youtube_dl -o '%(title)s.%(ext)s' \
--restrict-filenames -f {} '{}' \
--exec 'mv {{}} {}' ".format(
        formats[int(x)], TEST, DST)

fname = os.popen(cmd + ' --get-filename').read()
print(fname)

import urllib.request as url
fname = fname.replace('\n', '')
htm = url.urlopen(sys.argv[1]).read()

htm = htm.decode('utf-8') 

from html_filter import *
htm2 = filter(htm)

with open(DST+'/'+fname+'.htm', 'wb') as f:
  f.write(htm2.encode('utf-8'))
with open(fname+'.htm', 'wb') as f:
  f.write(htm.encode('utf-8'))

print(cmd)
os.system(cmd)
