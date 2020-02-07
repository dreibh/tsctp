# Created by: Thomas Dreibholz <dreibh@iem.uni-due.de>
# $FreeBSD: head/net/tsctp/Makefile 509200 2019-08-18 10:50:13Z pi $

PORTNAME=	tsctp
PORTVERSION=	0.7.4~rc3
CATEGORIES=	net
MASTER_SITES=	https://www.uni-due.de/~be0001/tsctp/download/

MAINTAINER=	dreibh@iem.uni-due.de
COMMENT=	SCTP Test Tool

LICENSE=	BSD
LICENSE_FILE=	${WRKSRC}/COPYING

USES=		tar:xz cmake

PLIST_FILES=	bin/tsctp man/man1/tsctp.1.gz
CMAKE_ARGS+=	-DCMAKE_INSTALL_MANDIR=${PREFIX}/man

.include <bsd.port.mk>
