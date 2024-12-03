# TSCTP
An SCTP test tool

## Description

TSCTP is an SCTP test tool. Its purpose is to perform basic SCTP
functionality tests to check implementations interoperability and
to verify that the SCTP stack is working.

See the manpage of tsctp for details!

## Usage Examples

### Notes

For TSCTP to work, the kernel needs to support SCTP, i.e. sockets with protocol IPPROTO_SCTP. In most cases, this means to load the SCTP kernel module.
#### Linux
```
echo "sctp" >/etc/modules-load.d/sctp.conf
```
Then, reboot to load the module.
Note: Ensure that the SCTP module is not blacklisted
(e.g. /etc/modprobe.d/sctp-blacklist.conf in Fedora Linux)!

#### FreeBSD
```
echo 'sctp_load="YES"' >>/boot/loader.conf
```
Then, reboot to load the module.

### Run TSCTP in server mode, listen for incoming connections
```
tsctp -l :: -l 0.0.0.0 -p 1234
```
Server mode: bind to all IPv4 and IPv6 addresses, listen on port 1234.

### Run TSCTP in client mode, connect to server and send messages

```
tsctp -l :: -l 0.0.0.0 -p 1234 -n 10 -l 1000 127.0.0.1
```
Client mode:
bind to all IPv4 and IPv6 addresses,
connect to localhost (127.0.0.1) on port 1234,
send unlimited number of messages of 4096 bytes each,
stop after 10 s.

```
tsctp -l :: -l 0.0.0.0 -p 1234 -n 0 -T 10 -l 4096 127.0.0.1
```
Client mode:
bind to all IPv4 and IPv6 addresses,
connect to localhost (127.0.0.1) on port 1234,
send unlimited number of messages of 4096 bytes each,
stop after 10 s.


## Binary Package Installation

Please use the issue tracker at https://github.com/dreibh/tsctp/issues to report bugs and issues!

### Ubuntu Linux

For ready-to-install Ubuntu Linux packages of TSCTP, see Launchpad PPA for Thomas Dreibholz!

```
sudo apt-add-repository -sy ppa:dreibh/ppa
sudo apt-get update
sudo apt-get install tsctp
```

### Fedora Linux

For ready-to-install Fedora Linux packages of TSCTP, see COPR PPA for Thomas Dreibholz!

```
sudo dnf copr enable -y dreibh/ppa
sudo dnf install tsctp
```

### FreeBSD

For ready-to-install FreeBSD packages of TSCTP, it is included in the ports collection, see Index of /head/net/tsctp/!

   pkg install tsctp

Alternatively, to compile it from the ports sources:

```
cd /usr/ports/net/tsctp
make
make install
```

## Sources Download

TSCTP is released under the GNU General Public Licence (GPL).

Please use the issue tracker at https://github.com/dreibh/tsctp/issues to report bugs and issues!

### Development Version

The Git repository of the TSCTP sources can be found at https://github.com/dreibh/tsctp:

- Issue tracker: https://github.com/dreibh/tsctp/issues.
  Please submit bug reports, issues, questions, etc. in the issue tracker!

- Pull Requests for TSCTP: https://github.com/dreibh/tsctp/pulls.
  Your contributions to TSCTP are always welcome!

- CI build tests of TSCTP: https://github.com/dreibh/tsctp/actions.

- Coverity Scan analysis of TSCTP: https://scan.coverity.com/projects/dreibh-tsctp.

### Current Stable Release

See https://www.nntb.no/~dreibh/tsctp/#Download!
