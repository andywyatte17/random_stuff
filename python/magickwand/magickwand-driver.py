from magickwand import *
from ctypes import *

mw = NewMagickWand()
help(MagickGetImagePage)
print(MagickReadImage(mw, "/tmp/IMG_1462.JPG"))
print(MagickGetResolution(mw))
print(MagickGetImageWidth(mw), MagickGetImageHeight(mw))
print(MagickGetImagePage(mw))
