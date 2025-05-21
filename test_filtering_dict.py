import unittest
from filtering_dict import filter_user

class TestFilterUser(unittest.TestCase):
    def test_filter_user(self):
        # Test data
        test_users = [
            {'name': 'Valid User', 'email': 'valid@example.com', 'age': 25},
            {'name': 'Young User', 'email': 'young@example.com', 'age': 17},
            {'name': 'Invalid Email', 'email': 'invalidemail', 'age': 30},
            {'name': 'No Domain', 'email': 'nodomain@', 'age': 20},
            {'name': 'No At Symbol', 'email': 'noatsymbol.com', 'age': 22}
        ]

        # Expected result: users with emails containing '@' and '.' and age >= 18
        expected = [
            {'name': 'Valid User', 'email': 'valid@example.com', 'age': 25}
        ]

        # Run the filter function
        result = filter_user(test_users)

        # Print the result for debugging
        print("Test result:", result)

        # Assert the result matches expected
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
