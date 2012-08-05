if(EXISTS ${CMAKE_CURRENT_BINARY_DIR}/package.cmake)
  include(${CMAKE_CURRENT_BINARY_DIR}/package.cmake)
endif()
rosbuild_add_library(topic_tools src/shape_shifter.cpp src/parse.cpp)
rosbuild_add_executable(switch_mux src/switch_mux.cpp)
target_link_libraries(switch_mux topic_tools)
rosbuild_add_executable(mux src/mux.cpp)
target_link_libraries(mux topic_tools)
rosbuild_add_executable(relay src/relay.cpp)
target_link_libraries(relay topic_tools)
rosbuild_add_executable(drop src/drop.cpp)
target_link_libraries(drop topic_tools)
#rosbuild_add_executable(demux demux.cpp)
#target_link_libraries(demux topic_tools)
rosbuild_add_executable(throttle src/throttle.cpp)
target_link_libraries(throttle topic_tools)

