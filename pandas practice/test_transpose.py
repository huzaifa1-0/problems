import unittest
from transpose_without_numpy import transpose_matrix

class TestTransposeMatrix(unittest.TestCase):
    def test_transpose_matrix(self):
        # Test case 1: Regular matrix
        matrix = [[1, 2, 3], [4, 5, 6]]
        expected = [[1, 4], [2, 5], [3, 6]]
        self.assertEqual(transpose_matrix(matrix), expected)
        
        # Test case 2: Square matrix
        matrix = [[1, 2], [3, 4]]
        expected = [[1, 3], [2, 4]]
        self.assertEqual(transpose_matrix(matrix), expected)
        
        # Test case 3: Empty matrix
        matrix = []
        expected = []
        self.assertEqual(transpose_matrix(matrix), expected)
        
        # Test case 4: Matrix with empty row
        matrix = [[]]
        expected = []
        self.assertEqual(transpose_matrix(matrix), expected)

if __name__ == '__main__':
    unittest.main()