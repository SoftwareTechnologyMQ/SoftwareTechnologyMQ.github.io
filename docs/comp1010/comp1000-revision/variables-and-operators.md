---
title: Variables and Operators
permalink: /comp1010/comp1000-revision/variables-and-operators
parent: COMP1000 Revision
grand_parent: COMP1010
nav_order: 1
---

- TOC
{:toc}


A *variable* is a named storage location that holds a value of a specific *type*. *Operators* combine values (and variables) into *expressions* that evaluate to a new value.

## Declaring and assigning variables

```java
type name = value;
```

Example:

```java
int age = 19;
double price = 4.95;
char grade = 'D';
boolean isEnrolled = true;
String unit = "COMP1010";
```

The most commonly used types are:

| Type      | Holds                             | Example literal |
|-----------|-----------------------------------|-----------------|
| `int`     | whole numbers                     | `42`, `-7`      |
| `double`  | floating-point numbers            | `3.14`, `17.0`  |
| `char`    | a single character                | `'a'`, `'7'`    |
| `boolean` | `true` or `false`                 | `true`          |
| `String`  | a sequence of characters          | `"hello"`       |

Note that `double` is the preferred floating-point type in Java (as opposed to `float` in Processing).

### Naming rules

A variable name (identifier) -

- can contain letters, digits, underscore (`_`) and dollar sign (`$`),
- cannot start with a digit,
- cannot be a reserved word (such as `int`, `if`, `class`),
- is case-sensitive (`total` and `Total` are different variables).

By convention, Java variable names use *camelCase* (`numberOfStudents`).

## Arithmetic operators

| Operator | Meaning                 | Example    | Result |
|----------|-------------------------|------------|--------|
| `+`      | addition                | `7 + 2`    | `9`    |
| `-`      | subtraction             | `7 - 2`    | `5`    |
| `*`      | multiplication          | `7 * 2`    | `14`   |
| `/`      | division                | `7 / 2`    | `3`    |
| `%`      | remainder (modulo)      | `7 % 2`    | `1`    |

### Integer division

If **both** operands are integers, `/` performs *integer division* and discards the fractional part.

```java
int a = 17/5;       // 3
double b = 17/5;    // 3.0 (integer division happens FIRST, then 3 is stored as 3.0)
double c = 17/5.0;  // 3.4 (one operand is a double, so the result is a double)
double d = (double)17/5; // 3.4 (casting 17 to a double before dividing)
```

### Remainder operator

`%` gives the remainder after integer division. It is very useful for checking divisibility.

```java
int r = 17 % 5;     // 2
boolean isEven = (n % 2 == 0);
int lastDigit = n % 10;
```

## Relational operators

Relational operators compare two values and produce a `boolean`.

| Operator | Meaning                  |
|----------|--------------------------|
| `==`     | equal to                 |
| `!=`     | not equal to             |
| `<`      | less than                |
| `<=`     | less than or equal to    |
| `>`      | greater than             |
| `>=`     | greater than or equal to |

Do not confuse `=` (assignment) with `==` (comparison).

## Logical operators

| Operator | Meaning | `true` when                    |
|----------|---------|--------------------------------|
| `&&`     | AND     | both operands are `true`       |
| <code>&#124;&#124;</code> | OR | at least one operand is `true` |
| `!`      | NOT     | the operand is `false`         |

```java
int x = 15;
boolean inRange = (x >= 10) && (x <= 20);   // true
boolean outside = (x < 10) || (x > 20);     // false
boolean notInRange = !inRange;              // false
```

## Operator precedence

From highest to lowest (operators on the same row are evaluated left to right):

1. `()` parentheses
2. `!`, unary `-`, casting
3. `*`, `/`, `%`
4. `+`, `-`
5. `<`, `<=`, `>`, `>=`
6. `==`, `!=`
7. `&&`
8. `||`
9. `=` (assignment)

When in doubt, use parentheses - they make your intention clear to the reader too.

## Shorthand assignment operators

```java
x += 5;   // x = x + 5;
x -= 5;   // x = x - 5;
x *= 5;   // x = x * 5;
x /= 5;   // x = x / 5;
x %= 5;   // x = x % 5;
x++;      // x = x + 1;
x--;      // x = x - 1;
```

## Exercises

Questions marked with ^**CORE** make a significant impact on subsequent learning.

### EXERCISE 1

Which one of the following is/are valid variable names?

1. `chicken_LEGS`
2. `COMP1000`
3. `1stOneIn`
4. `#hashtag`
5. `why?`
6. `chicken-LEGS`

### EXERCISE 2

What is the value of `n` when the following code executes?

```java
int n = 17/5;
```

### EXERCISE 3 ^**CORE**

What is the value of `n` when the following code executes?

```java
double n = 17/5;
```

### EXERCISE 4

What is the value of `n` when the following code executes?

```java
double n = 17/5.0;
```

### EXERCISE 5

What is the value of `flag` when the following code executes?

```java
boolean flag = (5 > 3) && (6 == 2);
```

### EXERCISE 6 ^**CORE**

What is the value of `flag` when the following code executes?

```java
boolean flag = true || true && false;
```

### EXERCISE 7

What are the values of `a`, `b` and `c` after the following code executes?

```java
int a = 10;
int b = 3;
int c = a % b + a / b * 2;
a += c;
b = a - b;
```

### EXERCISE 8

Write a boolean expression that is `true` if and only if the integer variable `year` holds a leap year. A year is a leap year if it is divisible by 4, except years divisible by 100, which are leap years only if they are also divisible by 400.

## More practice

- [Variables]({{ site.baseurl }}/comp1000/variables)
- [Boolean expressions]({{ site.baseurl }}/comp1000/boolean-expressions)
- [Practice with variables and operators]({{ site.baseurl }}/comp1000/practice-questions)
