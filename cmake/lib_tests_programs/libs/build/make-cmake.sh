#set path=%path%;C:\Program Files\CMake\bin
#set path_of_me_script=%%~dp0
rm -f CMakeCache.txt
cmake ../a/ -G"Xcode" -DCMAKE_INSTALL_PREFIX=../vsm_dev
cmake --build . --target install | xcpretty -c
cmake --build . --target a_tests | xcpretty -c
./tests/Debug/a_tests