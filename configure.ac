AC_INIT([TSCTP], [0.6.0~rc1.1], [dreib@iem.uni-due.de])
AM_INIT_AUTOMAKE
AC_CANONICAL_HOST
AC_PREFIX_DEFAULT(/usr/local)
if test "x$prefix" = "xNONE"; then
  prefix=$ac_default_prefix
  ac_configure_args="$ac_configure_args --prefix $prefix"
fi

AC_PROG_CC

if test "$GCC" = "yes"; then
  CFLAGS="$CFLAGS -g -Wall"
fi

AC_CANONICAL_HOST

case $host_os in
solaris*)
  CFLAGS="$CFLAGS -D_XPG4_2 -D__EXTENSIONS__"
  ;;
linux*)
  CFLAGS="$CFLAGS -DLINUX"
  ;;
esac

AC_CHECK_TYPE(size_t)
AC_CHECK_TYPE(ssize_t)

AC_CHECK_FUNC([socket], :, [AC_CHECK_LIB([socket], [socket])])
AC_CHECK_FUNCS(inet_addr, , AC_CHECK_LIB(nsl, inet_addr))
AC_CHECK_FUNCS(sctp_recvmsg, , AC_CHECK_LIB(sctp, sctp_recvmsg))
AC_CHECK_LIB(pthread,pthread_create)

AC_CHECK_HEADERS(sys/types.h)
AC_CHECK_MEMBER(struct sockaddr_in.sin_len,
                AC_DEFINE(HAVE_SIN_LEN, 1, [Define this if your IPv4 has sin_len in sockaddr_in struct.]),,
                [#ifdef HAVE_SYS_TYPES_H
                 #include <sys/types.h>
                 #endif
                 #include <netinet/in.h>])

AC_MSG_CHECKING(for socklen_t)
AC_TRY_COMPILE([#ifdef HAVE_SYS_TYPES_H
                #include <sys/types.h>
                #endif
                #include <sys/socket.h>],
               [socklen_t x = 1; return 0;],
               [AC_MSG_RESULT(yes)],
               [AC_MSG_RESULT(int)
                AC_DEFINE(socklen_t, int, [Define a type for socklen_t.])])

AC_OUTPUT(Makefile)
