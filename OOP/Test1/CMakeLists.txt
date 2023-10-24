cmake_minimum_required(VERSION 3.21)
project(t1_Bogdy3145)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(t1_Bogdy3145
        bills.cpp
        bills.h
        dynamicArray.cpp
        dynamicArray.h
        repo.cpp
        repo.h
        service.cpp
        service.h
        ui.cpp
        tests.cpp
        tests.h)
