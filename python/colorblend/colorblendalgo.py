from colorsys import *

def full_mask():
    while True: yield (255,255,255,255)

def _01_to_255(x): return int(x*255.99)

def color_blend(rgbas, rgb, mask_rgbas):
    rgbas_out = []
    sh,ss,sv = rgb_to_hsv(rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0)
    for rgba, m_rgba in zip(rgbas, mask_rgbas if mask_rgbas else full_mask()):
        h,s,v = rgb_to_hsv(rgba[0]/255.0, rgba[1]/255.0, rgba[2]/255.0)
        h = sh
        s = ss
        r,g,b = hsv_to_rgb(h, s, v)
        rgbas_out.append((_01_to_255(r),
                          _01_to_255(g),
                          _01_to_255(b), rgba[3]))
        
    return rgbas_out

if __name__=='__main__':
    r = color_blend( [(255,128,0,255), (128,64,32,64)],
                     (192,160,130),
                     None )
    print(r)
