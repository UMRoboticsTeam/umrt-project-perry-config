cmake_minimum_required(VERSION 3.16)
project(umrt-project-perry-description)

set(CMAKE_CXX_STANDARD 14)

if(CMAKE_CXX_COMPILER_ID MATCHES "(GNU|Clang)")
    add_compile_options(-Wall -Wextra -fPIC)
endif()

# Fixes intellisense not finding ros2 headers https://youtrack.jetbrains.com/issue/CPP-29747/Certain-ROS2-package-headers-missing-from-Intellisense-when-using-a-Docker-toolchain
include_directories(SYSTEM /opt/ros/$ENV{ROS_DISTRO}/include)

# find dependencies
set(THIS_PACKAGE_INCLUDE_DEPENDS
)

# find dependencies
find_package(ament_cmake REQUIRED)
foreach(Dependency IN ITEMS ${THIS_PACKAGE_INCLUDE_DEPENDS})
    find_package(${Dependency} REQUIRED)
endforeach()

# Parse version number from the file
file(READ "../version" version_input)
string(REGEX MATCH "([0-9]+)\.([0-9]+)\.([0-9]+)" _ ${version_input})

# Fill version number into package.xml
configure_file(
        package.in.xml
        ${CMAKE_CURRENT_SOURCE_DIR}/package.xml
        @ONLY
)


# INSTALL
install(
        DIRECTORY urdf rviz
        DESTINATION share/${PROJECT_NAME}/
)

ament_package()
