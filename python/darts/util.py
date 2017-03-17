#!/bin/python

import subprocess

def subprocess_grab(args):
  return subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0]

the_urllib2 = None
try:
  import urllib2
except:
  import urllib.request as urllib2

the_urllib2 = urllib2
