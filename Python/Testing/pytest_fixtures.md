# Fixtures
Fixtures are a way of providing data, test doubles, or state setup to your tests.    
Fixtures are functions that can return a wide range of values.  
Eg.: connecting to DB before starting testcase and disconnecting one, launching URL, maximize window before start and closing window when done, Opening data file for reading/writing and closing when done  

```python
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

#TODO [conftest.py](https://docs.pytest.org/en/6.2.x/fixture.html#conftest-py-sharing-fixtures-across-multiple-files)

## Sources used for the creation of this cheat sheet
- official pytest documentation website, [How to use fixtures](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html)
