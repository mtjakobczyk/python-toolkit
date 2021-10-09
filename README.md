# Python recipes and reusable code

## Test-driven development with Python
Project `my-app` provides a single module `csv-processor` that defines function `fun1()` inside `function.py` file.
```bash
my-app
└── modules # directory with all modules
    └── csv-processor # module csv-processor
        ├── __init__.py # empty file 
        ├── function.py
        └── tests
            ├── __init__.py # empty file
            └── test_function.py
```
The `__init__.py` files are empty. 
> The `__init__.py` files are required to make Python treat directories containing the file as packages.  
> https://docs.python.org/3/tutorial/modules.html#packages

```python
# csv-processor/function.py
def fun1():
	return 1
```

```python
# csv-processor/tests/test_function.py
import unittest
from ..function import fun1

class TestMyFunction(unittest.TestCase):

    def test_two(self):
        result1 = fun1()
        self.assertEqual(result1, 21)
```
Testing goes as follows:
```bash
cd my-app/modules/csv-processor
```
```bash
python3 -m unittest discover
```
Produces (output):
```console
======================================================================
FAIL: test_two (csv-processor.tests.test_function.TestMyFunction)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/*****/Code/my-app/modules/csv-processor/tests/test_function.py", line 8, in test_two
    self.assertEqual(result1, 21)
AssertionError: 1 != 21

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```
See:
- https://docs.python.org/3/library/unittest.html
- https://docs.python.org/3/tutorial/modules.html#packages
- https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure
