set path=%path%;C:\Program Files (x86)\CMake\bin
pushd .
cd %~dp0
cd build
cmake ..
popd