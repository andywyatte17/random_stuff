#!/usr/bin/env python3

'''
Read the given clipboard data type and dump as base-64 to the stdout.

py clipboard_win_read.py <type>

  where type is "CF_DIBV5", "PNG" or an integer.
'''

from clipboard_win_lib import *
import sys

clip_bytes = None

if sys.argv[1]=="CF_DIBV5":
    clip_bytes = ReadClipData(CF_DIBV5)
elif sys.argv[1]=="PNG":
    clip_bytes = ReadClipData(PNG)
else:
    try:
        n = int(sys.argv[1])
        clip_bytes = ReadClipData(PNG)
    except:
      pass

if not clip_bytes:
    print("No bytes found in the clipboard", file = sys.stderr)
    sys.exit(1)

import base64
print(base64.encodebytes(clip_bytes).decode('ascii'))
