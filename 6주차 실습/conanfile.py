import os
from conans import ConanFile, CMake

class boost_test_conan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = [
        "boost/1.75.0",
        "openssl/1.1.1k",
        "bzip2/1.0.8",
        "catch2/2.13.0"
    ]
    generators = "cmake_find_package"
    default_options = {
        "openssl:shared": True,
        "openssl:no_threads": True,
        "boost:shared": False,
        "boost:bzip2": True,
        "boost:zlib": False,
        "boost:error_code_header_only": True,
        "boost:layout": "versioned"
    }

    def config_options(self):
        if self.settings.os == "Windows":
            self.requires("zlib-ng/2.0.2")
