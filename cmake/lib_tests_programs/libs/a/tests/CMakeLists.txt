cmake_minimum_required(VERSION 3.2)

project (a_project)

add_executable(a_tests tests_a.cpp)

target_include_directories(a_tests SYSTEM PUBLIC
  $<BUILD_INTERFACE:${CMAKE_INSTALL_PREFIX}>/include
)

add_dependencies(a_tests a)
target_link_libraries(a_tests a)
