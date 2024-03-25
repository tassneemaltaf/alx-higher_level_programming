#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0])
    matrix_new = [[0 for x in range(cols)] for y in range(rows)]
    for i in range(0, rows):
        for j in range(0, cols):
            matrix_new[i][j] = matrix[i][j] ** 2

    return matrix_new
