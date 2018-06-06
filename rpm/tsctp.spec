Name: tsctp
Version: 0.6.6
Release: 1
Summary: SCTP test tool
Group: Applications/Internet
License: GPLv3
URL: https://www.uni-due.de/~be0001/tsctp/
Source: https://www.uni-due.de/~be0001/tsctp/download/%{name}-%{version}.tar.gz

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
* Tue Nov 05 2017 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.5.3~rc1
- Created RPM package.
