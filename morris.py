#!/usr/bin/env python
"""A (something like)Morris scanner.

Usage:
python morris.py --host localhost --ports 21 22 80 37
or
python morris.py -H localhost -p 21 22 80 37
"""
__author__ = "Sachin"
__email__ = "iclcoolster@gmail.com"
__description__ = "A (something like)Morris scanner."

import argparse
import socket
import threading


def connect_target(host, port, buffer_size=200):
    """Try to connect the target host:port"""
    threadlock = threading.Lock()
    try:
        conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_socket.connect((host, port))
        reply = conn_socket.recv(buffer_size)
        threadlock.acquire()
        print '[+] Port %d: %s' % (port, reply.strip())
    except Exception, err:
        threadlock.acquire()
        print '[-] Port %d %s' % (port, err)
    finally:
        threadlock.release()
        conn_socket.close()


def port_scan(host, ports, timeout=1):
    """Try to scan ports of host specified"""
    try:
        target = socket.gethostbyname(host)
    except:
        target = socket.gethostbyaddr(host)
    socket.setdefaulttimeout(timeout)

    threads = []
    for port in ports:
        thread = threading.Thread(target=connect_target, args=(target, port))
        thread.start()


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
        port_scan(args.host, args.ports)
