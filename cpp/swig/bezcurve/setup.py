from distutils.core import setup, Extension

extension_mod = Extension("_bezcurve",
                          sources=["bezcurve_wrap.cxx", "bezcurve.cpp"],
                          )

setup(name = "bezcurve",
      ext_modules=[extension_mod],
      py_modules = ["bezcurve"],
      swig_opts=['-c++'],
      )

