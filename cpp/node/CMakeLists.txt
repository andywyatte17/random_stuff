cmake_minimum_required(VERSION 3.2)

project(node)

set(CMAKE_CXX_STANDARD 11)
add_compile_options(-std=c++11)

add_executable(node main.cpp node.h)

set_property(TARGET node PROPERTY CXX_STANDARD_REQUIRED 11)
