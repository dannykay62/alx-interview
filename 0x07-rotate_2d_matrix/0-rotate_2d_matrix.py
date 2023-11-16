#!/usr/bin/python3
"""rotate a 2D matrix of n x n, 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """rotate a 2D matrix"""
    n = len(matrix)
    order = []

    for i in range(n):
        for j in range(n - 1, -1, -1):
            order.append(matrix[j][i])

    for i in range(n):
        for j in range(n):
            matrix[i][j] = order.pop(0)
