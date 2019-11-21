#!/usr/bin/env python3

import traceback
from collections import OrderedDict
from pprint import pprint
from clipboard_dib import *
from clipboard_examples import *
import sys

# ...

# ...

def get_cf_bits_from_clip(fmt):
    ClipFns().OpenClipboard(0)
    try:
        if ClipFns().IsClipboardFormatAvailable(fmt):
            data = ClipFns().GetClipboardData(fmt)
            size = ClipFns().GlobalSize(data)
            raw_data = ctypes.create_string_buffer(size)
            data_locked = ClipFns().GlobalLock(data)
            ctypes.memmove(raw_data, data_locked, size)
            ClipFns().GlobalUnlock(data_locked)
            return raw_data.raw
    finally:
        ClipFns().CloseClipboard()
    return None

# ...

# InstallGimpPng16x16()
InstallGimp_DIBV5_16x16()
# InstallPaintNET_DIBV5_16x16()
# InstallChrome_DIBV5_16x16()

print("PNG (%d)" % PNG)
png = None
png = get_cf_bits_from_clip(PNG)
if png:
    # print(repr(png))
    # print(png[0:100] + b'...')
    pass

print("\n\n")

print("CF_DIBV5")
dibv5 = None
dibv5 = get_cf_bits_from_clip(CF_DIBV5)
if dibv5:
    # print(repr(dibv5)); sys.exit(0)
    # print(dibv5[:100] + b'...')
    parse_dibv5(dibv5, verbose=True)
    pass

#try:
#    print("CF_UNICODETEXT")
#    print(get_cf_bits_from_clip(CF_UNICODETEXT).decode("utf-16"))
#except:
#    pass

# bump
