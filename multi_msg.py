#!/usr/local/bin/python3

message = input('what is the message? ')
count = int(input('how many times do you want to repeat it? '))


def multi_msg(message, count):
    while count > 0:
        print(message)
        count -= 1


multi_msg(message, count)
