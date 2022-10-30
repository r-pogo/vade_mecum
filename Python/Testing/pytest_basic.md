# Pytest
Example of testing a simple calculator:

````python
import numbers


class CalculatorError(Exception):
    """For calculator errors"""


class Calculator:
    """A terrible calculator."""

    def add(self, a, b):
        """Add two numbers."""
        self._check_operand(a)
        self._check_operand(b)
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide two numbers."""
        try:
            return a / b
        except ZeroDivisionError as ex:
            raise CalculatorError("You can't divide by zero.") from ex

    def _check_operand(self, operand):
        """Check that the operand is a number."""
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f'"{operand}" is not a number.')


if __name__ == "__main__":
    print("Let's calculate!")
    print("Press Ctrl+C to quit.")
    calculator = Calculator()
    operations = {
        "1": calculator.add,
        "2": calculator.subtract,
        "3": calculator.multiply,
        "4": calculator.divide,
    }
    while True:
        print("Pick a calculation:")

        for choice, operation in sorted(operations.items()):
            print(f"{choice}: {operation.__name__}")
        operation = input("What operation? ")
        if operation not in operations:
            print("Sorry, that's not a valid choice.")
            continue

        a = float(input("Select first operand: "))
        b = float(input("Select second operand: "))

        try:
            print("The result is: {}\n".format(operations[operation](a, b)))
        except CalculatorError as error:
            print(error)
````
## Testing script
````python
import pytest

from calculator import Calculator, CalculatorError


def test_add():
    calculator = Calculator()

    result = calculator.add(2, 3)

    assert result == 5


def test_add_weird_stuff():
    calculator = Calculator()

    with pytest.raises(CalculatorError):
        result = calculator.add("two", 3)


def test_add_weirder_stuff():
    calculator = Calculator()

    with pytest.raises(CalculatorError):
        result = calculator.add("two", "three")


def test_subtract():
    calculator = Calculator()

    result = calculator.subtract(9, 3)

    assert result == 6


def test_multiply():
    calculator = Calculator()

    result = calculator.multiply(9, 3)

    assert result == 27


def test_divide():
    calculator = Calculator()

    result = calculator.divide(9, 3)

    assert result == 3


def test_divide_by_zero():
    calculator = Calculator()

    with pytest.raises(CalculatorError):
        result = calculator.divide(9, 0)
````
___
## Sources used for the creation of this cheat sheet
[python-frederick/python-testing-101](https://github.com/python-frederick/python-testing-101)