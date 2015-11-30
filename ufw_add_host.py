#!/usr/bin/env python

import sys
from subprocess import check_output, run


def main():
    if (len(sys.argv) != 2):
        error()
    elif (sys.argv[1] == "--help"):
        print_help()
        sys.exit(2)

    add_rule(sys.argv[1])


def add_rule(url):
    host_output = check_output(["host", "-t", "A", url]).decode()
    host_lines = host_output.split('\n')
    ip_list = []

    for line in host_lines:
        try:
            ip = line.split(' ')[3]
        except(IndexError):
            continue
        print(ip)
        ip_list.append(ip)

    for ip in ip_list:
        print(ip)
        # run("ufw allow out from any to ", ip)


def error():
    print("Bad argument(s) or bad url")
    print_help()
    sys.exit(2)


def print_help():
    print("Usage: ufw_addhost.py [url]")

if __name__ == "__main__":
    main()
