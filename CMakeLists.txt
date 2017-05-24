cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(example C CXX Fortran)

add_library(c_example SHARED example.c)
add_library(fortran_example SHARED example.F90)

add_library(pi SHARED pi/pi.cpp)

include_directories(${PROJECT_BINARY_DIR})

add_executable(
    pi.x
    pi/main.cpp
    )

target_link_libraries(
    pi.x
    pi
    )

include(GenerateExportHeader)
generate_export_header(pi)
