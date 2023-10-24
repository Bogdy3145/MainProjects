cmake_minimum_required(VERSION 3.21)
project(DSA)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(DSA
        App.cpp
        ExtendedTest.cpp
        ExtendedTest.h
        Set.cpp
        Set.h
        SetIterator.cpp
        SetIterator.h
        ShortTest.cpp
        ShortTest.h)
