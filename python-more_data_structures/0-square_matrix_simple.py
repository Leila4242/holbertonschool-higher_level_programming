#!/usr/bin/python3
def kvadrat(x):
    return x ** 2
def square_matrix_simple(matrix=[]):
    new_matrix = map(kvadrat,matrix)
    print(new_matrix)
    print(matrix)
