cmake_minimum_required(VERSION 3.0.2)

project (a_project)

add_subdirectory(tests)

add_library(a a.cpp a.h "a_sub/a_sub.h")

set_target_properties(a PROPERTIES PUBLIC_HEADER "a.h")
set_target_properties(a PROPERTIES PUBLIC_HEADER "a_sub\\a_sub.h")

#INSTALL(TARGETS a
#  ARCHIVE DESTINATION "lib\\VsmSoftware\\a"
#  PUBLIC_HEADER DESTINATION "include\\VsmSoftware\\a"
#)

INSTALL(TARGETS a
  ARCHIVE DESTINATION "lib\\VsmSoftware\\a"
)
