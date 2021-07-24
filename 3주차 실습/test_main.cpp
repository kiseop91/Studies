#define CATCH_CONFIG_FAST_COMPILE
#define CATCH_CONFIG_RUNNER
#include <catch2/catch.hpp>
#if defined(WIN32)
#include <winsock2.h>
#include <ws2tcpip.h>
#else
#include <netdb.h>
#include <sys/socket.h>
#include <sys/types.h>
#endif

int main(int argc, char *argv[]) {
  Catch::Session s{};
  return s.run(argc, argv);
}

TEST_CASE("Test, test")
{
  REQUIRE(true);
}