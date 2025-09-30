# operations.py

class Operation:
    """
    The Operation class encapsulates basic arithmetic operations as static methods.
    This design groups related functions (addition, subtraction, multiplication, division, 
    and power) in a single class, making the code more modular and organized.
    """

    @staticmethod
    def addition(a: float, b: float) -> float:
        """Adds two floating-point numbers and returns the result."""
        return a + b
    
    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """Subtracts the second number from the first and returns the result."""
        return a - b
    
    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """Multiplies two floating-point numbers and returns the product."""
        return a * b
    
    @staticmethod
    def division(a: float, b: float) -> float:
        """Divides the first number by the second and returns the quotient."""
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
    
    @staticmethod
    def power(a: float, b: float) -> float:
        """Raises one number to the power of another and returns the result."""
        return a ** b
    
    @staticmethod
    def modulus(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Modulus by zero is not allowed.")
        return a % b