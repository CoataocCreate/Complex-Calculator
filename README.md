# Complex Calculator

This Python script implements a complex calculator capable of performing various mathematical operations, including basic arithmetic, trigonometric functions, logarithms, factorial calculation, permutations, combinations, and more.

## Features

- **Basic Arithmetic Operations:** Addition, subtraction, multiplication, and division.
- **Exponentiation and Square Root:** Calculate powers and square roots of numbers.
- **Logarithms:** Compute logarithms with a specified base.
- **Trigonometric Functions:** Sine, cosine, and tangent of angles in radians.
- **Factorial:** Compute the factorial of a non-negative integer.
- **Permutation and Combination:** Calculate permutations and combinations of objects.
- **Absolute Value:** Get the absolute value of a number.

## Usage

1. Clone the repository or download the Python script `complex_calculator.py`.
2. Import the `ComplexCalculator` class into your Python script.
3. Create an instance of the `ComplexCalculator` class.
4. Use the instance to call the desired mathematical operations with appropriate arguments.

### Examples:

```python
from complex_calculator import ComplexCalculator
import math

# Create an instance of ComplexCalculator
calculator = ComplexCalculator()

# Basic arithmetic operations
print("Addition:", calculator.add(5, 3))
print("Subtraction:", calculator.subtract(5, 3))
print("Multiplication:", calculator.multiply(5, 3))
print("Division:", calculator.divide(5, 3))

# Exponentiation and square root
print("Power:", calculator.power(5, 3))
print("Square Root:", calculator.sqrt(25))

# Logarithm
print("Logarithm:", calculator.log(100))
print("Custom Base Logarithm:", calculator.log(100, 2))

# Trigonometric functions
print("Sine:", calculator.sin(math.pi / 2))
print("Cosine:", calculator.cos(math.pi))
print("Tangent:", calculator.tan(math.pi / 4))

# Factorial
print("Factorial:", calculator.factorial(5))

# Permutation and Combination
print("Permutation:", calculator.permutation(5, 3))
print("Combination:", calculator.combination(5, 3))

# Absolute value
print("Absolute Value:", calculator.absolute(-10))
