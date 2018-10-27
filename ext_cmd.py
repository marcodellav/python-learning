#!/usr/local/bin/python3
import os
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('port_number', help='the port that you want to free up')
port_number = parser.parse_args().port_number

try:

    lsof = subprocess.run(
        ['lsof', '-n', "-i4TCP:%s" % port_number],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
except subprocess.CalledProcessError:
    print(f"No process listening on port {port_number}")
else:
    for line in lsof.stdout.splitlines():
        line = line.split()
        print(line[-1])
