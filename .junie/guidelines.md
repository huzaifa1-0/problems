# Project Development Guidelines

This document provides guidelines and information for developers working on this project.

## Build/Configuration Instructions

### Dependencies
- Python 3.x
- NumPy (required for the transpose matrix verification)

### Setup
1. Clone the repository
2. Install dependencies:
   ```
   pip install numpy
   ```

## Testing Information

### Running Tests
The project uses Python's built-in `unittest` framework for testing. To run tests:

1. Run a specific test file:
   ```
   python test_filtering_dict.py
   python test_transpose.py
   ```

2. Run all tests (using a test discovery tool like pytest):
   ```
   pytest
   ```
   Note: You'll need to install pytest first with `pip install pytest`

### Adding New Tests
1. Create a new test file with the naming convention `test_*.py`
2. Import the unittest module and the functions/classes you want to test
3. Create a test class that inherits from `unittest.TestCase`
4. Add test methods that start with `test_`
5. Use assertion methods like `assertEqual`, `assertTrue`, etc.

### Example Test
Here's an example of how to create a test for a new function:

```python
import unittest
from your_module import your_function

class TestYourFunction(unittest.TestCase):
    def test_your_function(self):
        # Test data
        input_data = "some input"
        expected_output = "expected result"
        
        # Run the function
        result = your_function(input_data)
        
        # Assert the result matches expected
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
```

## Code Style and Development Guidelines

### Code Style
- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused on a single task

### Project Structure
The project consists of several Python modules:
- `filtering_dict.py`: Contains functions for filtering dictionaries based on specific criteria
- `transpose_without_numpy.py`: Contains functions for matrix operations without using NumPy's built-in functions
- `main.py`: Simple entry point for the application

### Best Practices
1. **Error Handling**: Use try-except blocks for handling potential errors
2. **Input Validation**: Validate inputs to functions to prevent unexpected behavior
3. **Testing**: Write tests for new functionality before implementation (Test-Driven Development)
4. **Documentation**: Document any non-obvious code with comments
5. **Naming Conventions**:
   - Use snake_case for variables and functions
   - Use PascalCase for classes
   - Use UPPER_CASE for constants

### Debugging Tips
- Use print statements or logging to debug issues
- For the transpose function, compare results with NumPy's transpose function
- For the filtering function, check the filter conditions carefully