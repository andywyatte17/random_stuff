from tabulate import tabulate
import math
from collections import deque
import sys
from pprint import pprint
PI = math.pi

def to_unsigned(n): return 2*n if n>=0 else -2*n-1
  
def circle_generator():
  for ang in range(0,360,12):
    x = 100 * math.sin(2*PI*ang/360.0)
    y = 75 * math.cos(2*PI*ang/360.0)
    x = int(x)
    y = int(y)
    yield (x,y)

def circle_generator2():
  x0 = 0
  y0 = 0
  for x,y in circle_generator():
    ang = math.atan2(y0-y, x0-x) + PI/2
    yield (x + int(math.cos(ang)*3), y + int(math.sin(ang)*3))
    yield (x - int(math.cos(ang)*3), y - int(math.sin(ang)*3))
    x0 = x
    y0 = 0

def satin_sides_generator():
  def lerp(a,b,x): return int(a*(1-x) + b*x)
  x0,y0,x1,y1 = (1050,1050,1350,1250)
  x2,y2,x3,y3 = (1100,1050,-1200,-1200)
  for m in range(0,11):
    yield (lerp(x0,x1,m * 0.1), lerp(y0,y1,m * 0.1))
    yield (lerp(x2,x3,m * 0.1), lerp(y2,y3,m * 0.1))

def zigzag_generator():
  for x in range(0,300,25):
    yield (x,-50)
    yield (x,50)

def fill_generator():
  x = 0
  y = 0
  dxs = (1,2,3,-2,-4)
  for i in range(0,10):
    for dx in dxs:
      x += 35 + dx
      y += 3
      yield (x,y)
    for dx in dxs:
      x -= 35 + dx
      y += 3
      yield (x,y)

circ_buf = deque(maxlen=5)
circ_buf.append( (0,0) )
circ_buf.append( (0,0) )
circ_buf.append( (0,0) )
circ_buf.append( (0,0) )
circ_buf.append( (0,0) )
      
def pred0():
  return ( 0, 0 )
    
def pred1():
  return ( circ_buf[-1][0],
           circ_buf[-1][1] )

def pred1a():
  return ( circ_buf[-2][0], circ_buf[-2][1] )

def pred1b():
  return ( 2*circ_buf[-2][0] - circ_buf[-4][0],
           2*circ_buf[-2][1] - circ_buf[-4][1] )
  
def pred2():
  return ( 2*circ_buf[-1][0] - circ_buf[-2][0],
           2*circ_buf[-1][1] - circ_buf[-2][1] )

def pred3():
  return ( 3*circ_buf[-1][0] - 3*circ_buf[-2][0] + circ_buf[-3][0],
           3*circ_buf[-1][1] - 3*circ_buf[-2][1] + circ_buf[-3][1])

predictors = [pred0, pred1, pred1a, pred1b, pred2, pred3]

def process(gen, signer):
  s = ['' for i in predictors]
  for _ in range(0,1):
    W = sys.stdout.write
    for x,y in gen():
      c = -1
      for pf in predictors:
        c += 1
        pred = pf()
        delta = (signer(x-pred[0]), signer(y-pred[1]))
        s[c] = s[c] + str(delta[0]) + ',' + str(delta[1]) + ' '
      circ_buf.append( (x,y) )

  c = -1
  for theS in s:
    theS = theS.replace(' 0','z')
    theS = theS.replace(' z','z')
    theS = theS.replace('z ','z')
    c += 1
    yield (len(theS), theS)
    
def namestr(obj, excludes):
  for name in globals().keys():
    if globals()[name]==obj and not name in excludes: return name
  return ''

table = list()
for gen in [
            circle_generator2, circle_generator, zigzag_generator
            ,fill_generator
            ,satin_sides_generator
            ]:
  table.append( list() )
  table[-1].append('{:28s}'.format(namestr(gen, ('gen'))))
  denom = 0
  for lenS, theS in process(gen, to_unsigned):
    # print '\n' + theS + '\n'
    if denom==0: denom = lenS
    table[-1].append('{:6d} {:3d}% '.format(lenS, (lenS*100)/denom))

headers = [namestr(x,('x')) for x in predictors]
print tabulate(table, headers=headers, tablefmt='grid', stralign='right')
 