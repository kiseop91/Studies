message(STATUS "VCPKG_ROOT : $ENV{VCPKG_ROOT}")
cmake_minimum_required(VERSION 3.20)
project(sample LANGUAGES CXX)

#VCPKG_CHAINGLOAD_TOOLCHAIN_FILE
#vcpkg의 툴체인은 라이브러리관리용. 크로스컴파일용 toolchaing은 위 변수를 셋팅해줘야한다.!

message(STATUS "cmake:")
message(STATUS "  - version:   ${CMAKE_VERSION}")
message(STATUS "  - toolchain: ${CMAKE_TOOLCHAIN_FILE}")
message(STATUS "  - find_root_path: ${CMAKE_FIND_ROOT_PATH}") 
message(STATUS "compiler:")
message(STATUS "  - id: ${CMAKE_CXX_COMPILER_ID}")
message(STATUS "  - version: ${CMAKE_CXX_COMPILER_VERSION}")
message(STATUS "  - path: ${CMAKE_CXX_COMPILER}")
message(STATUS "android:")
message(STATUS "  - platform:  ${ANDROID_PLATFORM}")
message(STATUS "  - arch_name: ${ANDROID_ARCH_NAME}")
message(STATUS "  - abi: ${ANDROID_ABI}") # arm64-v8a 
message(STATUS "  - ndk: ${ANDROID_NDK}") # Path/to/NDK
message(STATUS "  - stl: ${ANDROID_STL}") # c++_shared

find_package(ZLIB 1.2 REQUIRED)