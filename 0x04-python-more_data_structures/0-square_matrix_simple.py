#!/usr/bin/python3
def square_matrix_simple(matrix):
    for i in range (0, len(matrix[0])):
        for j in range (0, len(matrix[0])):
            matrix2[i][j] = matrix[i][j]*matrix[i][j]
        
    return(matrix2)
