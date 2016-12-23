#!/bin/python

from pyprocessing import *

def draw_curves(pts):
    '''
    This code draws curves in the Premier+ style (wrt end calculation) except that
    the end vectors are set to zero.
    '''
    if len(pts)<4:
        return

    def Calc(p0,p1,p2):
        return (p1 + (p2-p0) * 0.2)    # This is value from our code - 0.6 / 3.0 where Tension = 0.6

    for i in range(0, len(pts)-1):
        p0 = pts[i][0]
	p1 = pts[i][0] if i==0 else Calc(pts[i-1][0], pts[i][0], pts[i+1][0])
	p2 = pts[i+1][0] if i==len(pts)-2 else Calc(pts[i+2][0], pts[i+1][0], pts[i][0])
	p3 = pts[i+1][0]
	for x,y in (p0,p1,p2,p3):
            rect(x, y, 2, 2)
        noFill()
	bezier(p0.x, p0.y, p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)

