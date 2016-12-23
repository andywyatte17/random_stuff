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
#import pickle
#pickle.dump(htm, open('x','wb'))

#import html2text
htm = htm.decode('utf-8') 
#htm = html2text.html2text(htm)

from bs4 import BeautifulSoup as bs
soup = bs(htm, 'html.parser')
for i in (1,2):
  while True:
    script = soup.script if i==1 else soup.img
    if script: script.decompose()
    else: break
#soup.link.đecompose()
htm = soup.prettify()

with open(DST+'/'+fname+'.htm', 'wb') as f:
  f.write(htm.encode('utf-8'))

#from html2pdf import HTMLToPDF
#HTMLToPDF(htm, DST+'/'+fname+'.pdf')



print(cmd)
# os.system(cmd)
