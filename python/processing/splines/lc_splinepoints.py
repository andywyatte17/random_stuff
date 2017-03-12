#!/bin/python
from pyprocessing import *
import pyprocessing
import pickle

from axw_pointf import PointF

'''
  PointF / Bool pair where Bool is True/False = Corner/Curve
'''

points = []
ix = -1
		
try:
    with open("_lc_splines", "r") as f:
        points, style = pickle.load(f)
except:
    pass

def setup():
    size(600, 600)
    frameRate(225)

def draw_points(points):
    noFill()
    stroke(0, 0, 0)
    for ptf,corner in points:
        if corner:
            rect(ptf.x-3.5, ptf.y-3.5, 7, 7)
	else:
            ellipse(ptf.x, ptf.y, 6, 6)
    global ix
    if 0<=ix and ix<len(points):
	ellipse(points[ix][0].x, points[ix][0].y, 12, 12)

def quadratic(pts3):
    CP1 = pts3[0] + (pts3[1]-pts3[0]) * 0.66
    CP2 = pts3[2] + (pts3[1]-pts3[2]) * 0.66
    bezier(pts3[0].x, pts3[0].y,
           CP1.x, CP1.y,
           CP2.x, CP2.y,
           pts3[2].x, pts3[2].y)

def draw():
    global ix, style
    background(255)
    fill(0)
    textSize(11)
    d=0
    if len(points)>0: d = (points[-1][0] - PointF(mouse.x, mouse.y)).magnitude()
    if 1<=ix and ix<len(points): d = (points[ix][0] - points[ix-1][0]).magnitude()  
    text("r=rot-ix; style (s)={}; q=end; c=clear; p=pop".format("???"), 10, 20)
    text("<SHIFT>+Click = cornerix (z/x) = {}; d={}".format(ix, int(d)), 10, 40)
    fill(250)
    noFill()
    stroke(200, 200, 200)
    ellipse(350, 350, 250, 250)
    draw_points(points)

    spl_pts = lc_splinepoints(False, # closed \
                              points)
    #print(len(spl_pts))
    noFill()
    stroke(0, 0, 0)
    i, flip = 0, 0
    while i+2<len(spl_pts):
      flip = (flip+1) % 2
      stroke(255,0,0) if flip else stroke(0,0,255)
      for pt in spl_pts[i:i+3]:
        ellipse(pt.x, pt.y, 9, 9)
      i += 2
    i, flip = 0, 0
    while i+2<len(spl_pts):
      flip = (flip+1) % 2
      stroke(255,0,0) if flip else stroke(0,0,255)
      quadratic(spl_pts[i:i+3])
      i += 2

key_down = 0

def mouseDragged():
    global ix
    if ix!=-1 and ix<len(points):
        points[ix] = (PointF(mouse.x, mouse.y), key_down==SHIFT)

def mousePressed():
    global key_down, ix
    if ix==-1:
        points.append( (PointF(mouse.x,mouse.y), key_down==SHIFT) )

def keyPressed():
    # SHIFT constant!
    global points, key_down, ix, style, STYLES
    if key.char=='q':
	try:
            with open('_splines1', 'w') as f:
	        pickle.dump( (points, style), f)
        except: pass
        quit()
    if key.char=='s':
	if not style in STYLES:
            style = STYLES[0]
        else:
	    index = STYLES.index(style)
	    if index>=0 : style = STYLES[(index+1)%len(STYLES)]
    if key.char=='z':
	ix-=1
	if ix<-1:
	    ix = len(points)-1
    if key.char=='x':
	ix+=1
	if ix>=len(points):
	    ix = -1
    if key.char=='c':
	points = []
    if key.char=='p':
	if len(points)>0: points = points[:-1]
    if key.char=='r':
	if len(points)>0: points = points[1:] + points[:1]
    key_down = key.code

def keyReleased():
    global key_down
    key_down = 0

def lc_splinepoints(closed, points):
    results = []
    n = len(points)
    if n<2 : return results
    vControl, vEnd = None, None
    if closed:
        # ...
        result(results)
    else:
        # ...
        results.append(points[0][0])
        vEnd = points[1][0]
        if n < 3:
            vControl = vEnd
            # lineTo vControl
            return results
        vControl = vEnd;
        vEnd = points[2][0]
        if n < 4:
            vStart = vControl
            vControl = vEnd
            # quadTo vStart, vControl
            for v in (vStart, vControl): results.append( v )
            return results

        vEnd = (points[1][0] + points[2][0])/2.0;
        vStart = vControl
        vControl = vEnd
        # quadTo vStart, vControl
        for v in (vStart, vControl): results.append( v )

        for i in range(2, n-2):
            vControl = points[i][0]
            vEnd = (points[i][0] + points[i+1][0])/2.0;
            vStart = vControl
            vControl = vEnd
            # quadTo: vStart, vControl
            for v in (vStart, vControl): results.append( v )

        vControl = points[n - 2][0]
        vEnd = points[n - 1][0]
        vStart = vControl
        vControl = vEnd
        # quadTo: vStart, vControl
        for v in (vStart, vControl): results.append( v )
        return results

run()
