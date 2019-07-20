cmake_minimum_required(VERSION 3.0.2)

project (a_project)

add_subdirectory(tests)

add_library(a a.cpp a.h)

set_target_properties(a PROPERTIES PUBLIC_HEADER "a.h")

INSTALL(TARGETS a
  ARCHIVE DESTINATION lib
  PUBLIC_HEADER DESTINATION include
)
