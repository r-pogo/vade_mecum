# Marks
Pytest allows to run selectively the tests by:
- run all tests in the current directory
- filtering functionality (use -k command line option to specify an 
expression which implements a substring match on the test names) e.h: `pytest -v -k string`
For running all tests except the ones that match the keyword: `pytest -k "not this" -v`  
Or select "test1" or "test2": `pytest -k "test1 or test2" -v`  
You can use and, or, not and parentheses.
- use markers

## Markers
You can define categories for your test and provides options for including or excluding
categories when running your suite. A test can be marked with any number of categories.

````python
from pytest import mark
import Calculator

@mark.calculator
def test_add():
    calculator = Calculator()

    result = calculator.add(2, 3)

    assert result == 5

def test_check_list():
    assert [1,2] == [1,2,3]
````
Now you can restrict a test run to run only test marked with `calculator`
`pytest -v -m calculator`
Or the inverse, running all tests except the calculator ones:
`pytest -v -m "not calculator"`  
You can use and, or, not  
Pytest provides some very useful markers out of the box, to se teh list use `pytest --markers`.  

If you create custom marks you should register them in the pytest.ini file, otherwise
when the test are ran there will always be the error message: `PytestUnknownMarkWarning`.  

Registering markers:
````python
# content of pytest.ini
[pytest]
markers =
    calculator: mark a test as a calculator.
````
Multiple custom markers can be registered, by defining each one in its own line, as shown in above example.

Example of default marker `skipif`:
````python
import pytest
from calculator import Calculator, CalculatorError
from pytest import mark
flag=0

@mark.calculator
def test_add():
    calculator = Calculator()
    result = calculator.add(2, 3)
    assert result == 5
    global flag
    flag = 1

@mark.skipif(flag=1)
def test_add_weird_stuff():
    calculator = Calculator()

    with pytest.raises(CalculatorError):
        result = calculator.add("two", 3)
````
___
## Marking at a class level
```python
from pytest import mark
from calculator import Calculator, CalculatorError

@mark.calculator
class CalculatorTest:
    
    def test_add():
    calculator = Calculator()
    result = calculator.add(2, 3)
    assert result == 5
    
    def test_subtract():
    calculator = Calculator()
    result = calculator.subtract(9, 3)
    assert result == 6
```
This is equivalent to directly applying the decorator to the two test functions.

To apply marks at the module level, use the pytestmark global variable:
```python
import pytest
pytestmark = pytest.mark.calculator
```
or multiple markers
```python
pytestmark = [pytest.mark.calculator, pytest.mark.weirdStuff]
```
___
## Sources used for the creation of this cheat sheet
- official pytest documentation website, [Working with custom markers](https://docs.pytest.org/en/7.1.x/example/markers.html#using-k-expr-to-select-tests-based-on-their-name)
