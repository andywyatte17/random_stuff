#!/usr/bin/env python3

import traceback
from collections import OrderedDict
from pprint import pprint
from clipboard_win_clip_dib import *
from clipboard_win_lib import *
import clipboard_win_example_data as examples
import sys

'''
Experimental code to read bitmap data in Windows clipboard.

Usage:
  py clipboard_win.py [n_example] PNG/CF_DIBV5
'''

# ...

ExampleInstallFns = [x for x in dir(examples) if x.startswith("Install_")]
ExampleInstallFns = OrderedDict([(n, ExampleInstallFns[n]) for n in range(0, len(ExampleInstallFns))])
pprint(ExampleInstallFns)

cf_type = None
if 1:
    n = None
    try:
        n = 0 if len(sys.argv)==1 else int(sys.argv[1])
    except:
        pass
    if n != None:
        name = ExampleInstallFns[n]
        getattr(examples, name)()
        print("\nPerformed install - %s\n" % ExampleInstallFns[n])
        cf_type = name.split("_")[-1]
        if cf_type=="DIBV5":
            cf_type = "CF_DIBV5"

if cf_type==None:
    cf_type = sys.argv[-1]
    if not (cf_type in ("PNG", "CF_DIBV5")):
        print("Must supply a type as the last arg - PNG or CF_DIBV5", file=sys.stderr)
        sys.exit(1)

if cf_type=="PNG":
    png = None
    png = ReadClipData(PNG)
    if png:
        print(png[0:100] + b'...')
        sys.exit(0)
    print("Unable to load PNG data from clipboard.")
    sys.exit(1)

if cf_type=="CF_DIBV5":
    dibv5 = ReadClipData(CF_DIBV5)
    if dibv5:
        # print(repr(dibv5)); sys.exit(0)
        # print(dibv5[:100] + b'...')
        ParseDibv5(dibv5, verbose=True)
