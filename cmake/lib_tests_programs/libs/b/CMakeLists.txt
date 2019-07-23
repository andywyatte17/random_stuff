cmake_minimum_required(VERSION 3.2)

#
# This demonstrates using python cog module to generate cmake files.
#
# python3 -m pip install --user cogapp
# python3 -m cogapp -r CMakeLists.txt
#
#

#[[[cog
#import CMakeLists
#CMakeLists.gen_sources()
#
#]]]

set(SOURCE_ "b.cpp" "b2.cpp" )
set(SOURCE_b_sub "b_sub/b_sub.cpp" )
set(SOURCE_tests "tests/tests_b.cpp" )

#[[[end]]]

project (lib_b)

#[[[cog
#import CMakeLists
#CMakeLists.gen_source_list('b')
#]]]

add_library(b ${SOURCE_} ${SOURCE_b_sub} ${SOURCE_tests} )

#[[[end]]]
