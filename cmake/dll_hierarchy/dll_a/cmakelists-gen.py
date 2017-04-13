#!/bin/python

from jinja2 import Template
import os

os.chdir( os.path.dirname(os.path.abspath(__file__)) )

template = Template(open("../cmakelists-dlls.tpl", "r").read())

s = template.render(name='John Doe', \
    libname="A",
    sources=[{"name":"SOURCES_ROOT", "files":["a","b"]},
          {"name":"SOURCES_OTHER", "files":["c","d"]}]
)

print(s)
