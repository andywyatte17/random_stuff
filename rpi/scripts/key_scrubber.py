#!/bin/python
import struct
import sys

EV_KEY=1
EV_SYN=0
FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)

f = open("/dev/input/event0", "rb")

while True:
  key = f.read(EVENT_SIZE)
  sec, usec, type, code, value = struct.unpack(FORMAT, key)
  if type==EV_KEY and value==1:
    pass # DN
  if type==EV_KEY and value==0:
    if 2<=code and code<=11:
      print("Key-code %d" % code)
    else:
      print("? Key-code %d" % code)

f.close()
