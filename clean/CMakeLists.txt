cmake_minimum_required(VERSION 3.16)
project(clean C)

set(CMAKE_C_STANDARD 99)

add_executable(hello  ${PROJECT_SOURCE_DIR}/hello.c onemore.c onemore.h)
