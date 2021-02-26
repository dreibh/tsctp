Name: tsctp
Version: 0.7.5
Release: 1
Summary: SCTP test tool
Group: Applications/Internet
License: GPL-3+
URL: https://www.uni-due.de/~be0001/tsctp/
Source: https://www.uni-due.de/~be0001/tsctp/download/%{name}-%{version}.tar.xz

AutoReqProv: on
BuildRequires: cmake
BuildRequires: gcc
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
%cmake -DCMAKE_INSTALL_PREFIX=/usr .
%cmake_build

%install
%cmake_install

%files
%{_bindir}/tsctp
%{_mandir}/man1/tsctp.1.gz

%doc

%changelog
* Fri Nov 13 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.7.5
- New upstream release.
* Fri Feb 07 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.7.4
- New upstream release.
* Wed Aug 07 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.7.3
- New upstream release.
* Fri Jul 26 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.7.2
- New upstream release.
* Tue May 21 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.7.1
- New upstream release.
* Sun Nov 05 2017 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.5.3~rc1
- Created RPM package.
