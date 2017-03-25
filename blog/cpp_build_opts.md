## Cpp Build Optimisations

### Aims

We have some old code which has stdafx.h (Visual Studio precompiled headers) that previously were used to optimise build performance.

  * How beneficial for compile-times are precompiled headers?

### Test build times

I have a project that is not properly setup with precompiled headers. I want to time how long a build takes (Visual Studio - msbuild) on a solution, then setup precompiled headers and test the time again.

```
rem Normal MSVC stuff in cmd to setup compilation
call "%VS140COMNTOOLS%"\vsvars32.bat
cd path\to\project

rem ... our build task : msbuild my.sln /t:rebuild
rem ... install python-timeit : python -m pip install --user timeit

python -m timeit -n 1 -r 1 "import os; os.system('msbuild /m my.sln /t:rebuild')"
```

### NB: CMake and precompiled headers

http://stackoverflow.com/questions/148570/using-pre-compiled-headers-with-cmake

My favoured solution:

```
if(MSVC)
    foreach( src_file ${SOURCES_ROOT} )
        set_source_files_properties(
            ${src_file}
            PROPERTIES
            COMPILE_FLAGS "/Yustdafx.h"
            )
    endforeach()
    set_source_files_properties(stdafx.cpp
        PROPERTIES
        COMPILE_FLAGS "/Ycstdafx.h"
        )
endif()
```

### My Results

Project 1:

  * Compile, no precompiled header
    * 2m 5s (1x).
  * Compile, with precompiled header (all files)
    * 0m 45s (0.36x).

All libraries project:

* Compile, no precompiled header
  * 13m 56s
* Compile, with precompiled header (all files)
  * 10m 01s
  * Only 8 out of 22 projects use precompiled headers.

It was surprisingly easy to get such a good improvement in the compile-times just by changing the CMakeLists.txt file (and making a few minor tweaks to the source files - not all files had a stdafx.h include as their first ```#include```).

### Precompiled headers - draw-backs

The precompiled header used in the above results pulls in many header files, including those from other related libraries and also the 'self' library. You might refer to such source files as less-stable, ie they are changing more frequently, for example if you are working on the project in question and recompiling frequently. This should be contrasted with, say, Standard C++ Library headers which are stable (ie they change infrequently and never due to a change that you as the developer actions).

Therefore a school of thought goes that you should not put less-stable headers in the precompiled header because any change to such headers will force a recompile of every cpp file in your project. So essentially you gain in a clean-rebuild, but lose out in a compile-after-source-change.

### Line Counting files and stdafx.h

The following to be used to line count files produced by compiling c++ code using
MSVC cl.exe compiler:

NB: I installed gnuwin32 via getgnuwin32 to get \*n\*x utilities like *sed*.

```
cl /C /EP -D _ITERATOR_DEBUG_LEVEL=1 path\to\xyz.cpp | find /v /c ""
```

Here's my command to do a line count on a cpp file but with the stdafx.h file removed:

```
CPP=path\to\xyz.cpp
type "%CPP%" | sed "s/#include \"stdafx.h\"/\/\/ #include \"stdafx.h\"/g" > "%CPP%".tmp.cpp
cl /C /EP -D _ITERATOR_DEBUG_LEVEL=1 "%CPP%".tmp.cpp | find /v /c ""
```

This is useful because you can see how many lines of C++ code you add by adding the ```#include "stdafx.h"``` line to your cpp file.

You can also line count the stdafx.h alone using:

```
cl /C /EP -D _ITERATOR_DEBUG_LEVEL=1 path\to\stdafx.cpp | find /v /c ""
```

### ...

...
