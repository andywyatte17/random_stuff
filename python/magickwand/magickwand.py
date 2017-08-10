from ctypes import *

MW = CDLL("libMagickWand.so.5")

MW.NewMagickWand.argtypes = None
MW.NewMagickWand.restype = c_void_p
def NewMagickWand():
  return MW.NewMagickWand()

MW.MagickReadImage.argtypes = [c_void_p, c_char_p]
MW.MagickReadImage.restype = c_bool
def MagickReadImage(mw, path):
  return not not MW.MagickReadImage(mw, path)

MW.MagickGetResolution.argtypes = [c_void_p, POINTER(c_double), POINTER(c_double)]
MW.MagickGetResolution.restype = c_bool
def MagickGetResolution(mw):
  x, y = (c_double(0.0), c_double(0.0))
  return None if not MW.MagickGetResolution(mw, byref(x), byref(y)) \
         else (x.value, y.value)

MW.MagickGetImageWidth.argtypes = [c_void_p]
MW.MagickGetImageWidth.restype = c_int
def MagickGetImageWidth(mw):
  return MW.MagickGetImageWidth(mw)

MW.MagickGetImageHeight.argtypes = [c_void_p]
MW.MagickGetImageHeight.restype = c_int
def MagickGetImageHeight(mw):
  return MW.MagickGetImageHeight(mw)

MW.MagickGetImagePage.argtypes = [c_void_p, POINTER(c_uint32), POINTER(c_uint32), 
                                  POINTER(c_uint32), POINTER(c_uint32)]
MW.MagickGetImagePage.restype = c_bool
def MagickGetImagePage(mw):
  '''Get image page. Returns (w,h,x,y) or None if failed.'''
  w,h,x,y = c_uint32(0), c_uint32(0), c_uint32(0), c_uint32(0)
  if not MW.MagickGetImagePage(mw, byref(w), byref(h), byref(x), byref(y)):
    return None
  return (w.value, h.value, x.value, y.value)

