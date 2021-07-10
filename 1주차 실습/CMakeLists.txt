cmake_minimum_required(VERSION 3.19.2 FATAL_ERROR) # 가능하면 3.11이상 버전을 쓰는 것을 추천

project(hell_world)

set(a "CMake is Hell")
message(${a})

#find_file (변수 찾을파일이름 찾을경로) short hand command

# find_file (
#           <VAR>  변수명 
#           name | NAMES name1 [name2 ...]  이름 / 후보군들..
#           [HINTS [path | ENV var]... ]
#           [PATHS [path | ENV var]... ]
#           [PATH_SUFFIXES suffix1 [suffix2 ...]]
#           [DOC "cache documentation string"]
#           [NO_CACHE]
#           [REQUIRED]
#           [NO_DEFAULT_PATH]
#           [NO_PACKAGE_ROOT_PATH]
#           [NO_CMAKE_PATH]
#           [NO_CMAKE_ENVIRONMENT_PATH]
#           [NO_SYSTEM_ENVIRONMENT_PATH]
#           [NO_CMAKE_SYSTEM_PATH]
#           [CMAKE_FIND_ROOT_PATH_BOTH |
#            ONLY_CMAKE_FIND_ROOT_PATH |
#            NO_CMAKE_FIND_ROOT_PATH]
#          )

message(STATUS "ENV PATH: $ENV{PATH}")

find_file(TXT_PATH 
    NAMES a.txt
    PATHS ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_SOURCE_DIR}
)
message(STATUS "Found txt : ${TXT_PATH}")

project(hell_world 
    VERSION 2021.7.10
    LANGUAGES C CXX
)

message(${PROJECT_NAME})
message(${PROJECT_VERSION})

enable_language(CXX)

# cmake 버전 3점대에서는 타겟을 먼저만들고, target_sources로 지정해서 사용한다.
# 변수에 몰아서 라이브러리에 넣어주는 것은 2점대에서 사용하던 패턴이다.