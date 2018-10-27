#!/usr/local/bin/python3

'''Write a script that prompts the user for:
A file_name where it should write the content.
The content that should go in the file. The script should keep accepting lines of text until the user enters an empty line.
After the user enters an empty line, write all of the lines to the file and end the script.'''

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the file to write to')
args = parser.parse_args()
print(args)

os.chdir('/home/marcodv/Documents/Python_Stuff')

file_line = str('can\'t be empty')
file_buffer = str('')

new_file = open(args.filename, 'a')
while file_line != '':
    file_line = input('please type a line to be appended to the file: ')
    file_buffer += (file_line + '\n')
new_file.write(str(file_buffer))
