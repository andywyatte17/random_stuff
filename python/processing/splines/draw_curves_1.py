#!/bin/python

from pyprocessing import *

def draw_curves(pts):
    '''
    This code draws the curves in Premier+ style - end vectors are calculated
    using an interpolated extra curve point..
    '''
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
	p1i = None if i!=0 else InterpPt(pts[i][0], pts[i+1][0], pts[i+2][0]) 
	p1 = Calc(p1i if p1i else pts[i-1][0], pts[i][0], pts[i+1][0])
	p2i = None if i!=len(pts)-2 else InterpPt(pts[i+1][0], pts[i][0], pts[i-1][0])
	p2 = Calc(p2i if p2i else pts[i+2][0], pts[i+1][0], pts[i][0])
	p3 = pts[i+1][0]
	for x,y in (p0,p1,p2,p3):
            rect(x, y, 2, 2)
        noFill()
	bezier(p0.x, p0.y, p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)

