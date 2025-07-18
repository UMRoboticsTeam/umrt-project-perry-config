cmake_minimum_required(VERSION 3.22)
project(project_perry_project_perry_ikfast_plugin)

if(NOT "${CMAKE_CXX_STANDARD}")
  set(CMAKE_CXX_STANDARD 14)
endif()
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(ament_cmake REQUIRED)
find_package(moveit_core REQUIRED)
find_package(pluginlib REQUIRED)
find_package(rclcpp REQUIRED)
find_package(tf2_kdl REQUIRED)
find_package(tf2_eigen REQUIRED)
find_package(LAPACK REQUIRED)

include_directories(include)

set(IKFAST_LIBRARY_NAME project_perry_project_perry_moveit_ikfast_plugin)
add_library(${IKFAST_LIBRARY_NAME} SHARED src/project_perry_project_perry_ikfast_moveit_plugin.cpp)
ament_target_dependencies(${IKFAST_LIBRARY_NAME}
  rclcpp
  moveit_core
  pluginlib
  tf2_kdl
  orocos_kdl
  tf2_eigen
  LAPACK
)
# suppress warnings about unused variables in OpenRave's solver code
target_compile_options(${IKFAST_LIBRARY_NAME} PRIVATE -Wno-unused-variable -Wno-unused-parameter)

install(TARGETS ${IKFAST_LIBRARY_NAME}
  EXPORT export_${PROJECT_NAME}
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib
  RUNTIME DESTINATION bin)

pluginlib_export_plugin_description_file(moveit_core project_perry_project_perry_moveit_ikfast_plugin_description.xml)

ament_export_targets(export_${PROJECT_NAME} HAS_LIBRARY_TARGET)
ament_export_dependencies(moveit_core)
ament_export_dependencies(pluginlib)
ament_export_dependencies(rclcpp)
ament_export_dependencies(tf2_kdl)
ament_export_dependencies(tf2_eigen)

# Parse version number from the file
file(READ "version" version_input)
string(REGEX MATCH "([0-9]+)\.([0-9]+)\.([0-9]+)" _ ${version_input})

# Fill version number into package.xml
configure_file(
        package.in.xml
        ${CMAKE_CURRENT_SOURCE_DIR}/package.xml
        @ONLY
)

ament_package()
