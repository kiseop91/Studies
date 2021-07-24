cmake_minimum_required(VERSION 3.13)
project(sample LANGUAGES CXX)

#테스트 프로젝트 빌드옵션
option(BUILD_TESTING "Build test programs" ON)

# conan install . -if build --build missing -s build_type=Debug
find_file(CONAN_SCRIPT 
    NAMES conanbuildinfo.txt
    PATHS ${CMAKE_BINARY_DIR}
          ${PROJECT_SOURCE_DIR}/build
)
if(CONAN_SCRIPT)
    get_filename_component(CONAN_SCRIPT_DIR ${CONAN_SCRIPT} DIRECTORY)
    list(APPEND CMAKE_MODULE_PATH ${CONAN_SCRIPT_DIR})
endif()

if(NOT BUILD_TESTING)
    return()
endif()
enable_testing()

#오호.. 이렇게 add_test를 통해 명령어가 제대로 실행됐는지 테스트케이스로 실행해볼수있따.
if(WIN32)
    add_test(NAME feature_Win32 COMMAND systeminfo)
elseif(APPLE)
    add_test(NAME feature_Apple COMMAND uname -a)
endif()

find_package(Catch2 REQUIRED)
#패키지를 찾을때 빌트인말고..
#list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR}) 처럼 내가 지정해서 쓸수도있다.

add_executable(test_suite
    test_main.cpp
)

set_target_properties(test_suite
PROPERTIES
    CXX_STANDARD 17
)

target_link_libraries(test_suite
PRIVATE
    Catch2::Catch2
)

add_test(
    NAME test_all
    COMMAND test_suite 
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
)