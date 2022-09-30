#!/usr/bin/python3
def best_score(a_dictionary):

    biggest_value = 0
    biggest_key = None
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > biggest_value:
                biggest_value = value
                biggest_key = key
    return biggest_key
