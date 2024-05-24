import math

class ComplexCalculator:
    def __init__(self):
        pass

    def add(self, x, y):
        """Addition operation: Returns the sum of two numbers."""
        return x + y

    def subtract(self, x, y):
        """Subtraction operation: Returns the difference between two numbers."""
        return x - y

    def multiply(self, x, y):
        """Multiplication operation: Returns the product of two numbers."""
        return x * y

    def divide(self, x, y):
        """Division operation: Returns the quotient of two numbers."""
        if y == 0:
            return "Cannot divide by zero!"
        else:
            return x / y

    def power(self, x, y):
        """Exponentiation operation: Returns x raised to the power of y."""
        return x ** y

    def sqrt(self, x):
        """Square root operation: Returns the square root of a number."""
        if x < 0:
            return "Square root of a negative number is not defined!"
        else:
            return math.sqrt(x)

    def log(self, x, base=10):
        """Logarithm operation: Returns the logarithm of x with the specified base."""
        if x <= 0 or base <= 0 or base == 1:
            return "Invalid input for logarithm!"
        else:
            return math.log(x, base)

    def sin(self, x):
        """Sine function: Returns the sine of an angle in radians."""
        return math.sin(x)

    def cos(self, x):
        """Cosine function: Returns the cosine of an angle in radians."""
        return math.cos(x)

    def tan(self, x):
        """Tangent function: Returns the tangent of an angle in radians."""
        return math.tan(x)

    def factorial(self, x):
        """Factorial operation: Returns the factorial of a non-negative integer."""
        if x < 0:
            return "Factorial is not defined for negative numbers!"
        else:
            return math.factorial(x)

    def permutation(self, n, r):
        """Permutation operation: Returns the number of permutations of n objects taken r at a time."""
        if n < r:
            return "Invalid input: n should be greater than or equal to r!"
        else:
            return math.perm(n, r)

    def combination(self, n, r):
        """Combination operation: Returns the number of combinations of n objects taken r at a time."""
        if n < r:
            return "Invalid input: n should be greater than or equal to r!"
        else:
            return math.comb(n, r)

    def absolute(self, x):
        """Absolute value operation: Returns the absolute value of a number."""
        return abs(x)
