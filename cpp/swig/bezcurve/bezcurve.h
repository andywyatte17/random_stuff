//

#pragma once

#ifdef SWIG
#  define DLL_PUBLIC
#else
// #  define DLL_PUBLIC __attribute__ ((visibility ("default")))
#  define DLL_PUBLIC
#endif

class DLL_PUBLIC BezCurve
{
public:
  BezCurve();
  void AddPoint(float x, float y);
};

