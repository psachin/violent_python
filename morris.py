#!/usr/bin/env python
"""A (something like)Morris scanner.

Usage:
python morris.py --host localhost --port 21,22,80,37
"""
__author__ = "Sachin"
__email__ = "iclcoolster@gmail.com"
__description__ = "A (something like)Morris scanner."

import argparse
import socket


def connect_target(host, port, buffer_size=200):
    """Try to connect the target host"""
    try:
        conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_socket.connect((host, port))
        reply = conn_socket.recv(buffer_size)
        conn_socket.close()
        return reply.strip()
    except Exception, error:
        return False


def port_scan(host, port):
    """Try to scan ports of host specified"""
    try:
        target = socket.gethostbyname(host)
    except:
        target = socket.gethostbyaddr(host)

    socket.setdefaulttimeout(1)
    reply = connect_target(target, port)
    if reply:
        print '[+] Port %d: %s' % (port, reply)
    else:
        print '[-] No reply from port %d' % port

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", dest='host', help="Host IP address")
    parser.add_argument("--ports", dest='ports', help="Port(s)")
    args = parser.parse_args()

    if args.host is None or args.ports is None:
        parser.print_help()
        exit(0)
    else:
        print "Scan results for %s" % args.host
        for port in args.ports.split(','):
            port_scan(args.host, int(port))
