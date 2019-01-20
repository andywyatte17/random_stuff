#!/usr/bin/env python2

'''
Usage:
  python capture.py /dev/video0 video-prefix frequency_in_seconds
'''

from __future__ import print_function
import os, sys
import time
import sched
import subprocess

if len(sys.argv)!=4:
  print(__doc__, file=sys.stderr)
  sys.exit(0)

CMD = r"""avconv -f video4linux2 -s 640x480 -i {dev}
         -ss 0:0:2 -frames 1 {name}"""
CMD = "".join(CMD.split("\n"))

BASE_NAME = "/tmp/" + sys.argv[2] + "_" + str(int(time.time())) + "_"

WAIT_IN_SECONDS = int(sys.argv[3])

def take_photo(time_now, n):
  time_now = int(time_now)
  cmd = CMD.format(dev=sys.argv[1], name=BASE_NAME + str(n) + ".jpg")
  subprocess.check_output(cmd, shell=True)

try:
  next_time = time.time()
  n = 0
  while True:
    now = time.time()
    if now > next_time:
      next_time = time.time() + WAIT_IN_SECONDS
      n += 1
      take_photo(now, n)
    else:
      time.sleep(0.5)
except KeyboardInterrupt:
  print("\nMaking video...")
  name = os.path.basename(BASE_NAME)
  cmd = "avconv -r 10 -i {}%d.jpg -b:v 1000k {}.mp4" \
            .format(BASE_NAME, name)
  with open("last_video.sh", "w") as f:
    f.write(cmd)
  os.system(cmd)
