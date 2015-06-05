from __future__ import print_function
from pprint import pprint
import sys, bisect, math, random


def round(x): return int(x-0.5) if x<0 else int(x+0.5)


def dda(x1,y1,x2,y2):
  if x1==x2 and y1==y2: return [(x1,y1)]
  dx = x2-x1
  dy = y2-y1
  ax = 1
  ay = 1
  c = 0
  if abs(dy) > abs(dx):
    c = abs(dy) + 1
    ax = float(dx) / c
    ay = 0 if dy==0 else 1 if dy>0 else -1
  else:
    c = abs(dx) + 1
    ax = 0 if dx==0 else 1 if dx>0 else -1
    ay = float(dy) / c
  rv = []
  while c > 0 :
    rv.append( (round(x1), round(y1)) )
    x1 += ax
    y1 += ay
    c -= 1
  return rv


def xy(angle):
  angle = angle * math.pi * 2
  s = math.sin(angle)
  c = math.cos(angle)
  return ( round(s*1000), round(c*1000) )


pixelLine = []
p_last = None
for angle in xrange(0,501):
  p = xy( angle / 500.0 )
  if p_last:
    pixelLine += dda(p_last[0], p_last[1], p[0], p[1])
    pixelLine = pixelLine[:-1]
  p_last = p
# pprint(pixelLine)

pixelLine = sorted(pixelLine)
#pprint(pixelLine)


def dist_fn(a,b): return math.hypot(a[0]-b[0], a[1]-b[1])


def PtNearestLine2(pt, pixelLine):
  best_dist = 2**20
  rv_pt = None
  for ptI in pixelLine:
    dist = dist_fn(ptI, pt)
    if dist < best_dist:
      best_dist = dist
      rv_pt = ptI
  return (best_dist, rv_pt)


def PtNearestLine(pt, pixelLine):

  compares = 0
  def find_lt(a,x):
    i = bisect.bisect_left(a,x)
    if i:
      return i
    else:
      return 0

  best_dist = dist_fn(pt, pixelLine[0])
  start = find_lt(pixelLine, pt)

  # Rightwards
  rv_pt = None
  for i in xrange(start, len(pixelLine)):
    compares += 1
    ptI = pixelLine[i]
    if ptI[0] - pt[0] > best_dist:
      break
    dist = dist_fn(pt, ptI)
    if dist < best_dist:
      #print(i, dist, ptI)
      best_dist = dist
      rv_pt = ptI
  #print(best_dist, rv_pt)

  # Leftwards
  for i in xrange( min(start, len(pixelLine)-1), -1, -1):
    compares += 1
    ptI = pixelLine[i]
    if -(ptI[0] - pt[0]) > best_dist:
      break
    dist = dist_fn(pt, ptI)
    if dist < best_dist:
      #print(i, dist, ptI)
      best_dist = dist
      rv_pt = ptI
  #print(best_dist, rv_pt)

  return (best_dist, rv_pt, compares)


def Randomize( xy_pt, r ):
  return (xy_pt[0] + random.randint(-r,r), xy_pt[1] + random.randint(-r,r))


pprint(len(pixelLine))
r1_count = 0
r2_count = 0
for x,y in [ Randomize(pixelLine[random.randint(0, len(pixelLine)-1)], 100) for x in xrange(0,100) ]:
  pt = (x,y)
  pprint(pt)
  r1, r2 = ( PtNearestLine( pt, pixelLine ), PtNearestLine2( pt, pixelLine ) )
  print( "\t", r1 )
  print( "\t", r2 )
  r2_count += len(pixelLine)
  r1_count += r1[2]

print(100 * (r1_count / float(r2_count)))
