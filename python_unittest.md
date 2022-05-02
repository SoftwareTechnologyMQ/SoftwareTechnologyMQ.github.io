---
layout: page
title: Python unittest
within: programming
---

<details class="prereq" markdown="1">
<summary>Assumed Knowledge</summary>
  * Variables and Operators in Python
  * Control structures (conditions and loops)
  * Functions
</details>

<details class="outcomes" markdown="1">
<summary>Learning Outcomes</summary>
  * Be acquainted with unittest environment.
  * Write a piece of code based on tests provided.
</details>

# Author: Gaurav Gupta

# Introduction

It is common to write a function and make a *simple* mistake that does not reveal itself until it's too late.

### Example 1

```python
def is_positive(val):
	if val >= 0:
		return True
	else:
		return False
```

This function would return true for for any `val` that is greater than **or equal to** zero. However, zero is NOT a positive number. Neither is it a negative number. 

Wouldn't it be greate, if we could catch this issue nice and early?

That is what unit testing provides. A set of inputs and corresponding expected outputs.

In this case, the following would be a start but not an adequate set.

|val|value returned|
|---|--------------|
|1.4|True|
|-2.7|False|

*Edge* cases should also be considered. So, we will include values on either side of zero, and zero itself.

|val|value returned|
|---|--------------|
|1.4|True|
|-2.7|False|
|-0.0001|False|
|0|False|
|0.0001|True|

## Write tests before code

In test-driven development, tests are written before the code and cover the different scenarios possible.

## Example 2

### Problem definition: Write a function that takes in three numbers, and returns the *median* value, that is the value that sits in the middle when the numbers are arranged in ascending (or descending) order.

For number 1.5, 0.7 and 8.3, it's the number 1.5 that is the median value.

Let us write some tests and compare our notes.

### First family of values will be three distinct values. 

The median should lie in all three places across the set.

- Second value is the median
	- 1.2, 3.5, 8.4: First less than third
	- 8.4, 3.5, 1.2: First more than third
- First value is the median
	- 3.5, 1.2, 8.4: Second less than third
	- 3.5, 8.4, 1.2: Second more than third
- Third value is the median
	- 8.4, 1.2, 3.5: First more than second
	- 1.2, 8.4, 3.5: First less than second


### Second family of values should be two of the same values and a third unique value. 

The order should be shuffled to explore all combinations. On the same line of thought as the first family, we get the following combinations

- First and second are the same
	- 25, 25, 75: Unique value is higher
	- 75, 75, 25: Unique value is lower
- First and third are the same	
	- 25, 75, 25: Unique value is higher
	- 75, 25, 75: Unique value is lower
- Second and third are the same
	- 75, 25, 25: Unique value is higher
	- 25, 75, 75: Unique value is lower

Note that we should try and not re-use the same few numerical value for all the cases, hence we replaced 1.2, 3.5 and 8.4 with 25 and 75 for the second family. 

### Third family of values is where all three values are the same.

- -10000, -10000, -10000

The complete set, and required answer, are:

|Input|Output|
|-----|------|
|1.2, 3.5, 8.4|3.5|
|8.4, 3.5, 1.2|3.5|
|3.5, 1.2, 8.4|3.5|
|3.5, 8.4, 1.2|3.5|
|8.4, 1.2, 3.5|3.5|
|1.2, 8.4, 3.5|3.5|
|25, 25, 75|25|
|75, 75, 25|75|
|25, 75, 25|25|
|75, 25, 75|75|
|75, 25, 25|25|
|25, 75, 75|75|
|-10000, -10000, -10000|-10000|

# Assertions

Python checks if the input matches the value returned using assertions.

## assertEqual
The simplest assertion is `assertEqual`. The following assertion passes if and only if `a` is exactly the same as `b`.

```python
assertEqual(a, b)
```

Example:

```python 
assertEqual(square(6), 36)
```

## assertAlmostEqual
`assertAlmostEqual` takes into account rounding-off errors that may occur while comparing floating-point values. The following assertion passes if and only if `a` is almost the same as `b`, upto 6 to 7 decimal places by default, or up to `n` decimal places if the third parameter is supplied. If `n` is supplied, it rounds off the numbers to `n` decimal places. `2.236` rounded-off to 2 decimal places will be `2.24`, while `1.4641` rounded-off to 2 decimal places will be `1.46`.

```python
assertAlmostEqual(a, b)
#OR
assertAlmostEqual(a, b, n)
```

Example:

```python 
assertAlmostEqual(square(1.25), 1.5625)
assertAlmostEqual(square(1.2), 1.464, 3) #just check first 3 decimal places
```

## assertTrue, assertFalse

`assertTrue` passes if and only if the value passed to the assertion is `True`.

```python
assertTrue(is_positive(3))
```

`assertFalse` is the opposite, it passes if and only if the value passed to the assertion is `False`.

```python
assertFalse(isPositive(0))
```

# Summary of assertions

A list of all assertions is given below:

| Method                                                                                                                 | Checks                                  | Version |
| ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ------- |
| [assertEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual)                           | a == b                                  | 3.x     |
| [assertNotEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual)                     | a != b                                  | 3.x     |
| [assertTrue](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue)                             | bool(x) is True                         | 3.x     |
| [assertFalse](https://docs.python.org/3/library/unittest.html#unittest.TestCase.ssertFalse)                            | bool(x) is False                        | 3.x     |
| [assertIs](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs)                                 | a is b                                  | 3.x     |
| [assertIsNot](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNot)                           | a is not b                              | 3.x     |
| [assertIsNone](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNone)                         | x is None                               | 3.x     |
| [assertIsNotNone](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNotNone)                   | x is not None                           | 3.x     |
| [assertIn](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn)                                 | a in b                                  | 3.x     |
| [assertNotIn](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIn)                           | a not in b                              | 3.x     |
| [assertIsInstance](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsInstance)                 | is instance(a,b)                        | 3.x     |
| [assertNotIsInstance](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsInstance)           | not is instance(a,b)                    | 3.x     |
| [assertRaises](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises)                         | fun(\*args,\*\*kwds) raises exc         | 3.x     |
| [assertRaisesRegexp](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaisesRegexp)             | fun(\*args,\*\*kwds) raises exc(regex)  | 3.x     |
| [assertAlmostEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual)               | round(a-b,7) == 0                       | 3.x     |
| [assertNotAlmostEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotAlmostEqual)         | round(a-b,7) != 0                       | 3.x     |
| [assertGreater](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreater)                       | a > b                                   | 3.x     |
| [assertGreaterEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreaterEqual)             | a >= b                                  | 3.x     |
| [assertLess](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLess)                             | a < b                                   | 3.x     |
| [assertLessEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLessEqual])                  | a <= b                                  | 3.x     |
| [assertRegexpMatches](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRegexpMatches)           | r.search(s)                             | 3.x     |
| [assertNotRegexpMatches](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotRegexpMatches)     | not r.search(s)                         | 3.x     |
| [assertItemsEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertItemsEqual)                 | sorted(a) == sorted(b)                  | 3.x     |
| [assertDictContainsSubset](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertDictContainsSubset) | all the key/value pairs in a exist in b | 3.x     |
| [assertMultiLineEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertMultiLineEqual)         | strings                                 | 3.x     |
| [assertSequenceEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSequenceEqual)           | sequences                               | 3.x     |
| [assertListEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertListEqual)                   | lists                                   | 3.x     |
| [assertTupleEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTupleEqual)                 | tuples                                  | 3.x     |
| [assertSetEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSetEqual)                     | sets or frozensets                      | 3.x     |
| [assertDictEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertDictEqual)                   | dicts                                   | 3.x     |

# How are assertions used

First thing is to import the `unittest` library as:

```python
import unittest
```

Assertions need to be wrapped in a class with the header:

```python
class Tester(unittest.TestCase):
```

and then inside a function with the header:

```python
def test_function_name(self):
```

So, if the name of the function to be tested is `is_positive`, it would become:

```python
def test_is_positive(self):
```

and if the name of the function to be tested is `square`, it would become:

```python
def test_square(self):
```

So far, we got:

```python
class Tester(unittest.TestCase):
	def test_function_name(self):
```

In there, you can have whatever assertions you want. You just need to prefix each assertion with `self.`. Some examples:

```python
self.assertTrue(is_positive(20))
self.assertEqual(square(6), 36))
self.assertAlmostEqual(average(3, 4), 3.5)
```

## One final step

The final step is to include the *driver*, so as to specify that it's a `unittest` we want to run.

```python
if __name__ == "__main__":    
    unittest.main() 
```

## Outcomes

If all the tests pass, python tells you everything went well, using **OK**.


```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

In case of failure, it will tell you the problem and also that it **Failed**. For example:

```
Traceback (most recent call last):
  File "/Users/gauravgupta/Documents/SoftwareTechnologyMQ.github.io/assets/codes/unittest_example_1.py", line 5, in test_is_positive
    self.assertTrue(is_positive(5635.5))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```

If all tests in a file pass, you should see something like (example for file containing 13 tests):

```
.............
----------------------------------------------------------------------
Ran 13 tests in 0.023s

OK
```

For each test failed, you get an explanation, such as,

```
..........F..
======================================================================
FAIL: test_sum_even (__main__.Tester)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/gauravgupta/Downloads/comp6010practicePackage-main/02_loops.py", line 195, in test_sum_even
    self.assertEqual(sum_even(2, 6), 6)
AssertionError: 8 != 6

----------------------------------------------------------------------
Ran 13 tests in 0.024s

FAILED (failures=1)
```

Here, it's saying that `self.assertTrue(is_positive(5635.5))` failed because the function call resulted in `False`, which is not `True` (as per the assertions demands).

# First complete example (assertTrue, assertFalse)

```python
import unittest

class Tester(unittest.TestCase):
    def test_is_positive(self):
        self.assertTrue(is_positive(5635.5))
        self.assertTrue(is_positive(1))
        self.assertTrue(is_positive(0.1))
        self.assertTrue(is_positive(0.01))
        self.assertFalse(is_positive(0))
        self.assertFalse(is_positive(-0.1))
        self.assertFalse(is_positive(-0.01))
        self.assertFalse(is_positive(-11454.4))
    
def is_positive(val):
    if val > 0:
        return True
    else:
        return False

if __name__ == "__main__":    
    unittest.main() 
```

# Second complete example (assertEqual)

```python
import unittest

class Tester(unittest.TestCase):
    def test_highest(self):
        self.assertEqual(3, highest(1, 1, 3))
        self.assertEqual(7, highest(5, 7, 5))
        self.assertEqual(-4, highest(-4, -10, -10))
        self.assertEqual(1, highest(1, 1, -3))
        self.assertEqual(5, highest(5, -7, 5))
        self.assertEqual(-10, highest(-14, -10, -10))
        self.assertEqual(1729, highest(1729, 1729, 1729))
        self.assertEqual(30, highest(10, 20, 30))
        self.assertEqual(100, highest(50, 100, 60))
        self.assertEqual(-100, highest(-500, -120, -100))
    
def highest(a, b, c):
    if a>=b:
        if a>=c:
            return a
        else:
            return c
    else:
        if b>=c:
            return b
        else:
            return c

if __name__ == "__main__":    
    unittest.main() 
```

# Third complete example (assertAlmostEqual)

```python
import unittest

class Tester(unittest.TestCase):
    def test_average(self):
        self.assertAlmostEqual(2.5, average(2, 3))
        self.assertAlmostEqual(-2.5, average(-2, -3))
        self.assertAlmostEqual(0, average(2, -2))
        self.assertAlmostEqual(-51.3, average(-51.1, -51.5))
        
        #up to 2 decimal places
        self.assertAlmostEqual(average(1.2555, 1.3), 1.28, 2) 
        
        #up to 1 decimal place only
        self.assertAlmostEqual(average(1.2345, 4.5678), 2.9, 1)

def average(a, b):
    return (a+b)/2

if __name__ == "__main__":    
    unittest.main() 
```


# An example where you complete the function

```python
import unittest

class Tester(unittest.TestCase):
    def test_is_odd(self):
        self.assertTrue(is_odd(5))
        self.assertTrue(is_odd(-5))
        self.assertTrue(is_odd(517))
        self.assertTrue(is_odd(-6561))
        self.assertFalse(is_odd(0))
        self.assertFalse(is_odd(8))
        self.assertFalse(is_odd(-8))
        self.assertFalse(is_odd(8096))
        self.assertFalse(is_odd(-8096))
    
def is_odd(val):
    return True # replace this with actual code

if __name__ == "__main__":    
    unittest.main() 
```
    
# An example where you write the tests and then the function

```python
import unittest

class Tester(unittest.TestCase):
    def test_is_divisible_by(self):
        # TODO
    
def is_odd(a, b):
    return True #update so it returns True if and only if a is divisible by b

if __name__ == "__main__":    
    unittest.main() 
```

# PRACTICE PACKAGE!!!

Find the entire practice package at [COMP6010PracticePackage.zip](https://softwaretechnologymq.github.io/assets/codes/COMP6010PracticePackage.zip)


