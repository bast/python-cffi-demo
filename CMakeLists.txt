cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(example C Fortran)

add_library(c_example SHARED example.c)
add_library(fortran_example SHARED example.F90)
