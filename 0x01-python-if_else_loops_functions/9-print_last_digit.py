#!/usr/bin/python3
def print_last_digit(num):
    if num >= 0:
        last_digit = num % 10
    else:
        last_digit = num % -10
        last_digit *= -1

    print("{:d}".format(last_digit), end='')
    return (last_digit)
