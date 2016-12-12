#!/bin/python
from pyprocessing import *
import pyprocessing
import pickle
from draw_curves_1 import draw_curves as dc1
from draw_curves_2 import draw_curves as dc2
from draw_curves_3 import draw_curves as dc3
from draw_curves_3 import draw_curves_closed as dc3a

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
style = "dc1"
STYLES = ["dc1", "dc2", "dc3", "dc3a"]

try:
    with open("_splines1", "r") as f:
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
            rect(ptf.x, ptf.y, 6, 6)
	else:
            ellipse(ptf.x, ptf.y, 6, 6)
    global ix
    if 0<=ix and ix<len(points):
	ellipse(points[ix][0].x, points[ix][0].y, 12, 12)

def draw():
    global ix, style
    background(255)
    fill(0)
    textSize(11)
    d=0
    if len(points)>0: d = (points[-1][0] - PointF(mouse.x, mouse.y)).magnitude()
    if 1<=ix and ix<len(points): d = (points[ix][0] - points[ix-1][0]).magnitude()  
    text("style (s)={}; q=end; c=clear; p=pop; <SHIFT>+Click = corner; ix (z/x) = {}; d={}".format(style, ix, int(d)), 25, 25)
    fill(250)
    noFill()
    stroke(200, 200, 200)
    ellipse(350, 350, 250, 250)
    draw_points(points)
    if style=="dc1": dc1(points)
    if style=="dc2": dc2(points)
    if style=="dc3": dc3(points)
    if style=="dc3a": dc3a(points)

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
    key_down = key.code

def keyReleased():
    global key_down
    key_down = 0

run()
