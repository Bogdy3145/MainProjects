cmake_minimum_required(VERSION 3.26)
project(MPI)

set(CMAKE_CXX_STANDARD 17)

# Manually set MPI include and library paths
set(MPI_INCLUDE_PATH "C:/Program Files (x86)/Microsoft SDKs/MPI/Include")
set(MPI_CXX_LIBRARIES "C:/Program Files (x86)/Microsoft SDKs/MPI/Lib/x64/msmpi.lib")

# Include MPI headers
include_directories(${MPI_INCLUDE_PATH})

# Add executable
add_executable(MPI main.cpp
        karatsuba.cpp)

# Link MPI libraries
target_link_libraries(MPI ${MPI_CXX_LIBRARIES})
