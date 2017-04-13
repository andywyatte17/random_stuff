cmake_minimum_required(VERSION 3.0.2)

# https://cognitivewaves.wordpress.com/cmake-and-visual-studio/

set (LIBNAME B)

project(${LIBNAME})

set(SOURCES_ROOT
  "main.cpp"
  "b.cpp"
)

source_group("_Src" FILES ${SOURCES_ROOT})

# ... stdafx ?
#if(MSVC)
#    foreach( src_file ${SOURCES_ROOT} )
#        set_source_files_properties(
#            ${src_file}
#            PROPERTIES
#            COMPILE_FLAGS "/Yustdafx.h"
#            )
#    endforeach()
#
#    foreach( src_file ${SOURCES_MULTIWAVEFILL}
#                      ${SOURCES_STITCHTOOBJECT} ${SOURCES_OBJECTSUMMARY}
#                      ${SOURCES_SATINTRACE} ${SOURCES_DRAWING})
#        set_source_files_properties(
#            ${src_file}
#            PROPERTIES
#            COMPILE_FLAGS "/Yu../stdafx.h"
#            )
#    endforeach()
#
#    set_source_files_properties(stdafx.cpp
#        PROPERTIES
#        COMPILE_FLAGS "/Ycstdafx.h"
#        )
#endif()

add_library(${LIBNAME} SHARED
  ${SOURCES_ROOT}
)

# INSTALL_DST_ROOT should be in CMAKE_PATH format - it then works correctly
#   with INSTALL(CODE "...")
FILE(TO_CMAKE_PATH "${CMAKE_BINARY_FOLDER}/install/" INSTALL_DST_ROOT)
SET(INSTALL_DST_ROOT "${INSTALL_DST_ROOT}/HeaderFiles/Dlls/${LIBBASE}")

# Clean-up header files folder
# install(CODE "FILE(REMOVE_RECURSE ${INSTALL_DST_ROOT})")

# Install header files
INSTALL(FILES
  "a.h"
  DESTINATION "${INSTALL_DST_ROOT}")

# Give the output name something different to the Release
set_target_properties(${LIBNAME} PROPERTIES OUTPUT_NAME_DEBUG ${LIBNAME}D)
set_target_properties(${LIBNAME} PROPERTIES COMPILE_PDB_NAME_DEBUG ${LIBNAME}D)
set_target_properties(${LIBNAME} PROPERTIES COMPILE_PDB_NAME_RELEASE ${LIBNAME})
set_target_properties(${LIBNAME} PROPERTIES COMPILE_PDB_NAME_RELWITHDEBINFO ${LIBNAME})
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAG} /EHsc /wd4456 /wd4458 /wd4459 /wd4457")
