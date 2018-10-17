#############################################################################
# PROGRAMS
#############################################################################

ADD_EXECUTABLE(tsctp tsctp.c)
TARGET_LINK_LIBRARIES(tsctp ${SCTP_LIB} "${CMAKE_THREAD_LIBS_INIT}")
INSTALL(TARGETS tsctp RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})
INSTALL(FILES tsctp.1 DESTINATION ${CMAKE_INSTALL_MANDIR}/man1)
