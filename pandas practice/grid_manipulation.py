import numpy as np


class ImageMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def rotate_90_clockwise(self):

        n = self.n
        rotated = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated[j][n - 1 - i] = self.matrix[i][j]
        self.matrix = rotated

    def flip_horizontal(self):

        n = self.n
        flipped = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                flipped[i][j] = self.matrix[i][n - 1 - j]
        self.matrix = flipped

    def get_matrix(self):
        return self.matrix



input_matrix = [
    [1, 2],
    [3, 4]
]

image = ImageMatrix(input_matrix)
print("Original Matrix:")
print(image.get_matrix())

image.rotate_90_clockwise()
print("\nAfter 90 degree rotation clockwise:")
print(image.get_matrix())

image.flip_horizontal()
print("\nAfter horizontal flip:")
print(image.get_matrix())


np_matrix = np.array(input_matrix)
rotated_np = np.rot90(np_matrix, -1)
flipped_np = np.fliplr(rotated_np)

print("\nNumPy rotation:")
print(rotated_np)

print("\nNumPy flip:")
print(flipped_np)
