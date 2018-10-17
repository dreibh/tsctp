# Created by: Thomas Dreibholz <dreibh@iem.uni-due.de>
# $FreeBSD$

PORTNAME=	tsctp
PORTVERSION=	0.7.0
CATEGORIES=	net
MASTER_SITES=	https://www.uni-due.de/~be0001/tsctp/download/

MAINTAINER=	dreibh@iem.uni-due.de
COMMENT=	SCTP Test Tool

LICENSE=        BSD
LICENSE_FILE=   ${WRKSRC}/COPYING

GNU_CONFIGURE=	yes
USES=           cmake
CMAKE_ARGS+=    -DCMAKE_INSTALL_MANDIR=${PREFIX}/man

.include <bsd.port.mk>
