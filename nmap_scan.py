#!/usr/bin/env python
"""Scanner based on Python-Nmap.

Usage:
python nmap_scan.py --host localhost --ports 21 22 80 37
or
python nmap_scan.py -H localhost -p 21 22 80 37
"""
__author__ = "Sachin"
__email__ = "iclcoolster@gmail.com"
__description__ = "Scanner based on Namp."

import argparse
import nmap


def scan(host, port):
    """Use Namp scanner to scan ports"""
    scanner = nmap.PortScanner()
    scanner.scan(host, str(port))
    state = scanner[host]['tcp'][port]['state']
    return state


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", dest='host',
                        help="Host IP address")
    parser.add_argument("-p", "--ports", nargs="+", dest='ports',
                        type=int, help="Port(s)")
    args = parser.parse_args()

    if args.host is None or args.ports is None:
        parser.print_help()
        exit(0)
    else:
        print "Scan results for %s" % args.host
        for port in args.ports:
            print "Port %d: %s" % (port, scan(args.host, port))
