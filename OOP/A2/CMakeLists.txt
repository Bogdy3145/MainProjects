cmake_minimum_required(VERSION 3.21)
project(a3_4_Bogdy3145 C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_executable(a3_4_Bogdy3145
        domain.c
        domain.h
        repo.c
        repo.h
        service.c
        service.h
        ui.c
        ui.h
        dynamicArray.c
        dynamicArray.h
        tests.c
        tests.h)
