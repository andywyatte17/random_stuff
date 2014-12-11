import sys
from random import randint

# python frame_source.py | ffmpeg -r 1 -f rawvideo -pix_fmt rgb24 -s 160x120 -i - -threads 0 -preset fast -y -crf 21 -pix_fmt yuv420p output.mp4
# python frame_source.py | xxd | more

def rand_color(): return (randint(128,255), randint(32,64), randint(32,64))

W,H = (160,120)
for frame in xrange(0,128):
  r,g,b = rand_color()
  for y in xrange(0,H):
    mod3 = ((y/(H/3)) % 3)
    if mod3==0: sys.stdout.write( '{:c}{:c}{:c}'.format(r,g,b) * W )
    if mod3==1: sys.stdout.write( '{:c}{:c}{:c}'.format(b,r,g) * W )
    if mod3==2: sys.stdout.write( '{:c}{:c}{:c}'.format(g,b,r) * W )
