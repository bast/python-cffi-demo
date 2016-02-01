cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(python-cffi-demo)

enable_language(C CXX)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/lib)

file(MAKE_DIRECTORY ${PROJECT_BINARY_DIR}/include)
file(COPY ${PROJECT_SOURCE_DIR}/api/example.h  DESTINATION ${PROJECT_BINARY_DIR}/include)
file(COPY ${PROJECT_SOURCE_DIR}/api/example.py DESTINATION ${PROJECT_BINARY_DIR})

include_directories(${PROJECT_SOURCE_DIR}/api)

add_library(
    example
    SHARED
    src/example.cpp
    )
