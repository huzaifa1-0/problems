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
                rotated[j][n-1-i] = self.matrix[i][j]
        self.matrix = rotated

    def horizontalflip(self):
        n = self.n
        flip = [[0]^n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                flip[i][j] = self.matrix[i][n-1-j]
        self.matrix = flip

    def getmatirx(self):
        return self.matrix



inputmatrix = [
    [8,9,0,1,2,3],
    [1,5,7,4,3,2]
]

image = imagematrix(inputmatrix)
print(inputmatrix)
print(image.getmatirx())


image.rotateclockwise()
print(image.getmatirx())

image.horizontalflip()
print(image.getmatirx)
