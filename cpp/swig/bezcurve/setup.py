from distutils.core import setup, Extension

extension_mod = Extension("_bezcurve", ["_bezcurve_module.cpp"])

setup(name = "bezcurve", ext_modules=[extension_mod])
