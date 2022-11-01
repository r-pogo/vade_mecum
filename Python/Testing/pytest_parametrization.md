# Parametrization
The purpose of parameterizing a test is to run a test against multiple sets of arguments. 
We can do this by `@pytest.mark.parametrize`.

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

# A different example non related to Calculator class
@mark.parametrize("a,b,c", [(1, 2, 3), ("a", "b", "ab"),
                                   ([1, 2], [3], [1, 2, 3])],
                         ids=["num", "str", "list"])  # ids are the names for each case you are passing for the test
def test_add(a, b, c):
    assert add(a, b) == c
```
___
## Fixture level
The fixture function gets access to each parameter through the special request object:
```python
from pytest import fixture

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
#TODO Dynamiczna parametryzacja funkcji pytest_generate_tests
___
## Sources used for the creation of this cheat sheet
- official pytest documentation website, [Parametrizing tests](https://doc.pytest.org/en/latest/example/parametrize.html)
- official pytest documentation website, [How to parametrize fixtures and test functions](https://doc.pytest.org/en/latest/how-to/parametrize.html#parametrize-basics)
- official pytest documentation website, [How to use fixtures/Parametrizing fixtures](https://doc.pytest.org/en/latest/how-to/fixtures.html#fixture-parametrize)
- [nikhilkumarsingh/pytest-tut](https://github.com/nikhilkumarsingh/pytest-tut)