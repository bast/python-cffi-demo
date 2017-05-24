cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(example C CXX Fortran)

add_library(c_example SHARED example.c)
add_library(fortran_example SHARED example.F90)

include_directories(${PROJECT_BINARY_DIR})

foreach(language cpp f90)
    add_library(
        pi-${language}
        SHARED
        pi/pi.${language}
        )

    add_executable(
        pi-${language}.x
        pi/main.${language}
        )

    target_link_libraries(
        pi-${language}.x
        pi-${language}
        )
endforeach()

include(GenerateExportHeader)
generate_export_header(pi-cpp)
