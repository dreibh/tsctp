<h1 align="center">
 TSCTP<br />
 <span style="font-size: 75%;">An SCTP Test Tool</span><br />
 <a href="https://www.nntb.no/~dreibh/tsctp/">
  <img alt="SCTP Project Logo" src="src/figures/SCTPProject-Logo.svg" width="25%" /><br />
  <span style="font-size: 75%;">https://www.nntb.no/~dreibh/tsctp</span>
 </a>
</h1>


# 💡 What is TSCTP?

TSCTP is an SCTP test tool. Its purpose is to perform basic SCTP
functionality tests to check implementations interoperability and
to verify that the SCTP stack is working.


# 😀 Examples

## Preparations

TSCTP uses the SCTP protocol, i.e., sockets with protocol IPPROTO_SCTP. It may be necessary to allow loading the SCTP kernel module first, if not already enabled. The following code blocks show how to enable it permanently.

### SCTP on Linux

```bash
echo "sctp" | sudo tee /etc/modules-load.d/sctp.conf
if [ -e /etc/modprobe.d/sctp-blacklist.conf ] ; then
   sudo sed -e 's/^blacklist sctp/# blacklist sctp/g' -i /etc/modprobe.d/sctp-blacklist.conf
fi
sudo modprobe sctp
lsmod | grep sctp
```

### SCTP on FreeBSD

```bash
echo 'sctp_load="YES"' | sudo tee --append /boot/loader.conf
sudo kldload sctp
kldstat | grep sctp
```

### SCTP on NetBSD

NetBSD provides SCTP support, but it must be compiled into the kernel.

### SCTP on Solaris

Solaris provides out-of-the-box SCTP support.


## TSCTP Server Mode

Server mode: bind to all IPv4 and IPv6 addresses, listen on port&nbsp;1234.

```bash
tsctp -L :: -L 0.0.0.0 -p 1234
```

## TSCTP Client Mode

* Client mode:
  bind to all IPv4 and IPv6 addresses,
  connect to localhost (127.0.0.1) on port&nbsp;1234,
  send unlimited number of messages of 4096&nbsp;bytes each,
  stop after 10 s.

  ```bash
  tsctp -L :: -L 0.0.0.0 -n 10 -l 1000 -p 1234 127.0.0.1
  ```

* Client mode:
  bind to all IPv4 and IPv6 addresses,
  connect to localhost (127.0.0.1) on port&nbsp;1234,
  send unlimited number of messages of 4096&nbsp;bytes each,
  stop after 10&nbsp;s.

  ```bash
  tsctp -L :: -L 0.0.0.0 -n 0 -T 10 -l 4096 -p 1234 127.0.0.1
  ```


# 📦 Binary Package Installation

Please use the issue tracker at [https://github.com/dreibh/tsctp/issues](https://github.com/dreibh/tsctp/issues) to report bugs and issues!

## Ubuntu Linux

For ready-to-install [Ubuntu Linux](https://ubuntu.com/) packages of TSCTP, see the [Launchpad PPA for Thomas Dreibholz](https://launchpad.net/~dreibh/+archive/ubuntu/ppa/+packages?field.name_filter=tsctp&field.status_filter=published&field.series_filter=)!

```bash
sudo apt-add-repository -sy ppa:dreibh/ppa
sudo apt-get update
sudo apt-get install tsctp
```

## Debian Linux

For ready-to-install [Debian Linux](https://www.debian.org/) packages of TSCTP, see the [Open Build Service PPA for Thomas Dreibholz](https://build.opensuse.org/project/show/home:dreibh)!

Add the PPA repository:

```bash
. /etc/os-release
DISTRIBUTION="Debian_${VERSION_ID:-$([ "${VERSION_CODENAME:-}" = sid ] && echo Unstable || echo Testing)}"
URL="https://download.opensuse.org/repositories/home:/dreibh/${DISTRIBUTION}"
KEY="/etc/apt/keyrings/dreibh-obs.gpg"

curl -fsSL "${URL}/Release.key" | sudo gpg --batch --yes --dearmor -o "${KEY}"
printf "deb [signed-by=%s] %s/ /\ndeb-src [signed-by=%s] %s/ /\n" "${KEY}" "${URL}" "${KEY}" "${URL}" | \
   sudo tee /etc/apt/sources.list.d/obs-dreibh.list
sudo apt update
```

Then, install TSCTP:

```bash
sudo apt-get install tsctp
```

## Fedora Linux

For ready-to-install [Fedora Linux](https://fedoraproject.org/) packages of TSCTP, see the [COPR PPA for Thomas Dreibholz](https://copr.fedorainfracloud.org/coprs/dreibh/ppa/package/tsctp/)!

```bash
sudo dnf copr enable -y dreibh/ppa
sudo dnf install tsctp
```

## OpenSUSE Linux

For ready-to-install [OpenSUSE Linux](https://www.opensuse.org/) packages of TSCTP, see the [Open Build Service PPA for Thomas Dreibholz](https://build.opensuse.org/project/show/home:dreibh)!

Add the PPA repository:

```bash
. /etc/os-release
[[ $VERSION_ID =~ ^[0-9]+\.[0-9]+$ ]] && DISTRIBUTION="${VERSION_ID}" || DISTRIBUTION="${NAME// /_}"
URL="https://download.opensuse.org/repositories/home:/dreibh/${DISTRIBUTION}"
rpm --import "${URL}/repodata/repomd.xml.key"
zypper addrepo -f "${URL}/" dreibh-obs
```

Then, install TSCTP:

```bash
sudo zypper install tsctp
```

## Alpine Linux

For ready-to-install [Alpine Linux](https://alpinelinux.org/) packages of TSCTP, see the [Open Build Service PPA for Thomas Dreibholz](https://build.opensuse.org/project/show/home:dreibh)!

Add the PPA repository:

```bash
DISTRIBUTION="Alpine_Latest_community"
URL="https://download.opensuse.org/repositories/home:/dreibh"
wget -O \
   /etc/apk/keys/home:dreibh@build.opensuse.org-527a4e72.rsa.pub \
   "${URL}/${DISTRIBUTION}/x86_64/home:dreibh%40build.opensuse.org-527a4e72.rsa.pub"
if ! grep -q "^${URL}/${DISTRIBUTION}" /etc/apk/repositories ; then
   echo "${URL}/${DISTRIBUTION}" | sudo tee -a /etc/apk/repositories
fi
```

Then, install TSCTP:

```bash
sudo apk add tsctp
```

## FreeBSD

For ready-to-install [FreeBSD](https://www.freebsd.org/) packages of TSCTP, it is included in the ports collection; see [FreeBSD ports tree index of net/tsctp/](https://cgit.freebsd.org/ports/tree/net/tsctp/)!

```bash
sudo pkg install tsctp
```

Alternatively, to compile it from the ports sources:

```bash
cd /usr/ports/net/tsctp
make
sudo make install
```

## NetBSD

TSCTP supports [NetBSD](https://netbsd.org/). However, there is no NetBSD packaging yet. Just build from sources!

## Solaris (OpenIndiana)

TSCTP supports [Solaris (OpenIndiana)](https://www.openindiana.org/). However, there is no Solaris packaging yet. Just build from sources!

## Homebrew (Linux only)

For the [Homebrew](https://brew.sh/) formula of TSCTP, see [Thomas Dreibholz's Homebrew Tap](https://github.com/dreibh/homebrew-tap)!

Add tap:

```bash
brew tap dreibh/tap
brew trust dreibh/tap
```

Then, install TSCTP:

```bash
brew install tsctp
```


# 💾 Build from Sources

TSCTP is released under the [BSD License](https://opensource.org/license/BSD-3-Clause).

Please use the issue tracker at [https://github.com/dreibh/tsctp/issues](https://github.com/dreibh/tsctp/issues) to report bugs and issues!

## Development Version

The Git repository of the TSCTP sources can be found at [https://github.com/dreibh/tsctp](https://github.com/dreibh/tsctp):

```bash
git clone https://github.com/dreibh/tsctp
cd tsctp
sudo ci/get-dependencies --install
cmake .
make
```

Optionally, for installation to the standard paths (usually under `/usr/local`):

```bash
sudo make install
```

Note: The script [`ci/get-dependencies`](https://github.com/dreibh/tsctp/blob/master/ci/get-dependencies) automatically installs the build dependencies under Debian/Ubuntu Linux, Fedora Linux, OpenSUSE Linux, Alpine Linux, FreeBSD, and Homebrew. For manual handling of the build dependencies, take a look at the packaging configuration files:

* [`debian/control`](https://github.com/dreibh/tsctp/blob/master/debian/control) (Debian/Ubuntu Linux),
* [`tsctp.spec`](https://github.com/dreibh/tsctp/blob/master/rpm/tsctp.spec) (Fedora Linux, OpenSUSE Linux),
* [`APKBUILD`](https://github.com/dreibh/tsctp/blob/master/packaging/APKBUILD) (Alpine Linux),
* [`Makefile`](https://github.com/dreibh/tsctp/blob/master/freebsd/tsctp/Makefile) (FreeBSD), and
* [`tsctp.rb`](https://github.com/dreibh/tsctp/blob/master/packaging/tsctp.rb) (Homebrew).

Contributions:

* Issue tracker: [https://github.com/dreibh/tsctp/issues](https://github.com/dreibh/tsctp/issues).
  Please submit bug reports, issues, questions, etc. in the issue tracker!

* Pull Requests for TSCTP: [https://github.com/dreibh/tsctp/pulls](https://github.com/dreibh/tsctp/pulls).
  Your contributions to TSCTP are always welcome!

* CI build tests of TSCTP: [https://github.com/dreibh/tsctp/actions](https://github.com/dreibh/tsctp/actions).

* Coverity Scan analysis of TSCTP: [https://scan.coverity.com/projects/dreibh-tsctp](https://scan.coverity.com/projects/dreibh-tsctp).

## Release Versions

See [https://www.nntb.no/~dreibh/tsctp/#current-stable-release](https://www.nntb.no/~dreibh/tsctp/#current-stable-release) for the release packages!


# 🔗 Useful Links

* [NetPerfMeter – A TCP/MPTCP/UDP/SCTP/DCCP Network Performance Meter Tool](https://www.nntb.no/~dreibh/netperfmeter/)
* [HiPerConTracer – High-Performance Connectivity Tracer](https://www.nntb.no/~dreibh/hipercontracer/)
* [Dynamic Multi-Homing Setup (DynMHS)](https://www.nntb.no/~dreibh/dynmhs/)
* [SubNetCalc – An IPv4/IPv6 Subnet Calculator](https://www.nntb.no/~dreibh/subnetcalc/)
* [System-Tools – Tools for Basic System Management](https://www.nntb.no/~dreibh/system-tools/)
* [Virtual Machine Image Builder and System Installation Scripts](https://www.nntb.no/~dreibh/vmimage-builder-scripts/)
* [Thomas Dreibholz's SCTP Page](https://www.nntb.no/~dreibh/sctp/)
* [Thomas Dreibholz's Reliable Server Pooling Page](https://www.nntb.no/~dreibh/rserpool/)
* [NorNet – A Real-World, Large-Scale Multi-Homing Testbed](https://www.nntb.no/)
* [NEAT – A New, Evolutive API and Transport-Layer Architecture for the Internet](https://neat.nntb.no/)
* [Michael Tüxen's SCTP Page](https://www.sctp.de/)
* [Lode Coene's SCTP Page](https://web.archive.org/web/20210813064400/http://www.sctp.be/)
* [OpenSS7](https://web.archive.org/web/20210813195936/http://www.openss7.org/)
* [Wireshark](https://www.wireshark.org/)
