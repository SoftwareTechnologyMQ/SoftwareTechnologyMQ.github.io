---
layout: page
title: "Practice with variables and operators"
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge</summary>

  * Variables
  * Arithmetic operators
  * Boolean operators
  * Boolean expressions
</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes</summary>

  * Determine where you stand in terms of using arrays

</details>

## Author: Gaurav Gupta

# Practice with variables

These practice questions are diagnostic in nature and should not be considered as samples for module exams or other assessments.

These will help you and the drop-in centre staff diagnose any gaps in knowledge and fix the same.

You unlock a level if you are able to solve the majority (defined here as *greater than or equal to 50%*) of questions at that level. For example, if you can solve majority of questions at "Pass to Credit" level but not "Credit to Distinction" level, it means you are somewhere in the Pass-Credit region.

## Level 1 - Pass

1. Write a statement that declares a variable named `nStudents` and assigns it the value 24. More than one data type are possible, but there is one that is more correct than the other.

2. Write a statement that declares a variable named `pi` and assigns it the value 3.14159.

3. Write a statement that declares a variable named `isHit` and assigns it the value `false`.

4. Write a statement that declares a variable named `initial` and assigns it the first character of your given name. 

5. What is the expression `20/5` evaluated to?

6. What is the expression `10 == 5` evaluated to?

7. What is the expression `6/4` evaluated to?

8. What is the expression `6/4.0` evaluated to?

9. What is the data type of the expression `6 + (3 - 5)/2 * 5`?

10. What is the data type of the expression `6 + (3 - 5.0)/2 * 5`?

11. What is the expression `150 > 128` evaluated to?

12. What is the expression `42 != 42` evaluated to?

13. What is the expression `-6 <= -6` evaluated to?

14. What is the expression `-6 < -6` evaluated to?

## Level 2 - Pass to Credit

1. Assume the existence of an integer variable `n`. Write one or more statements that assigns the valuer of the integer after `n`, to a variable named `nextOne` (that you should declare). For example, if `n = 7`, `nextOne` should be 8.

2. Assume the existence of two integer variables `x` and `y`. Write one or more statements that assigns the product of the two, to a variable named `z` (that you should declare).

3. The expression `12 = 6 * 2` attempts to determine if 12 is equal to 6 * 2, but it has a bug. Identify and fix it.

4. What is the expression `3 + 5 * 2` evaluated to?

5. The following statement determines if a student has passed on not based on the minimum passing mark and their mark. What is wrong with the code, if anything? If there is, in fact, a problem, think of the different ways in which it can be fixed. Is there one approach that is better than the other?

```java
boolean studentPasses = (minimumPassingMark > studentMark);
```

6. If `x` is an integer variable, is the statement `x = x + 2.4;` valid?

7. What is wrong with the following code?

```java
int a = 10;
int b = 20;
int c = 30
a = a + b;
b = b + c;
c = c + a;
a = a + 1;
int d = 40;
int e = a + b + c + d + e;
```

8. What is wrong with the following code?

```java
int a = 10;
float b = 20;
int c = 30
b = b + c;
a = a - c;
c = b + c;
```

9. What is wrong with the following code?

```java
int a = 10;
boolean b = true;
char c = "f";
float f = 1.618;
```

## Level 3 - Credit to Distinction

1. What is wrong with the following statement, if anything? If there is, in fact, a problem, think of the different ways in which it can be fixed. Is there one approach that is better than the other?

2. What is the expression `6 + 4 / 3` evaluated to?
  

```java
int speed = 24.5;
``` 

3. What is wrong with the following statement, if anything? If there is, in fact, a problem, think of the different ways in which it can be fixed. Is there one approach that is better than the other?


```java
float x = 15;
``` 

4. What is wrong with the following statement, if anything? If there is, in fact, a problem, think of the different ways in which it can be fixed. Is there one approach that is better than the other?


```java
float flightCount = 15;
``` 

5. Assume the existence of an integer variable `n`. Write one or more statements that assigns the last digit of `n`, to a variable named `lastDigit` (that you should declare).

6. What is wrong with the following statement, if anything? If there is, in fact, a problem, think of the different ways in which it can be fixed. Is there one approach that is better than the other?


```java
boolean identical = (width1 = width2 && height1 = height2);
```

## Level 4 - Distinction to High Distinction

1. Write the boolean expression that evaluates to `true` if a year held in variable `yy` is a leap year, `false` otherwise.

2. What is the expression `12/5 == 2` evaluated to?
 
3. What is the value of `x` after the following statement executes?

```java
float x = 36/10;
```

4. Assuming the existence of two integers `tom` and `jerry`, assign the average of the two to a variable named `bruno` (that you should declare). For example, if `tom = 10, jerry = 15`, then `bruno` should be 12.5

5. Assume that the top-left corner of a rectangle is at the location `(x1, y1)`, its width is `w` and height is `h`. Store the bottom-right corner of the rectangle in variables `(x2, y2)`.

6. Assume that the top-right corner of a rectangle is at the location `(x1, y1)`, its width is `w` and height is `h`. Store the bottom-left corner of the rectangle in variables `(x2, y2)`.

7. What is the output of the following code (the final value of `r2d2`)?

```java
int r2d2 = 12;
r2d2 = r2d2 + 3.6;
println(r2d2);
```

8. What is the output of the following code (the final value of `r2d2`)?

```java
int r2d2 = 12;
r2d2+=3.6;
```

## Level 5 - High Distinction and beyond

1. Assuming the existence of a floating-point variable `val` that holds some non-negative value, write one or more statements that assigns `val` rounded-off to the nearest integer, into `n`. You may not use any built-in math functions (such as `ceil(), floor(), ...`), or conditions.

2. Assuming the existence of a numerical (integer/floating-point) variable `val`, ass

3. Assume that the top-left corner of a rectangle is at the location `(x1, y1)`, its width is `w1` and height is `h1`, and also that the top-left corner of the another rectangle is at the location `(x2, y2)`, its width is `w2` and height is `h2`. Write one or more statements such that by the end of those statements being executed, a variable `overlapping` holds the value `true` if the two rectangles overlap (even if just their borders are overlapping), `false` otherwise.

4. Assume a circle with its centre at `(x, y)` and radius of `r`. Write one or more statements such that by the end of those statements being executed, variables `leftMostX, leftMostY` represent the left-most point of the circle. 