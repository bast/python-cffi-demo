cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(example C CXX Fortran)

add_library(c_example SHARED example.c)
add_library(fortran_example SHARED example.F90)

include_directories(${PROJECT_BINARY_DIR})

# c library
add_library(
    pi-cpp
    SHARED
    pi/pi.cpp
    )

# fortran library
add_library(
    pi-f90
    SHARED
    pi/pi.f90
    )

# c executable
add_executable(
    pi-cpp.x
    pi/main.cpp
    )
target_link_libraries(
    pi-cpp.x
    pi-cpp
    pi-f90
    )

# fortran executable
add_executable(
    pi-f90.x
    pi/main.f90
    )
target_link_libraries(
    pi-f90.x
    pi-cpp
    pi-f90
    )

include(GenerateExportHeader)
generate_export_header(pi-cpp)
