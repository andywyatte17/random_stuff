#!/usr/bin/env python3

import ctypes
import ctypes.wintypes as w
import traceback

CF_TEXT, CF_DIBV5, CF_UNICODETEXT = 1, 17, 13

kernel32 = ctypes.windll.kernel32
kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
kernel32.GlobalLock.restype = ctypes.c_void_p
kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
GlobalSize = kernel32.GlobalSize
GlobalSize.argtypes = w.HGLOBAL,
GlobalSize.restype = w.ctypes.c_size_t
user32 = ctypes.windll.user32
user32.GetClipboardData.restype = ctypes.c_void_p

RegisterClipboardFormatA = user32.RegisterClipboardFormatA
RegisterClipboardFormatA.argtypes = [w.LPCSTR]
RegisterClipboardFormatA.restype = ctypes.c_uint32

PNG = RegisterClipboardFormatA("PNG".encode("utf-8"))
print(PNG)

def get_cf_bits_from_clip(fmt):
    user32.OpenClipboard(0)
    try:
        if user32.IsClipboardFormatAvailable(fmt):
            data = user32.GetClipboardData(fmt)
            size = GlobalSize(data)
            #print(size)
            raw_data = ctypes.create_string_buffer(size)
            data_locked = kernel32.GlobalLock(data)
            ctypes.memmove(raw_data, data_locked, size)
            kernel32.GlobalUnlock(data_locked)
            return raw_data.raw
    except:
        traceback.print_exc()
    finally:
        user32.CloseClipboard()
    return None

try:
    print("PNG?")
    print(get_cf_bits_from_clip(PNG)[0:100])
except:
    pass

try:
    print("CF_DIBV5?")
    print(get_cf_bits_from_clip(CF_DIBV5)[0:100])
except:
    pass

try:
    print("CF_UNICODETEXT")
    print(get_cf_bits_from_clip(CF_UNICODETEXT).decode("utf-16"))
except:
    pass

# bump