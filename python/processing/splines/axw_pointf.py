#!/bin/python

from collections import namedtuple
import unittest

_PointF = namedtuple('PointF', ['x','y'])

class PointF(_PointF):
    def __init__(self, x=0, y=0):
        self._replace(x=float(x))
        self._replace(y=float(y))
    def __mul__(self, m):
        return PointF(m * self.x, m*self.y)
    def __add__(self, rhs):
        return PointF(self.x + rhs.x, self.y + rhs.y)
    def __sub__(self, rhs):
        return PointF(self.x - rhs.x, self.y - rhs.y)
    def magnitude(self):
	return (self.x**2 + self.y**2)**0.5

class TestPointF(unittest.TestCase):
    def test_simple(self):
        pt = PointF(2.0, 5.0)
        self.assertTrue(pt.x==2.0)
        self.assertTrue(pt.y==5.0)
    def test_multiply(self):
        pt = PointF(2,3)
        pt = pt * 5.0
        self.assertAlmostEqual(pt.x, 10.0)
        self.assertAlmostEqual(pt.y, 15.0)
    def test_add(self):
        pt = PointF(2,3) + PointF(-4.5, 6.3)
        self.assertAlmostEqual(pt.x, -2.5)
        self.assertAlmostEqual(pt.y, 9.3)
    def test_sub(self):
        pt = PointF(2,3) - PointF(4.5, -6.3)
        self.assertAlmostEqual(pt.x, -2.5)
        self.assertAlmostEqual(pt.y, 9.3)
    def test_print(self):
        self.assertEqual(str(PointF(2,3)), "PointF(x=2, y=3)")
    def test_magnitude(self):
	self.assertAlmostEqual(PointF(0,1).magnitude(), 1)

if __name__ == '__main__':
    unittest.main()
