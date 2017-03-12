from distutils.core import setup, Extension

extension_mod = Extension("bezcurve", ["_bezcurve_module.cpp", "bezcurve.cpp"])

setup(name = "bezcurve", ext_modules=[extension_mod],
                         swig_opts=['-c++'],
                         )

