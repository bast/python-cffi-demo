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

# workaround for CMP0042 warning on Mac
if(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    if(NOT DEFINED CMAKE_MACOSX_RPATH)
        set(CMAKE_MACOSX_RPATH ON)
    endif()
endif()

# set default build paths
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/lib)

# generated export header will be placed here
include_directories(${PROJECT_BINARY_DIR})

# c library
add_library(
    pi_cpp
    SHARED
    island/pi.cpp
    )

# fortran library
add_library(
    pi_fortran
    SHARED
    island/pi.f90
    )

# c executable
add_executable(
    pi_cpp.x
    island/main.cpp
    )
# linked against both c and fortran libraries
target_link_libraries(
    pi_cpp.x
    pi_cpp
    pi_fortran
    )

# fortran executable
add_executable(
    pi_fortran.x
    island/main.f90
    )
# linked against both c and fortran libraries
target_link_libraries(
    pi_fortran.x
    pi_cpp
    pi_fortran
    )

# we let cmake generate the export header
include(GenerateExportHeader)
generate_export_header(
    pi_cpp
    BASE_NAME pi
    )

install(
    TARGETS
        pi_cpp
        pi_fortran
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    )

install(
    FILES
        island/pi.h
        ${PROJECT_BINARY_DIR}/pi_export.h
    DESTINATION
        include
    )
