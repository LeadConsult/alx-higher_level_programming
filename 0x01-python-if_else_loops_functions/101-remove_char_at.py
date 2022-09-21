#!/usr/bin/python3
def remove_char_at(str, n):
    x = ""
    for i in range(len(str)):
        if i != n:
            x = x + str[i]
    return (x)
