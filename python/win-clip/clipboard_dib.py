#!/usr/bin/env python3

import struct
from collections import OrderedDict
from pprint import pprint

def Extract_BITMAPV5HEADER(some_bytes):
    u32 = lambda off,size : struct.unpack_from("<I", some_bytes[off:off+size])[0]
    i32 = lambda off,size : struct.unpack_from("<i", some_bytes[off:off+size])[0]
    u16 = lambda off,size : struct.unpack_from("<H", some_bytes[off:off+size])[0]
    BI_X = {0: ("BI_RGB", 0), 0x0001: ("BI_RLE8", 0x0001), 0x0002: ("BI_RLE4", 0x0002), 0x0003: ("BI_BITFIELDS", 0x0003),
            0x0004: ("BI_JPEG", 0x0004), 0x0005: ("BI_PNG", 0x0005), 0x000B: ("BI_CMYK", 0x000B),
            0x000C: ("BI_CMYKRLE8", 0x000C), 0x000D: ("BI_CMYKRLE4", 0x000D)}
    bv5h = OrderedDict(
      ( \
        ( 'bV5Size_u32', u32(0, 4) ),
        ( 'bV5Width_i32', i32(4, 4) ),
        ( 'bV5Height_i32', i32(8, 4) ),
        ( 'bV5Planes_u16', u16(12, 2) ),
        ( 'bV5BitCount_u16', u16(14, 2) ),
        ( 'bV5Compression_u32', BI_X[u32(16, 4)] ),
        ( 'bV5SizeImage_u32', u32(20, 4) ),
        ( 'bV5XPelsPerMeter_i32', i32(24, 4) ),
        ( 'bV5YPelsPerMeter_i32', i32(28, 4) ),
        ( 'bV5ClrUsed_u32', u32(32, 4) ),
        ( 'bV5ClrImportant_u32', u32(36, 4) ),
        ( 'bV5RedMask_u32', (u32(40, 4), hex(u32(40, 4))) ),
        ( 'bV5GreenMask_u32', (u32(44, 4), hex(u32(44, 4))) ),
        ( 'bV5BlueMask_u32', (u32(48, 4), hex(u32(48, 4))) ),
        ( 'bV5AlphaMask_u32', (u32(52, 4), hex(u32(52, 4))) ),
        ( 'bV5CSType_u32', some_bytes[56:60] ),
        ( 'bV5Endpoints_36bytes', some_bytes[60:96] ),
        ( 'bV5GammaRed_u32', u32(96, 4) ),
        ( 'bV5GammaGreen_u32', u32(100, 4) ),
        ( 'bV5GammaBlue_u32', u32(104, 4) ),
        ( 'bV5Intent_u32', u32(108, 4) ),
        ( 'bV5ProfileData_u32', u32(112, 4) ),
        ( 'bV5ProfileSize_u32', u32(116, 4) ),
        ( 'bV5Reserved_u32', u32(120, 4) ),
      )
    )

    return bv5h, some_bytes[124:]

# ...

def parse_dibv5(dibv5_bytes, verbose = False):
    bv5h, after_header = Extract_BITMAPV5HEADER(dibv5_bytes)

    pprint(bv5h); print()

    compression, width, height = bv5h['bV5Compression_u32'], bv5h['bV5Width_i32'], bv5h['bV5Height_i32']
    bitcount = bv5h['bV5BitCount_u16']
    stride = ((width * bitcount + 31) // 32) * 4

    off = 0
    if compression [0] == 'BI_BITFIELDS':
        off += 12

    remains = len(after_header) - off
    im_size = width * stride
    if remains != im_size:
        print("Bad image input size!")
        return
    if not (bitcount==24 or bitcount==32):
        print("bitcount must be 24 or 32")
        return

    if bitcount==32 and compression[0]=='BI_RGB':
        mask_rgba = (bv5h["bV5RedMask_u32"], bv5h["bV5GreenMask_u32"], 
                     bv5h["bV5BlueMask_u32"], bv5h["bV5AlphaMask_u32"])
        mask_rgba = [x[0] for x in mask_rgba]
        if mask_rgba != [0xff0000, 0xff00, 0xff, 0xff000000 ]:
            print('BI_RGB, bits=32 => RGBA mask is incorrect')
            return

    if bitcount==32 and compression[0]=='BI_BITFIELDS':
        mask_rgba = (bv5h["bV5RedMask_u32"], bv5h["bV5GreenMask_u32"], 
                     bv5h["bV5BlueMask_u32"], bv5h["bV5AlphaMask_u32"])
        mask_rgba = [x[0] for x in mask_rgba]
        if mask_rgba != [0xff0000, 0xff00, 0xff, 0xff000000 ] and \
           mask_rgba != [0xff0000, 0xff00, 0xff, 0x0 ]:
            print('BI_BITFIELDS, bits=32 => RGBA mask is incorrect - ' + str(mask_rgba))
            return

    Alpha_Unmultiply = None
    if bitcount==24:
        xadd, row_fmt, hdr = (3, "BBB", "BGR ")
    if bitcount==32:
        xadd, row_fmt, hdr = (4, "BBBB", "BGRA")
        def f(bgra):
            b,g,r,a = [x/255.0 for x in bgra]
            if a>0.0001:
                r /= a
                g /= a
                b /= a
            return (int(x * 255.999) for x in (b,g,r,a))
        Alpha_Unmultiply = f

    for yo in range(0, abs(height)):
        y = yo
        if height > 0 :
            y = height - 1 - yo
        for x in range(0, width):
            row = after_header[off + (stride * y) + (xadd * x):]
            if x==0 and verbose: print("%4d  %s " % (yo, hdr), end='')
            values = struct.unpack_from(row_fmt, row)
            if Alpha_Unmultiply:
                values = Alpha_Unmultiply(values)
            values = "(" + ", ".join(["{:3d}".format(x) for x in values]) + ")"
            if verbose: print("{} ".format(values), end='')
        if verbose: print()
