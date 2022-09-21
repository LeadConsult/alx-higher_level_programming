#!/usr/bin/python3
def remove_char_at(str, n):
    x = 0
    new_str = ""
    for ch in str:
        if x != n:
            new_str += ch
        x += 1
    return 
