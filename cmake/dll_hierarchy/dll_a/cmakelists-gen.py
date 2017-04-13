#!/bin/python

from jinja2 import Template
import os

os.chdir( os.path.dirname(os.path.abspath(__file__)) )

template = Template(open("../cmakelists-dlls.tpl", "r").read())

def my_glob(root, extensions, exclusions = []):
    import glob
    results = []
    for x in glob.glob(root + "\\*.*"):
        added = False
        for ext in extensions:
            if x.lower().endswith('.' + ext.lower()):
                results.append( root + '/' + os.path.basename(x) )
                added = True
                break
        if added:
            for exc in exclusions:
                if results[-1].lower().endswith(exc.lower()):
                    results.pop()
                    break
    return results
    
s = template.render(name='John Doe', \
    libname="A",
    shared_static="SHARED",
    sources=[{"name":"SOURCES_ROOT",
                "group":"_Src",
                "files":my_glob(".", ['cpp', 'h'], ['resource.h'])},
             {"name":"SOURCES_RC",
                "group":"rc",
                "files":my_glob(".", ['rc', 'rc2', 'resource.h'])},
             {"name":"SOURCES_F1",
                "group":"f1",
                "files":my_glob("f1", ['cpp', 'h'])}
            ],
    install_files=[ {"folder":"A/", "files":["a.h"]} ]
)

print(s)
