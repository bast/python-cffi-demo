# stop configuration if cmake version is below 2.8
cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

# project name and enabled languages
project(example CXX Fortran)

# if CMAKE_BUILD_TYPE undefined, we set it to Release
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Release")
endif()

# compiler flags for release mode
set(CMAKE_CXX_FLAGS_RELEASE "-O3")
set(CMAKE_Fortran_FLAGS_RELEASE "-O3")

# set default build paths
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/lib)

include_directories(${PROJECT_BINARY_DIR})

# c library
add_library(
    pi_cpp
    SHARED
    pi/pi.cpp
    )

# fortran library
add_library(
    pi_f90
    SHARED
    pi/pi.f90
    )

# c executable
add_executable(
    pi_cpp.x
    pi/main.cpp
    )
# linked against both c and fortran libraries
target_link_libraries(
    pi_cpp.x
    pi_cpp
    pi_f90
    )

# fortran executable
add_executable(
    pi_f90.x
    pi/main.f90
    )
# linked against both c and fortran libraries
target_link_libraries(
    pi_f90.x
    pi_cpp
    pi_f90
    )

include(GenerateExportHeader)
generate_export_header(pi_cpp)
