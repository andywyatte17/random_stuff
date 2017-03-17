#!/bin/python

import subprocess
import sys

def ensure_str(s):
  if type(s)==bytes:
    return s.decode('utf-8')
  if type(s)!=str:
    raise TypeError("String-like thing is of unhandled type - " + str(s) + " - " + str(type(s)))
  return s

def subprocess_grab(args):
  result = subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0]
  result = ensure_str(result)
  return result

the_urllib2 = None
try:
  import urllib2
except:
  import urllib.request as urllib2

the_urllib2 = urllib2
