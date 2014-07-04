Name: tsctp
Version: 0.6.0~rc1.1
Release: 1
Summary: SCTP test tool
Group: Applications/Internet
License: GPLv3
URL: http://www.iem.uni-due.de/~dreibh/tsctp/
Source: http://www.iem.uni-due.de/~dreibh/tsctp/download/%{name}-%{version}.tar.gz

AutoReqProv: on
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: lksctp-tools-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-build

%define _unpackaged_files_terminate_build 0

%description
 TSCTP is an SCTP test tool. Its purpose is to perform basic SCTP
 functionality tests to check implementations interoperability and
 to verify that the SCTP stack is working.

%prep
%setup -q

%build
autoreconf -if

%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%{_bindir}/tsctp
%{_datadir}/man/man1/tsctp.1.gz

%doc

%changelog
* Tue Nov 05 2013 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.5.3~rc1
- Created RPM package.
