#!/bin/python

from pyprocessing import *

def draw_curves_impl(pts, which):
    if len(pts)<4:
        return

    def Calc(p0,p1,p2):
        return (p1 + (p2-p0) * 0.2)    # This is value from our code - 0.6 / 3.0 where Tension = 0.6

    wrap = lambda x : len(pts)-1 if x<0 else 0 if x>=len(pts) else x  
    if not which: which = range(0, len(pts)-1)
    for i in which:
        p0 = pts[i][0]
	p1 = Calc(pts[wrap(i-1)][0], pts[i][0], pts[i+1][0])
	p2 = Calc(pts[wrap(i+2)][0], pts[i+1][0], pts[i][0])
	p3 = pts[i+1][0]
        noFill()
	stroke(255,0,0) if i==0 else stroke(0,255,0) if i==len(pts)-2 else stroke(0,0,0)
        for x,y in (p0,p1,p2,p3):
            rect(x, y, 2, 2)
	bezier(p0.x, p0.y, p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)

def draw_curves(pts):
    '''
    Draw curves allowing the next (ie wrap-around) point to be considered in the end
    vector calculation.
    '''
    draw_curves_impl(pts, None)

def draw_curves_closed(pts):
    '''
    Draw curves allowing the next (ie wrap-around) point to be considered in the
    vector calculation, and closing the curve section between first and last point..
    '''
    some_points = lambda x : [ pts[ (len(pts) + x) % len(pts)] ]
    pts_tmp = some_points(-1) + pts + some_points(0) + some_points(1)
    draw_curves_impl( pts_tmp, range(1, len(pts_tmp)-2) )

def draw_curves_closed_2(pts):
    '''
    Draw curves as if the two end-points were equal. This is similar to draw_curves_closed
    except we use some different points..
    '''
    some_points = lambda x : [ pts[ (len(pts) + x) % len(pts)] ]
    pts_tmp = some_points(-2) + pts + some_points(1)
    draw_curves_impl( pts_tmp, range(1, len(pts_tmp)-2) )

