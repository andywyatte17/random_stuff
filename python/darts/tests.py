import unittest

TEST = R"""

References

   Visible links
   1. http://www.google.co.uk/search?q=hey&um=1&ie=UTF-8&hl=en&tbm=isch&source=og&sa=N&tab=wi
   2. http://maps.google.co.uk/maps?q=hey&um=1&ie=UTF-8&hl=en&sa=N&tab=wl
   3. https://play.google.com/?q=hey&um=1&ie=UTF-8&hl=en&sa=N&tab=w8
   4. http://www.youtube.com/results?q=hey&um=1&ie=UTF-8&gl=GB&sa=N&tab=w1
"""

class Test(unittest.TestCase):
  def setUp(self):
    pass
    
  def test_get_nearest_week(self):
    yd = lambda y_m_d : dt.datetime(y_m_d[0], y_m_d[1], y_m_d[2], 0, 0, 0, 0).timetuple().tm_yday
    w = get_nearest_week( yd((2017,2,2)) )
    self.assertEqual(w,1)
    w = get_nearest_week( yd((2017,2,2+6)) )
    self.assertEqual(w,1)
    w = get_nearest_week( yd((2017,2,2+7)) )
    self.assertEqual(w,2)
    w = get_nearest_week( yd((2016,1,1)) )
    self.assertEqual(w,1)
