<h1 align="center">
 TSCTP<br />
 <span style="font-size:75%">An SCTP Test Tool</span><br />
 <img width="25%" src="https://www.nntb.no/~dreibh/sctp/images/SCTPProject.svg" alt="The SCTP Project" />
</h1>


# 💡 What is TSCTP?

TSCTP is an SCTP test tool. Its purpose is to perform basic SCTP
functionality tests to check implementations interoperability and
to verify that the SCTP stack is working.


# 😀 Examples

## Preparations

TSCTP uses the SCTP protocol, i.e. sockets with protocol IPPROTO_SCTP. It may be necessary to allow loading the SCTP kernel module first, if not already enabled. The following code blocks show how to enable it permanently.

### SCTP on Linux

<pre>
echo "sctp" | sudo tee /etc/modules-load.d/sctp.conf
if [ -e /etc/modprobe.d/sctp-blacklist.conf ] ; then
   sudo sed -e 's/^blacklist sctp/# blacklist sctp/g' -i /etc/modprobe.d/sctp-blacklist.conf
fi
sudo modprobe sctp
lsmod | grep sctp
</pre>

### SCTP on FreeBSD

<pre>
echo 'sctp_load="YES"' | sudo tee --append /boot/loader.conf
sudo kldload sctp
kldstat | grep sctp
</pre>

## TSCTP Server Mode

Server mode: bind to all IPv4 and IPv6 addresses, listen on port&nbsp;1234.

<pre>
tsctp -l :: -l 0.0.0.0 -p 1234
</pre>

## TSCTP Client Mode

* Client mode:
  bind to all IPv4 and IPv6 addresses,
  connect to localhost (127.0.0.1) on port&nbsp;1234,
  send unlimited number of messages of 4096&nbsp;bytes each,
  stop after 10 s.

  <pre>
  tsctp -l :: -l 0.0.0.0 -p 1234 -n 10 -l 1000 127.0.0.1
  </pre>

* Client mode:
  bind to all IPv4 and IPv6 addresses,
  connect to localhost (127.0.0.1) on port&nbsp;1234,
  send unlimited number of messages of 4096&nbsp;bytes each,
  stop after 10&nbsp;s.

  <pre>
  tsctp -l :: -l 0.0.0.0 -p 1234 -n 0 -T 10 -l 4096 127.0.0.1
  </pre>


# 📦 Binary Package Installation

Please use the issue tracker at [https://github.com/dreibh/tsctp/issues](https://github.com/dreibh/tsctp/issues) to report bugs and issues!

## Ubuntu Linux

For ready-to-install Ubuntu Linux packages of TSCTP, see [Launchpad PPA for Thomas Dreibholz](https://launchpad.net/~dreibh/+archive/ubuntu/ppa/+packages?field.name_filter=tsctp&field.status_filter=published&field.series_filter=)!

<pre>
sudo apt-add-repository -sy ppa:dreibh/ppa
sudo apt-get update
sudo apt-get install tsctp
</pre>

## Fedora Linux

For ready-to-install Fedora Linux packages of TSCTP, see [COPR PPA for Thomas Dreibholz](https://copr.fedorainfracloud.org/coprs/dreibh/ppa/package/tsctp/)!

<pre>
sudo dnf copr enable -y dreibh/ppa
sudo dnf install tsctp
</pre>

## FreeBSD

For ready-to-install FreeBSD packages of TSCTP, it is included in the ports collection, see [FreeBSD ports tree index of benchmarks/tsctp/](https://cgit.freebsd.org/ports/tree/benchmarks/tsctp/)!

<pre>
pkg install tsctp
</pre>

Alternatively, to compile it from the ports sources:

<pre>
cd /usr/ports/benchmarks/tsctp
make
make install
</pre>


# 💾 Build from Sources

TSCTP is released under the [BSD License](https://opensource.org/licenses/BSD-3-Clause).

Please use the issue tracker at [https://github.com/dreibh/tsctp/issues](https://github.com/dreibh/tsctp/issues) to report bugs and issues!

## Development Version

The Git repository of the TSCTP sources can be found at [https://github.com/dreibh/tsctp](https://github.com/dreibh/tsctp):

<pre>
git clone https://github.com/dreibh/tsctp
cd tsctp
cmake .
make
</pre>

Contributions:

- Issue tracker: [https://github.com/dreibh/tsctp/issues](https://github.com/dreibh/tsctp/issues).
  Please submit bug reports, issues, questions, etc. in the issue tracker!

- Pull Requests for TSCTP: [https://github.com/dreibh/tsctp/pulls](https://github.com/dreibh/tsctp/pulls).
  Your contributions to TSCTP are always welcome!

- CI build tests of TSCTP: [https://github.com/dreibh/tsctp/actions](https://github.com/dreibh/tsctp/actions).

- Coverity Scan analysis of TSCTP: [https://scan.coverity.com/projects/dreibh-tsctp](https://scan.coverity.com/projects/dreibh-tsctp).

## Stable Versions

See [https://www.nntb.no/~dreibh/tsctp/#current-stable-release](https://www.nntb.no/~dreibh/tsctp/#current-stable-release) for the stable release packages!


# 🔗 Useful Links

* [NetPerfMeter – A TCP/MPTCP/UDP/SCTP/DCCP Network Performance Meter Tool](https://www.nntb.no/~dreibh/netperfmeter/index.html)
* [HiPerConTracer – High-Performance Connectivity Tracer](https://www.nntb.no/~dreibh/hipercontracer/index.html)
* [SubNetCalc – An IPv4/IPv6 Subnet Calculator](https://www.nntb.no/~dreibh/subnetcalc/index.html)
* [Thomas Dreibholz's SCTP Page](https://www.nntb.no/~dreibh/sctp/index.html)
* [Thomas Dreibholz's Reliable Server Pooling Page](https://www.nntb.no/~dreibh/rserpool/index.html)
* [NorNet – A Real-World, Large-Scale Multi-Homing Testbed](https://www.nntb.no/)
* [NEAT – A New, Evolutive API and Transport-Layer Architecture for the Internet](https://neat.nntb.no/)
* [Michael Tüxen's SCTP Page](https://www.sctp.de/)
* [Lode Coene's SCTP Page](https://web.archive.org/web/20210813064400/http://www.sctp.be/)
* [OpenSS7](https://web.archive.org/web/20210813195936/http://www.openss7.org/)
* [Wireshark](https://www.wireshark.org/)
