CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
PROJECT(tsctp)

SET(BUILD_MAJOR "0")
SET(BUILD_MINOR "7")
SET(BUILD_PATCH "0~rc1")
SET(BUILD_VERSION ${BUILD_MAJOR}.${BUILD_MINOR}.${BUILD_PATCH})


#############################################################################
# INSTALLATION_DIRECTORIES
#############################################################################

SET(CMAKE_INSTALL_BINDIR        "bin"       CACHE PATH "user executables [PREFIX/bin]")
SET(CMAKE_INSTALL_SBINDIR       "sbin"      CACHE PATH "system admin executables [EPREFIX/sbin]")
SET(CMAKE_INSTALL_DATADIR       "share"     CACHE PATH "read-only architecture-independent data [PREFIX/share]")
SET(CMAKE_INSTALL_SYSCONFDIR    "etc"       CACHE PATH "read-only single-machine data [PREFIX/etc]")
SET(CMAKE_INSTALL_LOCALSTATEDIR "var"       CACHE PATH "modifiable single-machine data [PREFIX/var]")
SET(CMAKE_INSTALL_LIBDIR        "lib"       CACHE PATH "object code libraries [PREFIX/lib]")
SET(CMAKE_INSTALL_INCLUDEDIR    "include"   CACHE PATH "read-only includes [PREFIX/include]")
SET(CMAKE_INSTALL_MANDIR        "share/man" CACHE PATH "man documentation [PREFIX/share/man]")


#############################################################################
# PACKAGING
#############################################################################

SET(CPACK_SOURCE_GENERATOR "TGZ")
SET(CPACK_SOURCE_PACKAGE_FILE_NAME
   "${CMAKE_PROJECT_NAME}-${BUILD_MAJOR}.${BUILD_MINOR}.${BUILD_PATCH}")
SET(CPACK_SOURCE_IGNORE_FILES
   "${PROJECT_SOURCE_DIR}/${CMAKE_PROJECT_NAME}-*;${PROJECT_SOURCE_DIR}/${CMAKE_PROJECT_NAME}_*;/build/;/.git/;/config.log;/CMakeFiles/;CMakeCache.txt$;.cmake$;.tar.gz$;/_CPack_Packages;/Makefile$;~$;/build-deb;/clean-deb;/filter-empty-entries;/make-symbols;/make-ppa;/make-deb;/debian.conf;/make-rpm;/rpm.conf;${CPACK_SOURCE_IGNORE_FILES}")
INCLUDE(CPack)

ADD_CUSTOM_TARGET(dist COMMAND ${CMAKE_MAKE_PROGRAM} clean package_source)


INCLUDE(CheckIncludeFile)
INCLUDE(CheckStructHasMember)


#############################################################################
# OS DEPENDENT
#############################################################################

IF (${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    MESSAGE(STATUS ${CMAKE_SYSTEM_NAME} " supported")
    FIND_LIBRARY(SCTP_LIB sctp)

ELSEIF (${CMAKE_SYSTEM_NAME} MATCHES "FreeBSD")
    MESSAGE(STATUS ${CMAKE_SYSTEM_NAME} " supported")
    SET(CMAKE_REQUIRED_INCLUDES "/usr/local/include" "/usr/include")
    SET(CMAKE_LIBRARY_PATH "/usr/local/lib")
    INCLUDE_DIRECTORIES("/usr/local/include")

ELSEIF (${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    MESSAGE(STATUS ${CMAKE_SYSTEM_NAME} " supported")
    SET(CMAKE_REQUIRED_INCLUDES "/usr/local/include" "/usr/include" "/usr/local/opt/openssl/include")
    SET(CMAKE_LIBRARY_PATH "/usr/local/lib")
    INCLUDE_DIRECTORIES("/usr/local/include" "/usr/local/opt/openssl/include")

ELSEIF (${CMAKE_SYSTEM_NAME} MATCHES "NetBSD")
    MESSAGE(STATUS ${CMAKE_SYSTEM_NAME} " supported")
    LIST(APPEND neat_headers neat_bsd.h)
    LIST(APPEND neat_sources neat_bsd.c)
    SET(CMAKE_REQUIRED_INCLUDES "/usr/pkg/include" "/usr/include" "/usr/local/include")
    SET(CMAKE_LIBRARY_PATH "/usr/local/lib")
    INCLUDE_DIRECTORIES("/usr/pkg/include" "/usr/local/include")

ELSEIF (${CMAKE_SYSTEM_NAME} MATCHES "NetBSD")
    MESSAGE(STATUS ${CMAKE_SYSTEM_NAME} " supported")

ELSE()
    MESSAGE(FATAL_ERROR ${CMAKE_SYSTEM_NAME} " not supported (yet?)")

ENDIF()


#############################################################################
# CHECK STRUCT MEMBERS
#############################################################################

CHECK_STRUCT_HAS_MEMBER("struct sockaddr" "sa_len" "sys/types.h;sys/socket.h" HAVE_SA_LEN)
IF (HAVE_SA_LEN)
    MESSAGE(STATUS "HAVE_SA_LEN")
    ADD_DEFINITIONS(-DHAVE_SA_LEN)
ENDIF()

CHECK_STRUCT_HAS_MEMBER("struct sockaddr_in" "sin_len" "sys/types.h;netinet/in.h" HAVE_SIN_LEN)
IF (HAVE_SIN_LEN)
    MESSAGE(STATUS "HAVE_SIN_LEN")
    ADD_DEFINITIONS(-DHAVE_SIN_LEN)
ENDIF()

CHECK_STRUCT_HAS_MEMBER("struct sockaddr_in6" "sin6_len" "sys/types.h;netinet/in.h" HAVE_SIN6_LEN)
IF (HAVE_SIN6_LEN)
    MESSAGE(STATUS "HAVE_SIN6_LEN")
    ADD_DEFINITIONS(-DHAVE_SIN6_LEN)
ENDIF()

CHECK_STRUCT_HAS_MEMBER("struct sockaddr_storage" "ss_len" "sys/types.h;sys/socket.h" HAVE_SS_LEN)
IF (HAVE_SS_LEN)
    MESSAGE(STATUS "HAVE_SS_LEN")
    ADD_DEFINITIONS(-DHAVE_SS_LEN)
ENDIF()


#############################################################################
# CHECK OPTIONS
#############################################################################

# Debug build type as default
IF (NOT CMAKE_BUILD_TYPE)
    MESSAGE(STATUS "No build type selected, using DEBUG")
    SET(CMAKE_BUILD_TYPE "DEBUG")
    # _FORTIFY_SOURCE requires compiling with optimization
    SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O")
ENDIF()


#############################################################################
# REQUIREMENTS
#############################################################################

# ====== Threads ============================================================
FIND_PACKAGE(Threads REQUIRED)

# ====== Kernel SCTP ========================================================
CHECK_INCLUDE_FILE(netinet/sctp.h HAVE_NETINET_SCTP_H)
IF (HAVE_NETINET_SCTP_H)
   SET(SCTP_INCLUDE "netinet/sctp.h")
   ADD_DEFINITIONS(-DHAVE_KERNEL_SCTP -DHAVE_NETINET_SCTP_H)
   IF (${CMAKE_SYSTEM_NAME} MATCHES "Linux")
      FIND_LIBRARY(SCTP_LIB sctp REQUIRED)
   ELSE()
      FIND_LIBRARY(SCTP_LIB sctp)
   ENDIF()
   IF (SCTP_LIB)
      SET(CMAKE_REQUIRED_LIBRARIES ${CMAKE_REQUIRED_LIBRARIES} ${SCTP_LIB})
   ELSE()
      SET(SCTP_LIB "")
   ENDIF()
ENDIF()


#############################################################################
# COMPILER FLAGS
#############################################################################

SET(CMAKE_C_FLAGS   "${CMAKE_C_FLAGS}   -Wall")

IF (CMAKE_BUILD_TYPE MATCHES DEBUG)
    MESSAGE(STATUS "Building in DEBUG mode")
    # _FORTIFY_SOURCE requires compiling with optimization
    SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O")
ENDIF()


#############################################################################
# SUBDIRECTORIES
#############################################################################

ADD_SUBDIRECTORY(src)
