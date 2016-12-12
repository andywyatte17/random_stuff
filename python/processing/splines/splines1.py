#!/bin/python
from pyprocessing import *
import pyprocessing
import pickle

'''
  If you get a c_int problem then edit pyprocessing > flippolicy.py and
  add the line from ctypes import c_int

  See http://stackoverflow.com/questions/14774641/python-fails-to-run-a-pyprocessing-script
'''

from axw_pointf import PointF

'''
  PointF / Bool pair where Bool is True/False = Corner/Non-corner
'''

points = []
ix = -1
try:
    with open("_splines1", "r") as f:
        points = pickle.load(f)
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
            rect(ptf.x, ptf.y, 6, 6)
	else:
            ellipse(ptf.x, ptf.y, 6, 6)
    global ix
    if 0<=ix and ix<len(points):
	ellipse(points[ix][0].x, points[ix][0].y, 12, 12)

def draw_curves(pts):
    if len(pts)<4:
        return

    def InterpPt(p0, p1, p2):
	'''
	  Uses Lagrange interpolating polynomial.
	  p0,p1,p2 = (end-point, end-point-minus-1, end-point-minus-2)
	'''
        def Lgx(n, t4):
            m = 1.0
            for j in range(0,3):
		if n!=j:
	            m *= (t4[3]-t4[j])
		    m /= (t4[n] - t4[j])
            return m
        t = (0.0, 0.4, 0.8, 1.0)
        # ( Lgx(0,t), Lgx(1,t), Lgx(2,t) )
	# sys.exit(0)
	# return (p0 * 0.375) + (p1 * -1.25) + (p2 * 1.875)
	return (p2 * 0.375) + (p1 * -1.25) + (p0 * 1.875)

    def Calc(p0,p1,p2):
        return (p1 + (p2-p0) * 0.2)    # This is value from our code - 0.6 / 3.0 where Tension = 0.6

    for i in range(0, len(pts)-1):
        p0 = pts[i][0]
	p1i = None
	if i==0: p1i = InterpPt(pts[i][0], pts[i+1][0], pts[i+2][0]) 
	p1 = Calc(p1i if p1i else pts[i-1][0], pts[i][0], pts[i+1][0])
	p2i = None
	if i==len(pts)-2: p2i = InterpPt(pts[i+1][0], pts[i][0], pts[i-1][0])
	p2 = Calc(p2i if p2i else pts[i+2][0], pts[i+1][0], pts[i][0])
	p3 = pts[i+1][0]
	for x,y in (p0,p1,p2,p3):
            rect(x, y, 2, 2)
        noFill()
	bezier(p0.x, p0.y, p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)

def draw():
    global ix
    background(255)
    fill(0)
    textSize(11)
    d=0
    if len(points)>0: d = (points[-1][0] - PointF(mouse.x, mouse.y)).magnitude()
    if 1<=ix and ix<len(points): d = (points[ix][0] - points[ix-1][0]).magnitude()  
    text("q=end; c=clear; p=pop; <SHIFT>+Click = corner; ix (z/x) = {}; d={}".format(ix, int(d)), 25, 25)
    fill(250)
    noFill()
    stroke(200, 200, 200)
    ellipse(350, 350, 250, 250)
    draw_points(points)
    draw_curves(points)

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
    global points, key_down, ix
    if key.char=='q':
	try:
            with open('_splines1', 'w') as f:
	        pickle.dump(points, f)
        except: pass
        quit()
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
    key_down = key.code

def keyReleased():
    global key_down
    key_down = 0

run()
