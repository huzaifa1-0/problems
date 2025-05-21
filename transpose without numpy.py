import numpy as np

def transpose_matrix(matrix):
    if not matrix or len(matrix[0]) == 0:
        return  []
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

matrix = [[10,20,30],[40,50,10],[10,20,900]]

custom_transpose = transpose_matrix(matrix)
print(custom_transpose)
numpy_transpose = np.transpose(matrix)
print(numpy_transpose)

assert custom_transpose == numpy_transpose.tolist()

