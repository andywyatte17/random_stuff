cmake_minimum_required(VERSION 3.2)

ADD_EXECUTABLE(client2 client2.cpp)

INCLUDE_DIRECTORIES("/usr/include/python2.7/")

add_definitions(-std=c++11)

TARGET_LINK_LIBRARIES(client2 
  "/usr/lib/i386-linux-gnu/libboost_python-py27.so.1.58.0"
  "/usr/lib/i386-linux-gnu/libpython2.7.so"
  "/usr/lib/i386-linux-gnu/libboost_system.so.1.58.0"
  "/usr/lib/i386-linux-gnu/libboost_thread.so.1.58.0"
  "/usr/lib/i386-linux-gnu/libboost_coroutine.a"
  "/usr/lib/i386-linux-gnu/libboost_context.so.1.58.0"
  "/usr/lib/i386-linux-gnu/libboost_python-py27.so.1.58.0"
  "/usr/lib/i386-linux-gnu/libboost_python-py27.so.1.58.0"
)
