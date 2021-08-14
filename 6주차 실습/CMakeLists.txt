cmake_minimum_required(VERSION 3.19)
project(boost_test_suite VERSION 2021.0814.1 LANGUAGES CXX)

# .cmake - include() 모듈패스를 추가한다.
list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/build-debug)

find_package(BZip2 REQUIRED) # BZip2::BZip2
find_package(OpenSSL REQUIRED) # OpenSSL::SSL OpenSSL::Crypto
find_package(Boost REQUIRED) # Boost::filesystem


# Git 패키지를 사용해서, 해드의 리비전을 가져온다.
find_package(Git REQUIRED)
execute_process(
    COMMAND "${GIT_EXECUTABLE}" rev-parse HEAD
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
    OUTPUT_VARIABLE GIT_COMMIT_ID
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

message(STATUS "Using commit: ${GIT_COMMIT_ID}")

string(TIMESTAMP BUILD_TIMESTAMP UTC) # %Y-%m-%dT%H:%M:%SZ

add_executable(boost_test_suite
    test_main.cpp
)

set_target_properties(boost_test_suite
PROPERTIES
    CXX_STANDARD 17
)

if(CMAKE_CXX_COMPILER_ID MATCHES Clang)
    target_compile_options(boost_test_suite
    PRIVATE
        -stdlib=libc++
    )
endif()

target_link_libraries(boost_test_suite
PRIVATE
    ${CMAKE_DL_LIBS} BZip2::BZip2 OpenSSL::SSL OpenSSL::Crypto Boost::filesystem
)

include(GNUInstallDirs)

install(TARGETS boost_test_suite
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

set(CPACK_PACKAGE_NAME ${PROJECT_NAME})
set(CPACK_PACKAGE_VERSION ${PROJECT_VERSION})
set(CPACK_PACKAGE_VENDOR "C++ Korea")
set(CPACK_PACKAGE_DESCRIPTION "https://github.com/cppkorea/studies")
set(CPACK_RESOURCE_FILE_README ${PROJECT_SOURCE_DIR}/readme.md)
set(CPACK_GENERATOR "ZIP")
include(CPack)