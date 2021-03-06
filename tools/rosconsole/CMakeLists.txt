if(ROSBUILD)
  include(rosbuild.cmake)
  return()
endif()

cmake_minimum_required(VERSION 2.4.6)
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)

set(ROS_BUILD_TYPE RelWithDebInfo)
#set(ROS_BUILD_TYPE Debug)

rosbuild_init()

# See ticket: https://code.ros.org/trac/ros/ticket/3626
# On mac use g++-4.2
IF(${CMAKE_SYSTEM} MATCHES "Darwin-11.*")
  IF(EXISTS "/usr/bin/g++-4.2")
    set(CMAKE_CXX_COMPILER /usr/bin/g++-4.2)
  ELSE(EXISTS "/usr/bin/g++-4.2")
    # If there is no g++-4.2 use clang++
    set(CMAKE_CXX_COMPILER /usr/bin/clang++)
  ENDIF(EXISTS "/usr/bin/g++-4.2")
ENDIF(${CMAKE_SYSTEM} MATCHES "Darwin-11.*")

include_directories(include/rosconsole)
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

rosbuild_add_boost_directories()

rosbuild_add_library(${PROJECT_NAME} src/rosconsole/rosconsole.cpp)

# required for correct linking with log4cxx
find_package(PkgConfig)
pkg_check_modules(LOG4CXX REQUIRED liblog4cxx>=0.10.0)
get_target_property(_rpaths ${PROJECT_NAME} INSTALL_RPATH)
list(APPEND _rpaths ${LOG4CXX_LIBRARY_DIRS})
set_target_properties(${PROJECT_NAME} PROPERTIES INSTALL_RPATH "${_rpaths}")
include_directories(${LOG4CXX_INCLUDE_DIRS})
target_link_libraries(${PROJECT_NAME} ${LOG4CXX_LDFLAGS})
rosbuild_link_boost(${PROJECT_NAME} thread regex)

rosbuild_add_executable(example examples/example.cpp)
target_link_libraries(example ${PROJECT_NAME})
# static libraries all need to be called for mingw. 
if(MINGW) 
  rosbuild_link_boost(example thread regex)
  target_link_libraries(example log4cxx aprutil-1 expat apr-1 rpcrt4 shell32 ws2_32 advapi32 kernel32 msvcrt)
endif()
set_target_properties(example PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/examples)

rosbuild_add_gtest(test/utest test/utest.cpp)
target_link_libraries(test/utest ${PROJECT_NAME})

if(${CMAKE_SYSTEM_NAME} STREQUAL Linux)
  rosbuild_add_gtest(test/assertion_test test/assertion_test.cpp)
  target_link_libraries(test/assertion_test ${PROJECT_NAME})
endif(${CMAKE_SYSTEM_NAME} STREQUAL Linux)

rosbuild_add_gtest(test/thread_test test/thread_test.cpp)
target_link_libraries(test/thread_test ${PROJECT_NAME})

#rosbuild_add_executable(speed_test test/speed_test.cpp)
#target_link_libraries(speed_test ${PROJECT_NAME})
#set_target_properties(speed_test PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/test)

