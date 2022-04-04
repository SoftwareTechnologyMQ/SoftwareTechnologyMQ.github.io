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

Let's say we are given specifications for writing a function that takes in three numbers, and returns the *median* value, that is the value that sits in the middle when the numbers are arranged in ascending (or descending) order.

For number 1.5, 0.7 and 8.3, it's the number 1.5 that is the median value.

So let's write some tests and compare our notes.

First family of values will be three distinct values. The median should lie in all three places across the set.

- Second value is the median
	- 1.2, 3.5, 8.4: First less than third
	- 8.4, 3.5, 1.2: First more than third
- First value is the median
	- 3.5, 1.2, 8.4: Second less than third
	- 3.5, 8.4, 1.2: Second more than third
- Third value is the median
	- 8.4, 1.2, 3.5: First more than second
	- 1.2, 8.4, 3.5: First less than second


Second family of values should be two of the same values and a third unique value. The order should be shuffled to explore all combinations. On the same line of thought as the first family, we get the following combinations

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

Third family of values is where all three values are the same.

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

## assertEquals
The simplest assertion is `assertEquals`. The following assertion passes if and only if `a` is exactly the same as `b`.

```python
assertEquals(a, b)
```

Example:

```python 
assertEquals(square(6), 36)
```

## assertAlmostEqual
`assertAlmostEqual` takes into account rounding-off errors that may occur while comparing floating-point values. The following assertion passes if and only if `a` is almost the same as `b` (upto 6 to 7 decimal places)

```python
assertAlmostEqual(a, b)
```

Example:

```python 
assertAlmostEqual(square(1.25), 1.5625)
```



