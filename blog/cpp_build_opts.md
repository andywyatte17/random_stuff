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

python -m timeit -n 1 -r 1 "import os; os.system('msbuild my.sln /t:rebuild')"
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

  * Compile, no precompiled header
    * 2m 5s (1x).
  * Compile, with precompiled header (all files)
    * 0m 45s (0.36x).

It was surprisingly easy to get such a good improvement in the compile-times just by changing the CMakeLists.txt file (and making a few minor tweaks to the source files - not all files had a stdafx.h include at their beginning).

### Precompiled headers - draw-backs

The precompiled header used in the above results pulls in many header files, including those from other related libraries and also the 'self' library. You might refer to such source files as less-stable, ie they are changing more frequently, for example if you are working on the project in question and recompiling frequently. This should be contrasted with, say, Standard C++ Library headers which are stable (ie they change infrequently and never due to a change that you as the developer actions).

Therefore a school of thought goes that you should not put less-stable headers in the precompiled header because any change to such headers will force a recompile of every cpp file in your project. So essentially you gain in a clean-rebuild, but lose out in a compile-after-source-change.
