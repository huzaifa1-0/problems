import numpy as np

class imagematrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def rotateclockwise(self):
        n = self.n
        rotated = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
