Name: tsctp
Version: 0.7.13~rc0
Release: 1
Summary: SCTP test tool
Group: Applications/Internet
License: BSD-3-clause
URL: https://www.nntb.no/~dreibh/tsctp/
Source: https://www.nntb.no/~dreibh/tsctp/download/%{name}-%{version}.tar.xz

AutoReqProv: on
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: lksctp-tools-devel
Recommends: hipercontracer
Recommends: iproute2
Recommends: netperfmeter
Recommends: rsplib-tools
Recommends: subnetcalc
Recommends: traceroute
Recommends: wireshark-cli
Suggests: dynmhs
Suggests: td-system-info
Suggests: traceroute
BuildRoot: %{_tmppath}/%{name}-%{version}-build


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
%{_datadir}/bash-completion/completions/tsctp
%{_mandir}/man1/tsctp.1.gz

%doc

%changelog
* Sat Feb 10 2024 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 0.7.12
- New upstream release.
* Wed Dec 06 2023 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 0.7.11
- New upstream release.
* Thu Jan 19 2023 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 0.7.10
- New upstream release.
* Sun Sep 11 2022 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.7.9
- New upstream release.
* Fri May 13 2022 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.7.8
- New upstream release.
* Thu Feb 17 2022 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.7.7
- New upstream release.
* Fri Nov 12 2021 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.7.6
- New upstream release.
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
