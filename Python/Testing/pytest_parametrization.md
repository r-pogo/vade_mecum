# Parametrization
When you have several tests with slightly different inputs and expected outputs.  
In these cases, you can parametrize a single test definition, and pytest will 
create variants of the test for you with the parameters you specify.  

Parametrize works at different levels: `@mark.parametrize` and `fixture`.  
## Mark level
This solution is harder to maintain
```python
from pytest import mark
import Calculator

@mark.parametrize("number", [1, 0, 1000, -3])
def test_first(number):
    assert number > 0

@mark.parametrize("a, b", [(2,5), (10,20), (25, 15), (-1, 1)])
def test_add(a, b):
    calculator = Calculator()
    result = calculator.add(a, b)
    assert result >= 0
```
___
## Fixture level
The fixture function gets access to each parameter through the special request object:
```python
from pytest import fixture, mark

@fixture(params=["apple", "banana", "orange"])
def fruit(request):
    return request.param # allows to read the params of the fixture

def test_fruit(fruit):
    print(f" I am {fruit}")
```
Using marks with parametrized fixtures
```python
import pytest

@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)])
def data_set(request):
    return request.param

def test_data(data_set):
    pass
```
___
## Sources used for the creation of this cheat sheet
- official pytest documentation website, [Parametrizing tests](https://doc.pytest.org/en/latest/example/parametrize.html)
- official pytest documentation website, [How to parametrize fixtures and test functions](https://doc.pytest.org/en/latest/how-to/parametrize.html#parametrize-basics)
- official pytest documentation website, [How to use fixtures/Parametrizing fixtures](https://doc.pytest.org/en/latest/how-to/fixtures.html#fixture-parametrize)