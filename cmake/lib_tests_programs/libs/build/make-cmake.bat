set path=%path%;C:\Program Files\CMake\bin
@rem set path_of_me_script=%%~dp0
cmake ..\a\ -DCMAKE_INSTALL_PREFIX=..\vsm_dev
cmake --build . --target install