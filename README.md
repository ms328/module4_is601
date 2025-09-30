Project Structure
app/
├── calculator/
│   └── __init__.py        # CLI REPL loop for calculator
├── calculation/
│   └── __init__.py        # Calculation base + concrete classes (Add, Subtract, Multiply, Divide, Modulus)
├── operation/
│   └── __init__.py        # Operation class with arithmetic functions
tests/
├── test_calculations.py    # Unit tests for calculation classes
├── test_calculator.py      # Tests for CLI calculator
└── test_operations.py      # Tests for Operation class

Features

Command-Line Interface (CLI): REPL-style calculator for user interaction.

Advanced OOP:

Calculation abstract class

Concrete classes: AddCalculation, SubtractCalculation, MultiplyCalculation, DivideCalculation, ModulusCalculation

CalculationFactory for object creation

Error Handling:

Handles division by zero and modulus by zero with clear error messages.

Testing with pytest:

Unit tests for all operations

Parameterized tests for efficiency

Edge case testing (e.g., zero divisor)

100% Test Coverage verified via pytest-cov.

Installation & Setup

Clone the repository:

git clone <your-repo-url>
cd module4_is601


Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows


Install dependencies:

pip install -r requirements.txt

Running Tests

Run all tests with coverage:

pytest --cov=app --cov-report=term-missing --cov-report=html


Open the HTML report:

open htmlcov/index.html    # macOS
start htmlcov/index.html   # Windows

Usage

Start the calculator from the CLI:

python -m app.calculator


Example interaction:

Enter first number: 10
Enter operation (+, -, *, /, %): %
Enter second number: 3
Result: 1

Learning Outcomes

Applied advanced OOP principles in Python.

Implemented the Factory Pattern for calculation objects.

Achieved 100% test coverage with pytest.

Practiced professional coding practices including modular design, error handling, and documentation.