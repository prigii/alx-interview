#!/usr/bin/python3
"""
Rotate an n x n 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]


# Function to print matrix
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
