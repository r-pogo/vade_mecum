# Fixtures
Fixtures are used when we want to run some code before every test method.  
So instead of repeating the same code in every test we define fixtures.
Fixtures are a way of providing data, test doubles, or state setup to your tests.
E.g.: connecting to DB before starting testcase and disconnecting one, launching URL, maximize window before start and closing window when done, Opening data file for reading/writing and closing when done  

A method is marked as a Pytest fixture by marking with `@pytest.fixture`

```python
import os
from pytest import fixture
import Credential  # fake class for example
@fixture
def credential_helper():
    username = os.environ["USERNAME"]
    passwd = os.environ["PASSWD"]
    helper = Credential(username, passwd)
    return helper

def test_presence_bixby_please_beg_end_utt(credential_helper):
    access_credential = credential_helper.acces() # this is a fake method of a fake class just for example
    assert access_credential is True
```
___
## Fixture scope
Fixtures are created when first requested by a test, and are destroyed based on their scope:  
- function: the default scope, the fixture is destroyed at the end of the test.  
- class: the fixture is destroyed during teardown of the last test in the class.
- module: the fixture is destroyed during teardown of the last test in the module.  
- package: the fixture is destroyed during teardown of the last test in the package.  
- session: the fixture is destroyed at the end of the test session.
```python
@fixture(scope="function", params=["usr", "psswd"])  # Default scope 
```
From version 5.2 there exists also `dynamic scope`.
## Built in fixtures
Example of `tmpdir` and `capsys`:
```python
import json
import os

from tut5.myapp.sample import save_dict

# Return a temporary directory path object which is unique to each test
# function invocation, created as a sub directory of the base temporary
# directory

#  Enable text capturing of writes to ``sys.stdout`` and ``sys.stderr``

def test_save_dict(tmpdir, capsys):
    filepath = os.path.join(tmpdir, "test.json")
    _dict = {"a": 1, "b": 2}

    save_dict(_dict, filepath)
    assert json.load(open(filepath, 'r')) == _dict
    assert capsys.readouterr().out == "saved\n"
```
___
## Fixtures factory
Basically higher order function used to create multiple testing objects
```python
import pytest
from datetime import datetime
from tut7.myapp.student import Student, get_topper # fake class just for example

@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1, 1), "coe", credits)

    return _make_dummy_student

def test_get_topper(make_dummy_student):
    students = [
        make_dummy_student("ram", 21),
        make_dummy_student("shyam", 19),
        make_dummy_student("ravi", 22)
    ]

    topper = get_topper(students)

    assert topper == students[2]
```
If you have many fixtures you can keep them in a `conftest.py` to better organize your code
___

#TODO [conftest.py](https://docs.pytest.org/en/6.2.x/fixture.html#conftest-py-sharing-fixtures-across-multiple-files)
#TODO use multiple fixtures
#TODO fixtures with yield
## Sources used for the creation of this cheat sheet
- official pytest documentation website, [How to use fixtures](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html)
- [nikhilkumarsingh/pytest-tut](https://github.com/nikhilkumarsingh/pytest-tut)
