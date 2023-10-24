cmake_minimum_required(VERSION 3.21)
project(a5_6_Bogdy3145)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(a5_6_Bogdy3145 ui.cpp
        dynamicArray.cpp
        dynamicArray.h
        movie.cpp
        movie.h
        repo.cpp
        repo.h
        service.cpp
        service.h
        ui.h
        tests.h
        tests.cpp
        user.cpp
        user.h)
