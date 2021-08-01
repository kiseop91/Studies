
# Directory
# 소스코드 관리 및 build system 파일 생성.

#Scripts
# 빌드타겟이 정의되지않음. 실행해도 Build system 파일이 생성되지않는다.

#Modules
# CMAKE_MOUDLE_PATH를 통해 검색됨.

cmake_minimum_required(VERSION 3.15)
project(sample LANGUAGES CXX)

include(CheckCXXCompilerFlag) #컴파일러 플레그 체크
check_cxx_compiler_flag(-std=c++14 supports_native_arch)
check_cxx_compiler_flag(-std=c++17 supports_native_arch)


include(CheckIncludeFileCXX) #파일이 있는지 찾아보는 함수
list(APPEND CMAKE_REQUIRED_FLAGS "...")
check_include_file_cxx("sys/stat.h" found_sys_stat)


include(CheckCXXSymbolExists)
check_cxx_symbol_exists(SEEK_SET "cstdio" HAVE_SEEK_SET)
check_cxx_symbol_exists(std::fopen "cstdio" HAVE_STD_FOPEN)


#Find Package!
find_package(Threads) # include(FindThreads)와 동일하다. (이건 레거시.)


find_package(Python3 REQUIRED
COMPONENTS
    Interpreter
)

if(Python3_FOUND)
    message(STATUS "Python3:")
    message(STATUS "  version: ${Python3_VERSION}")
    message(STATUS "  executable: ${Python3_EXECUTABLE}")
    message(STATUS "  Interpreter: ${Python3_INTERPRETER_ID}")
    message(STATUS "  include:")
    foreach(folder ${Python3_INCLUDE_DIRS})
        message(STATUS "    - ${folder}")
    endforeach()
endif()

function(print_folders LABEL DIRS)
    list(LENGTH DIRS length)
    if(NOT length)
        return()
    endif()
    message(STATUS "  ${LABEL}:")
    foreach(name  ${DIRS})
        message(STATUS "    - ${name}")
    endforeach()
endfunction()

list(APPEND folders "floder1" "folders2")

print_folders("aaaa" ${folders})

