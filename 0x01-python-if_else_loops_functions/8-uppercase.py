#!/usr/bin/python3
def to_uper(char_):
    if ord(char_) >= 97 and ord(char_) <= 122:
        return (ord(char_) - 32)
    else:
        return ord(char_)


def uppercase(str):
    new = ""
    for char_ in str:
        new += "%c" % to_uper(char_)
    print("{:s}".format(new))
