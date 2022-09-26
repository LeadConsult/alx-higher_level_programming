#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if y != 0:
                print(" ", end='')
            print("{:d}".format(matrix[x][y]), end='')
        print()
