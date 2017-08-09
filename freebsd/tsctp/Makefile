# New ports collection makefile for: subnetcalc
# Date created:                      27 July 2010
# Whom:                              Thomas Dreibholz <dreibh@iem.uni-due.de>
#
# $FreeBSD: ports/net/subnetcalc/Makefile,v 1.1 2010/08/04 20:00:20 ohauer Exp $
#

PORTNAME=	tsctp
PORTVERSION=	0.5.0
CATEGORIES=	net
MASTER_SITES=	https://www.uni-due.de/~be0001/tsctp/download/ \
		http://www.exp-math.uni-essen.de/~dreibh/tsctp/download/

MAINTAINER=	dreibh@iem.uni-due.de
COMMENT=	SCTP Test Tool

LIB_DEPENDS=

GNU_CONFIGURE=	no
CONFIGURE_ARGS=
USE_GMAKE=	no

LICENSE=	BSD
LICENSE_FILE=	${WRKSRC}/COPYING

PLIST_FILES=	bin/tsctp
MAN8=		tsctp.8

.include <bsd.port.mk>
