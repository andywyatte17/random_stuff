#!/bin/python

import os, sys

stdafx_h = R"""//
// stdafx.h
//

#include "../OsBridge/platform.h"

#if VSM_PLATFORM==VSM_PLATFORM_WINXX

#include "../Fundamentals/stdafx_cmn.h"
#include <vector>

#endif
"""

stdafx_cpp = R"""//
// stdafx.cpp
//

#include "stdafx.h"
"""

def MakeStdafxPath(cppPath):
    dirname = os.path.dirname(cppPath)
    stdafx_h_loc = "stdafx.h"
    for i in range(0,10):
        if os.path.exists( os.path.join(dirname, stdafx_h_loc) ):
            return stdafx_h_loc
        stdafx_h_loc = "../" + stdafx_h_loc
    raise RuntimeError("Whoops!")

def AddStdafxHeaderToCpp(cppPath):
    stdafx_h_loc = MakeStdafxPath(cppPath)
    old_stdout = sys.stdout
    import fileinput
    found = False
    for line in fileinput.input(cppPath, inplace=1):
        if line.startswith('#include') and not found:
            # old_stdout.write(cppPath)
            if not ("stdafx.h" in line):
                print('''#include "stdafx.h"'''.replace("stdafx.h", stdafx_h_loc))
            print(line.replace("\n","").replace("\r",""))
            found = True
        else:
            print(line.replace("\n","").replace("\r",""))

project_root = sys.argv[1]
os.chdir(project_root)
if not open("stdafx.cpp", "r"):
    open("stdafx.cpp", "w").write( stdafx_cpp )
if not open("stdafx.h", "r"):
    open("stdafx.h", "w").write( stdafx_h )

for root, dirs, files in os.walk('.'):
    for x in [os.path.join(root, name) for name in files]:
        if not x.endswith(".cpp"): continue
        if "Tests\\" in x: continue
        if "stdafx" in x: continue
        AddStdafxHeaderToCpp(x)
