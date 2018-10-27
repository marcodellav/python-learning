#!/usr/local/bin/python3.6

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_name', help='the file to read from')
parser.add_argument('line_number', help='the line number in the file to be read')
args = parser.parse_args()
# print(args)

try:
    f = open(args.file_name)
except FileNotFoundError as err:
    print(f"Error: {err}")

else:
    tot_lines = 0
    lines = f.readlines()
    for line in lines:
        tot_lines += 1
    print(f"the total amount of lines in the file is: {tot_lines}")
    if int(args.line_number) > tot_lines:
        print("The line number of the line you want to print is higher than the total number of lines in the file")
    else:
        print (f"the line you selected is: {lines[int(args.line_number)]}")
