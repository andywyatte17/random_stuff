cmake_minimum_required (VERSION 3.4)

SET(CMAKE_CXX_STANDARD 11)
SET(CMAKE_CXX_EXTENSIONS OFF)

project (memstream)

add_executable(memstream microtar.c microtar.h memstream.cpp)