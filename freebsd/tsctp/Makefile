PORTNAME=	tsctp
PORTVERSION=	0.7.11
CATEGORIES=	net
MASTER_SITES=	https://www.nntb.no/~dreibh/tsctp/download/

MAINTAINER=	thomas.dreibholz@gmail.com
COMMENT=	SCTP Test Tool
WWW=		https://www.nntb.no/~dreibh/tsctp/

LICENSE=	BSD2CLAUSE
LICENSE_FILE=	${WRKSRC}/COPYING-BSD

USES=		tar:xz cmake

CMAKE_ARGS+=	-DCMAKE_INSTALL_MANDIR=${PREFIX}/man

PLIST_FILES=	bin/tsctp man/man1/tsctp.1.gz

.include <bsd.port.mk>
