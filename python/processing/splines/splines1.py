#!/bin/python
from pyprocessing import *

'''
  If you get a c_int problem then edit pyprocessing > flippolicy.py and
  add the line from ctypes import c_int

  See http://stackoverflow.com/questions/14774641/python-fails-to-run-a-pyprocessing-script
'''

from axw_pointf import PointF
points = []

def setup():
    size(600, 600)
    frameRate(225)

def draw():
    background(255)
    for ptf in points:
        ellipse(ptf.x-2, ptf.y-2, 4, 4)

def mousePressed():
    points.append( PointF(mouse.x,mouse.y) )

def keyPressed():
    quit()

run()
