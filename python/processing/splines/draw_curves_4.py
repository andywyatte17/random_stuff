#!/bin/python

from pyprocessing import *
from collections import namedtuple

CurveSection = namedtuple('CurveSection', ['p0','p1','p2','p3','type'])

def Unmask(n):
    rv, m, mt = ("", 1, 8)
    while mt:
        rv += "x" if n&mt else "o"
        m *= 2
	mt /= 2
    return rv

# for i in range(16): print(Unmask(i))

def CalculateMask(pts_corners):
    rv, m = 0, 1
    for _,corner in pts_corners:
        if corner!=0: rv += m
	m *= 2
    return rv

# MASKS - the type of curve based on the CalculateMask(..) value
MASKS = (  "curve",     # 0 = oooo
           "curve",     # 1 = xooo
           "curve-xb",  # 2 = oxoo
           "curve-xb",  # 3 = xxoo
           "curve-xe",  # 4 = ooxo
           "straight",  # 5 = xoxo
           "straight",  # 6 = oxxo
           "straight",  # 7 = xxxo
           "curve",     # 8 = ooox
           "curve",     # 9 = xoox
           "straight",  # 10 = oxox
           "straight",  # 11 = xxox
           "curve-xe",  # 12 = ooxx
           "straight",  # 13 = xoxx
           "straight",  # 14 = oxxx 
           "straight" ) # 15 = xxxx



def draw_curves_section(pts):
    def Calc(p0,p1,p2):
        return (p1 + (p2-p0) * 0.2)    # This is value from our code - 0.6 / 3.0 where Tension = 0.6
    cm = CalculateMask(pts)
    curve_type = MASKS[cm]
    i = 1
    if curve_type=="straight":
	return CurveSection(p0=pts[i][0], p1 = pts[i+1][0], p2 = None, p3 = None, type = curve_type)
    p0 = pts[i][0]
    p1 = pts[i][0] if curve_type=="curve-xb" \
		   else Calc(pts[i-1][0], pts[i][0], pts[i+1][0])
    p2 = pts[i+1][0] if curve_type=="curve-xe" \
		     else Calc(pts[i+2][0], pts[i+1][0], pts[i][0])
    p3 = pts[i+1][0]
    return CurveSection(p0=p0, p1=p1, p2=p2, p3=p3, type=curve_type)

def draw_curves_closed(pts):
    '''
    Draw curves allowing the next (ie wrap-around) point to be considered in the
    vector calculation, and closing the curve section between first and last point..
    '''
    if len(pts)<2: return
    if len(pts)>1 and (pts[0][0]-pts[-1][0]).magnitude()<3.0:
	return draw_curves_closed_2(pts)

    some_points = lambda x : [ pts[ (len(pts) + x) % len(pts)] ]
    pts_tmp = some_points(-2) + some_points(-1) + pts + some_points(0) + some_points(1)
    last = len(pts_tmp)-4
    for i in range(1, last+1):
        cs = draw_curves_section( pts_tmp[i:i+4] )
        noFill()
        stroke(255,0,0) if i==1 else stroke(0,255,0) if i==last else stroke(0,0,0)
	if cs.type=="straight":
            line(cs.p0.x, cs.p0.y, cs.p1.x, cs.p1.y)
	    continue
	for x,y in (cs.p1, cs.p2):
            rect(x-1.5, y-1.5, 3, 3)
        bezier(cs.p0.x, cs.p0.y, cs.p1.x, cs.p1.y, cs.p2.x, cs.p2.y, cs.p3.x, cs.p3.y)
        # Use Cubic Hermite splines instead...
        # curve(pts[i-1][0].x, pts[i-1][0].y, p0.x, p0.y, p3.x, p3.y, pts[i+2][0].x, pts[i+2][0].y)

def draw_curves_closed_2(pts):
    '''
    Draw curves allowing the next (ie wrap-around) point to be considered in the
    vector calculation, but not losing the curve section between first and last point.
    '''
    some_points = lambda x : [ pts[ (len(pts) + x) % len(pts)] ]
    pts_tmp = some_points(-2) + pts + some_points(1)
    last = len(pts_tmp)-4
    for i in range(0, last+1):
        cs = draw_curves_section( pts_tmp[i:i+4] )
        noFill()
        stroke(255,0,0) if i==0 else stroke(0,255,0) if i==last else stroke(0,0,0)
	if cs.type=="straight":
            line(cs.p0.x, cs.p0.y, cs.p1.x, cs.p1.y)
	    continue
	for x,y in (cs.p1, cs.p2):
            rect(x-1.5, y-1.5, 3, 3)
        bezier(cs.p0.x, cs.p0.y, cs.p1.x, cs.p1.y, cs.p2.x, cs.p2.y, cs.p3.x, cs.p3.y)
        # Use Cubic Hermite splines instead...
        # curve(pts[i-1][0].x, pts[i-1][0].y, p0.x, p0.y, p3.x, p3.y, pts[i+2][0].x, pts[i+2][0].y)

