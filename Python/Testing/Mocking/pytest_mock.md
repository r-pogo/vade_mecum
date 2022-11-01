# Mock
Mock object allows to replace the actual call for a dependency, and replicate the behaviour of the dependency.
Example of mock concept:
```python
from unittest import mock
import random

def roll_dice():
   return random.randint(1, 6)

mock_roll_dice = mock.Mock(name= "roll dice Mock", return_value=3)

roll_dice = mock_roll_dice
roll_dice()
```
# TODO finish description https://blog.finxter.com/how-to-use-mock-in-pytest/
https://medium.com/analytics-vidhya/mocking-in-python-with-pytest-mock-part-i-6203c8ad3606

___
## Sources used for the creation of this cheat sheet
- [nikhilkumarsingh/pytest-tut](https://github.com/nikhilkumarsingh/pytest-tut)