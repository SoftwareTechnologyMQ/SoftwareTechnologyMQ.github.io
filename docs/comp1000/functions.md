---
title: Functions
permalink: /comp1000/functions
parent: COMP1000
nav_order: 10
---

- TOC
{:toc}

<!-- Assumed Knowledge -->
{% capture topic_prereq %}
  * [Primitive Operations]({{ site.baseurl }}/comp1000/primitive-operations)
  * [Variables]({{ site.baseurl }}/comp1000/variables)
  * [Conditions]({{ site.baseurl }}/comp1000/conditions)
{% endcapture %}
<!-- Learning Outcomes -->
{% capture topic_outcomes %}
  * Know the syntax of functions
  * Understand how functions relate to algorithms
  * Be able to pass values into a function
  * Be able to get values back from a function
  * Be able to write your own functions
  * Be able to reason about the flow of a program that uses functions
{% endcapture %}

{% include prereq_outcomes.html prereq=topic_prereq outcomes=topic_outcomes %}

{: .keynote}
A function is a named piece of code that can be supplied with some inputs (known as parameters) and may return a value back to the caller.

{: .readings}
* Chapter 7 of [Learning Processing](http://learningprocessing.com) by Danel Shiffman.

## Macquarie University Videos

### Function Design

{% include youtube.html id="1taENRdghmQ" %}

### Function Defintion and Call

{% include youtube.html id="CowX0cMCg1s" %}

## Videos by Daniel Shiffman

{% include youtube.html id="zBo2D3Myo6Q" %}

{% include youtube.html id="j_XyeWg_3EE" %}

{% include youtube.html id="b9AYvekwKIg" %}

## Discussion

A function is a *named* piece of code with zero or more inputs that optionally returns a value back to the caller.

<img src="{{ site.baseurl }}/assets/comp1000/functions/functionMemoryDiagrams-figure0.png" style="width: 300px; margin: 16px"/>

<!--For example, we may have a function that determines the higher of two integers. We can call it by passing it two integers. If we pass the values 2 and 5, it should return 5.

<div class="centred-img"><img src="functionsFigs/functionMemoryDiagrams-figure1.png" style="width: 300px;"/></div>

However, if we pass only one value, it cannot be executed, as it expects two integers.

<div class="centred-img"><img src="functionsFigs/functionMemoryDiagrams-figure2.png" style="width: 300px;"/></div>

Similarly, you cannot pass it more than 2 values.

<div class="centred-img"><img src="functionsFigs/functionMemoryDiagrams-figure3.png" style="width: 300px;"/></div>

Even if you pass two values, you must ensure they are of the right type. For example, we cannot pass a `boolean` instead of an integer.

<div class="centred-img"><img src="functionsFigs/functionMemoryDiagrams-figure4.png" style="width: 300px;"/></div>
-->
### Designing a function

While designing a function, you must think of three aspects carefully:

1. Input(s)
2. Purpose (decides the name of the function)
3. Return value (Type of answer)

#### Example 1

```text
Alice -> Bob: Is 5 an even number?
Bob --> Alice: No.
Charles -> Bob: Is -18 an even number?
Bob --> Charles: Yes.
```

Here, *"Bob"* is the function that expects an integer value to be supplied to them, and gives the answer *"Yes"/"No"* back to the client (caller).

1. Input: `int`
2. Purpose: `isEven`
3. Return value: boolean

#### Example 2

```text
Alice -> Bob: What is 12.8 rounded-off to the nearest integer?
Bob --> Alice: 13.
Charles -> Bob: What is -3.01 rounded-off to the nearest integer?
Bob --> Charles: -3.
Diane -> Bob: What is "Super Nintendo Chalmers" rounded-off to the nearest integer?
Bob --> Diane: GO AWAY!
Elise -> Bob: What are 1.5 and -2.7 rounded-off to the nearest integer?
Bob --> Elise: One number at a time, please.
```

Here, we have intentionally made invalid calls from Diane (and Elise) to Bob. This shows that Bob expects one (and only one) `float` to be provided.

1. Input: `float`
2. Purpose: `roundedOff`
3. Return value: `int`

### Defining a function

All functions have _just one_ function definition - the place that the function itself is described.  Syntax of a function _definition_ is:

```java
returnType function(<parameters>) {
    <some code>
    <if>
    	<return statement>
    <endif>
    <some code>
    <return statement>
}
```

Once this exists, you can have _many_ function calls - the place that the code asks the function to run.  Syntax of a function _call_ is:

```java
functionName (<parameters>);
```

For example, the following function _definition_

```java
int foo(int a, int b){
    int result = a + b;
    return result;
}
```

can be called by anywhere in the program. For example,

```java
void setup() {
	int y = foo(12, 5);
}
```

During the call `foo(12, 5)`,

- Function `foo` expects two integers
- The values passed are 12 and 5 (2 integers). So it's all good
- 12 is copied into the local variable `a`
- 5 is copied into the local variable `b`
- Control is transferred to the function
- `result` becomes 17.
- This value 17 is returned by the function and replaces the call `foo(12, 5)`.
- Control transfers back to the calling statement.
- The statement becomes `int y = 17;` since the call is replaced by the value it returns.

### Formal and Actual parameters

Since we have both function definitions and function calls, and parameters appear in each, it is useful to be able to distinguish the two uses.
  * Parameters appearing in the top line (signature) of a function definition are called _formal parameters_ and are defined in the same way as any other variable declaration. In the example above, `a` and `b` are the *formal parameters*.
  * Parameters appearing in a function call are called _actual paramters_ and work like any other value in Processing. In the example above, 12 and 5 are the *actual parameters*.

When the function is executed, the actual paramters are copied into the formal paramter slots and the function is run.

<!-- Exercise -->
{% capture my_problem %}
Suppose we have a function that accepts a real number (`float`) and returns its square.

Draw a block diagram for the interaction when a caller calls the function with the value 2.5. Assume the name of the formal parameter is `val`, and the value returned by the function is copied into a variable `sqr`.
{% endcapture %}

{% capture my_solution %}
<img src="{{ site.baseurl }}/assets/comp1000/functions/block_ans.png" alt="Block Diagram Answer" />
{% endcapture %}

{% include exercise.html
  title=""
  problem=my_problem
  solution=my_solution
%}

<!-- Exercise -->
{% capture my_problem %}
Consider the following function definition,

```java
int roundOff(float a) {
	return (int)(a+0.5);
}
```

Write a statement that calls the function `roundOff` with the parameter 6.8 and stores the value returned in a variable `result`.
{% endcapture %}

{% capture my_solution %}
```java
int result;
result = roundOff(6.8);
```
{% endcapture %}

{% include exercise.html
  title=""
  problem=my_problem
  solution=my_solution
%}

<!-- Exercise -->
{% capture my_problem %}
Which of the following are valid calls to function `roundOff`?

1. `int a = roundOff(4.5);`
2. `int b = roundOff(8);`
3. `roundOff(2.6);`
4. `float c = roundOff(-1.53);`
5. `int d = roundOff(3.2, 4.8);`
6. `int e = roundOff();`
7. `int e = roundOff(true);`
{% endcapture %}

{% capture my_solution %}
1. Yes
2. Yes, the integer is treated like a float when it arrives in the formal parameter.  It is identical to writing `float a = 8`
3. Yes, the return value is thrown away, but that is allowed
4. Yes, the return value is treated like a float when it arrives in `c`
5. No, too many actual parameters
6. No, not enough acutal parameters
7. No, actual parameter type does not match formal parameter type.
{% endcapture %}

{% include exercise.html
  title=""
  problem=my_problem
  solution=my_solution
%}

<!-- Exercise -->
{% capture my_problem %}
Define a function that when passed two integers, returns their average. Remember that 15/2 is 7 while 15/2.0 is 7.5.
{% endcapture %}

{% capture my_solution %}
```java
float average(int a, int b){
    return (a + b)/2.0;
}
```
{% endcapture %}

{% include exercise.html
  title=""
  problem=my_problem
  solution=my_solution
%}

### Void Functions

Functions that perform some action (like drawing something or displaying some text) but don't return a value have a return type of void. They can still have a `return;` statement, that transfers control back to the caller.

For example,

```java
void drawShip() {
	//IMPORTANT: should draw the ship ONLY if mouse is in the right half

	if(mouseX < width/2) { //no need to draw
		return; //transfer control back to the caller
	}

	line(mouseX+50, mouseY-20, mouseX+50, mouseY+10);
	triangle(mouseX, mouseY, mouseX+100, mouseY, mouseX+50, mouseY+20);

	//control automatically transferred once you reach the end
	///so no need to have return statement
}
```

and the call,

```java
void draw() {
	background(255);
	drawShip();
}
```

### Effectively Unconditional Return

A function that promises to return a value, must do so *effectively* unconditionally.

Take the following example,

```java
boolean isEven(int n) {
	if(n%2 == 0) {
		return true;
	}
	if(n%2 != 0) {
		return false;
	}
}
```

While mathematically, one of the two boolean expressions (`n%2 == 0` and `n%2 != 0`) WILL be `true`, the programming language doesn't make that optimization. For JavaProcessing, the two return statements are in conditional blocks. Hence, you will get a compilation error - `method must return a value of type boolean`.

To fix this, you should use,

```java
boolean isEven(int n) {
	if(n%2 == 0) {
		return true;
	}
	else {
		return false;
	}
}
```

Now, in terms of programming, either the `if` block, or the `else` block are guaranteed to execute, thereby returning a value unconditionally.

### Statements or Expressions?

  * function declarations are statements.
  * function calls are statements if the function returns `void`.
  * function calls are statements _and_ expressions if they return a value.
  * formal parameters are statements.
  * actual parameters are expressions.

The fact that a function call in processing can _do_ something and also _evaluate to a value_ makes them special.  In fact, this double-life is a bit of a point of friction in language design.  Some languages insist that functions must be statements and others insist they must be expressions, but those are rare.  The situation we have here, while strange, is quite common.

## Furthering our Understanding

{% include youtube.html id="VU284tKC_HY" %}

<!-- Number of digits in an integer -->
{% capture my_problem %}
Define a function that when passed an integer, returns the number of digits in the integer.
{% endcapture %}

{% capture my_solution %}
```java
int digits(int input){
    int totalSoFar = 0;
    while (input > 0) {
        totalSoFar++;
        intput = input / 10;
    }
    return totalSoFar;
}
```
{% endcapture %}

{% include exercise.html
  title="Number of digits in an integer"
  problem=my_problem
  solution=my_solution
%}

<!-- Is Divisible -->
{% capture my_problem %}
Given two integers (store in formal parameters `a, b`), define a function that determines if either of them is divisible by the other. Some input-output mappings are:

  * `a = 14, b = 6` --> return `false`
  * `a = 14, b = 7` --> return `true`
  * `a = 9, b = 30` --> return `false`
  * `a = 9, b = 36` --> return `true`
  * `a = 12, b = 0` --> return `true` (0 is divisible by 12)
{% endcapture %}

{% capture my_solution %}
```java
/*
	We need to check if divisible both ways. That is, a % b and b % a.
	Notice, that taking modulus 0 of a number will crash our program with a "ArithmeticException: / by zero" error.
	We need to only apply the modulus after ensuring the number is not 0 to circumvent that.
*/
boolean isDivisible(int a, int b){
    if(b!=0 && a%b==0) {
    	return true;
    }
    if(a!=0 && b%a==0) {
    	return true;
    }
    return false;
}
```
{% endcapture %}

{% include exercise.html
  title="Is Divisible"
  problem=my_problem
  solution=my_solution
%}

<!-- Leap Years -->
{% capture my_problem %}
A year is leap if it satisfies one of the two conditions,

1. it's divisible by 400, or,
2. it's divisible by 4 but **NOT** by 100.

Define a function that determines if an year passed (store in formal parameter `year`) is `leap`. Return `true` if it's a leap year, and `false` otherwise. Some input-output mappings are:

  * `year = 2016` --> return `true`
  * `year = 1800` --> return `false`
  * `year = 2018` --> return `false`
  * `year = 1600` --> return `true`
{% endcapture %}

{% capture my_solution %}
```java
boolean isLeapYear(int year){
    return (isDivisible(year, 400) || (isDivisible(year, 4) && !isDivisible(year 100)));
}
```
{% endcapture %}

{% include exercise.html
  title="Leap Years"
  problem=my_problem
  solution=my_solution
%}


<!-- Non-trivial divisors -->
{% capture my_problem %}
I would like to count the number of non-trivial (apart from 1 and itself) divisors of a given integer. Some input-output mappings are:

  * `n = 18` --> return `4` (as there are 4 non-trivial divisors: 2, 3, 6, 9)
  * `n = 31` --> return `0` (as there is no non-trivial divisor of 31)
  * `n = 77` --> return `2` (as there are 2 non-trivial divisors: 7, 11)
{% endcapture %}

{% capture my_solution %}
```java
int divisors(int input){
    found = 0;
    for(int i = 2; i < input; i++){
        if (isDivisible(input, i)){
            found++;
        }
    }
    return found;
}
```
{% endcapture %}

{% include exercise.html
  title="Non-trivial divisors"
  problem=my_problem
  solution=my_solution
%}
