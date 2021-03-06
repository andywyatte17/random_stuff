#!/bin/python

import struct
import sys
from threading import Thread
from Queue import Queue
from key_scrubber_config import *
import os
import subprocess

EV_KEY=1
EV_SYN=0
FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)

f = open("/dev/input/" + KBD_DEV, "rb")
q = Queue()
popen = None

def worker():
  while True:
    item = q.get()
    item()
    q.task_done()

t = Thread(target=worker)
t.daemon = True
t.start()

cmd = ""

def bus_fn(bus_stop_code):
  q.put( lambda : os.system("sh bus2 %d" % bus_stop_code) )

def mpc_fn(mpc_command_list):
  for cmd in mpc_command_list:
    q.put( lambda : os.system("mpc " + cmd) )

def process_fn(args):
  def popen_proc(x):
    global popen
    if popen:
      popen.terminate()
      popen = None
    popen = subprocess.Popen(args, shell=True)
  q.put( lambda args=args : popen_proc(args) )

def system_fn(cmd):
  if cmd=="stop": sys.exit(0)
  if cmd=="reboot": os.system("reboot ")
  if cmd=="shutdown": os.system("shutdown -h now")

'''
Handle the code value from FUNCTIONS and perform the
relevant task
'''
def HandleCode(code):
  if code in FUNCTIONS:
    v = FUNCTIONS[code]
    if isinstance(v, bus):
      bus_fn(v.bus_stop_code)
    if isinstance(v, mpc):
      mpc_fn(v.command)
    if isinstance(v, process):
      process_fn(v.command)
    if isinstance(v, system):
      system_fn(v.command_name)

while True:
  key = f.read(EVENT_SIZE)
  sec, usec, type, code, value = struct.unpack(FORMAT, key)
  if type==EV_KEY and value==1:
    pass # DN
  if type==EV_KEY and value==0:
    if code in NUM_KEY_CODES:
      cmd = cmd + NUM_KEY_CODES[code]
    elif code==ENTER_KEY:
      print(cmd)
      HandleCode(cmd)
      cmd = ""
    else:
      print("? Key-code %d" % code)

f.close()
