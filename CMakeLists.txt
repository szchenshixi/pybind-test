cmake_minimum_required(VERSION 3.10)
project(pybind-test CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_CXX_STANDARD 11)

set(SRC main.cpp)

add_executable(run ${SRC})
find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS} extern/pybind11/include)
target_link_libraries(run PUBLIC ${PYTHON_LIBRARIES})

