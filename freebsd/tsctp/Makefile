# Created by: Thomas Dreibholz <thomas.dreibholz@gmail.com>
# $FreeBSD: head/net/tsctp/Makefile 509200 2019-08-18 10:50:13Z pi $

PORTNAME=	tsctp
PORTVERSION=	0.7.10
CATEGORIES=	net
MASTER_SITES=	https://www.nntb.no/~dreibh/tsctp/download/

MAINTAINER=	thomas.dreibholz@gmail.com
COMMENT=	SCTP Test Tool

LICENSE=	BSD
LICENSE_FILE=	${WRKSRC}/COPYING

USES=		tar:xz cmake

PLIST_FILES=	bin/tsctp man/man1/tsctp.1.gz
CMAKE_ARGS+=	-DCMAKE_INSTALL_MANDIR=${PREFIX}/man

.include <bsd.port.mk>
