cmake_minimum_required(VERSION 3.0.2)

include("CMakeLists-vsm.cmake")
project (a_project)

set(SOURCES_A "a.cpp" "a.h" "a-other.h")
set(SOURCES_A_PH "a.h" "a-other.h")
set(SOURCES_A_SUB "a_sub/a_sub.h")
set(SOURCES_A_SUB_PH "a_sub/a_sub.h")

add_subdirectory(tests)

add_library(a ${SOURCES_A} ${SOURCES_A_SUB})

INSTALL(TARGETS a
  ARCHIVE DESTINATION "lib/VsmSoftware"
)

install_sources_xyz_ph_files("include/VsmSoftware/a")
