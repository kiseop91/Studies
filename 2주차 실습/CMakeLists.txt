# Import Target : 미리 빌드된 타겟

# Alias Target : 별칭 타겟. (네임스페이스개념 : 별칭을 달면 리드온리)

# Interface Target : 헤더온리 타겟.

# CMake 문서에서  <> 필수 , []은 옵션

# Cmake 3.11부터 add_library에 넣지않고, 나중에 target_sources에 넣어도된다.

# Imported Executable?

# set_target_properties


cmake_minimum_required(VERSION 3.18)
project(hell_world VERSION 1.0.0 LANGUAGES CXX)

option(BUILD_SHARED_LIBS "Create shared libraries if ON" OFF)

message(STATUS "Using Generator : ${CMAKE_GENERATOR}")

add_library(hell_world)

target_sources(hell_world PUBLIC main.cpp)

if(WIN32)
    set_target_properties(hell_world
    PROPERTIES
        CXX_STANDARD 17
        WINDOWS_EXPORT_ALL_SYMBOLS OFF
    )
endif()

message(STATUS "System Name : ${CMAKE_SYSTEM_NAME}")
# 빌드 Config에 따라서 이름을 다르게 하도록 할 수 있습니다. <CONFIG>_POSTFIX
if(CMAKE_SYSTEM_NAME STREQUAL Windows)
    set_target_properties(hell_world
    PROPERTIES
        DEBUG_POSTFIX D
        LIBRARY_OUTPUT_NAME main
    )
endif()

if(MSVC) # https://docs.microsoft.com/en-us/cpp/build/reference/linker-options?view=msvc-160
    target_link_options(hell_world
    PRIVATE
        /ERRORREPORT:SEND
    )
endif()

find_package(Git REQUIRED)

add_custom_target(check1
    COMMAND ${GIT_EXECUTABLE} --version
    COMMENT "target - check1"
)
add_custom_target(check2
    COMMAND ${GIT_EXECUTABLE} rev-parse HEAD
    COMMENT "target - check2"
)
add_dependencies(check2 check1)

message(STATUS "CMAKE INSTALL PREFIC : ${CMAKE_BINARY_DIR}")
install(TARGETS hell_world
        RUNTIME  DESTINATION ${CMAKE_BINARY_DIR}/bin
        LIBRARY  DESTINATION ${CMAKE_BINARY_DIR}/lib
        ARCHIVE  DESTINATION ${CMAKE_BINARY_DIR}/lib
        INCLUDES DESTINATION ${CMAKE_BINARY_DIR}/include
)

include(CMakePackageConfigHelpers)
set(VERSION_FILE_PATH   ${CMAKE_BINARY_DIR}/cmake/${PROJECT_NAME}-config-version.cmake)
write_basic_package_version_file(${VERSION_FILE_PATH}
    VERSION             ${PROJECT_VERSION}
    COMPATIBILITY       SameMajorVersion
)
install(FILES           ${VERSION_FILE_PATH} 
        DESTINATION     ${CMAKE_BINARY_DIR}/share/${PROJECT_NAME}
)