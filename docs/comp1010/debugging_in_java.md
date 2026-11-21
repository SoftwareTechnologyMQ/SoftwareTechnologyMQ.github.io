---
title: Debugging in Java
permalink: /comp1010/debugging
parent: COMP1010
nav_order: 3
---

<!-- Assumed Knowledge -->
{% capture topic_prereq %}
  * [Transition to Java]({{ site.baseurl }}/comp1010/transition-to-java)
{% endcapture %}
<!-- Learning Outcomes -->
{% capture topic_outcomes %}
  * Be able to identify input/output pairs that are good for debugging.
  * Be able to debug Java programs with appropriate tools.
  * Be able to do paper traces of Java code.
{% endcapture %}

{% include prereq_outcomes.html prereq=topic_prereq outcomes=topic_outcomes %}

For any given problem, we design a solution and then implement it.

As an example, let's say that we are writing a program that gives you the number of digits in an integer. We expect the following *input-output mappings*.


| Input      | Output |
|------------|--------|
| 1729       | 4      |
| 1234567890 | 10     |
| 0          | 0      |
| -888       | 3      |
{: .table}

Now, it's possible that the actual outputs you get from your code are as follows,

| Input      | Output |
|------------|--------|
| 1729       | 4      |
| 1234567890 | 10     |
| 0          | 1      |
| -888       | 4      |
{: .table}

We need to find out why do some inputs have incorrect outputs. So we go through our design and implementation looking for possible bugs. A logical way to do this is to trace every variable at every stage and see where the program deviates from the expected.

## Example 1

Consider the following code that is supposed to return the product of all integers from 1 to `n` (`n` >= 1).
```java
/**
 * @param n >= 1
 * @return product of integers from 1 to n (including 1 and n).
 */
public static int factorial(int n) {
    int result = 0;
    for(int i=1; i < n; i++) {
        result = result * i;
    }
}
 ```

<!-- <script src="https://gist.github.com/gaurav1780/71d8008cd4cc632dc6119b1594dcfe88.js"></script> -->

The input-output mappings are -

| Input      | Expected Output | Actual Output |
|------------|--|---|
| 4       | 24 	| 0 |
| 6 		| 720 	| 0 |
| 7      	| 5040	| 0 |
| 1      	| 1 	| 0 |
{: .table}

If you trace the program, you'll see that the loop executes when `i=1` and `result` becomes `result (0) * i (1) = 0`. And every subsequent time, `result` becomes `0 * i = 0`. A trace for `n=4` using *logic table* is provided below,

| i | i < 4 | result |
|---|-------|--------|
| 1 |  true | 0\*1 = 0|
| 2 |  true | 0\*2 = 0|
| 3 |  true | 0\*3 = 0|
| 4 |  false | |
{: .table}

Thus, the first bug is that `result` should be initalized to 1 and not 0.

Our partially fixed code:

```java
/**
 * @param n >= 1
 * @return product of integers from 1 to n (including 1 and n).
 */
public static int factorial(int n) {
    int result = 1; //fixed initial value of result
    for(int i=1; i < n; i++) {
        result = result * i;
    }
}
```

<!-- <script src="https://gist.github.com/gaurav1780/526b68d197c7c3a705780af2fcef93c1.js"></script> -->

The new input-output mappings are,

| Input      | Expected Output | Actual Output |
|------------|--|---|
| 4       | 24 	| 6 |
| 6 		| 720 	| 120 |
| 7      	| 5040	| 720 |
| 1      	| 1 	| 1 |
{: .table}

A trace for `n=4` using *logic table* is provided below,

| i | i < 4 | result |
|---|-------|--------|
| 1 |  true | 1\*1 = 1|
| 2 |  true | 1\*2 = 2|
| 3 |  true | 2\*3 = 6 (not the expected output)|
| 4 |  false | |
{: .table}

It can now be seen that the loop **should** execute for `i=4` and multiply it into the `result` but it doesn't. By changing `i < n` to `i <= n`, we fix this problem.

```java
/**
 * @param n >= 1
 * @return product of integers from 1 to n (including 1 and n).
 */
public static int factorial(int n) {
    int result = 1; //fixed initial value of result
    for(int i=1; i <= n; i++) {
        result = result * i;
    }
}
```

<!-- <script src="https://gist.github.com/gaurav1780/331fb94f328322b2fc4bd781ef22d18e.js"></script> -->

To confirm, we trace once more for `i=4`.

| i | i < 4 | result |
|---|-------|--------|
| 1 |  true | 1\*1 = 1|
| 2 |  true | 1\*2 = 2|
| 3 |  true | 2\*3 = 6|
| 4 |  true | 6\*4 = 24 (expected output)|
| 5 |  false | |
{: .table}

QUESTION:
Debug the following method for which the expected input-output mappings are provided in the javadoc (comment above the method).

SOLUTION:

{: .highlight}
**CRITICAL STEP!!!** Write down the actual input-output mappings after every iteration of debugging.

```java
public static boolean allPositives(int[] arr) {
    for(int i=0; i < arr.length; i++) { //(first item is at index 0 not 1)
        if(arr[i] <= 0) //check if the current item is NOT positive
            return false; 
        /*
            if it IS positve, you cannot return true immediately 
            as one or more of the subsequent items might not be!
        */
    }
    //loop ended, means all items checked, none NOT positive
    return true;
}
```

<!-- <script src="https://gist.github.com/gaurav1780/7556eea66978a974423447f544150841.js"></script> -->
 
## Performing Debugging in Popular IDEs

Most of the modern Integrated Development Environments (IDEs) have a comprehensive debugging feature that lets you trace the variables as your program executes.

The debugger relies of placing `breakpoints` that are like pitstops in a car race. The program runs till the next breakpoint where you can see the values of all the variables and when you hit `resume`, it goes to the next breakpoint.

## Visual Studio Code

{% include youtube.html id="zZ8ofDJeizs" %}

## Eclipse

{% include youtube.html id="NQTQVYhmsL0" %}

# Pen and paper methodology

At this point, it becomes tempting to throw away your notebook, you have everything you need in the programming environment, right?

No!

Debugging is still mostly done in your head or on paper, so it is worth revisiting our programming tracing skills.  What follows is a set of exercises for you to get familiar with tracing Java code.  You should do all these exercises with just a pen/pencil and paper as the skill you are training is to be able to trace a program _without_ the aid of a computer.

QUESTION:
Trace the flow of the following program and determine the value of `result` at the end of it.

```java
int a = 5;
int b = 10;
int result;
if(a < b && b % a == 0 && a % 2 == 0) { //b should be divisible by a and a should be even
	result = a;
}
else {
	result = b;
}
```

<!-- <script src="https://gist.github.com/gaurav1780/767824769b5456ddb080e63d84124d70.js"></script> -->

SOLUTION:
`a < b` is `true`

`b % a == 0` is `true`

`a % 2 == 0` is `false`

The expression becomes `true && true && false`

This is `false`

Hence, the `else` block executes, and `result` becomes `b (10)`.


QUESTION:
Trace the flow of the following program and determine the value of `result` at the end of it.

```java
int a = 5, b = 10;
int result = 0;
if(a == b) { //check for equality
	result = a;
}
else {
	b = b - a;
	if(a == b) {
		result = b;
	}
}
```

<!-- <script src="https://gist.github.com/gaurav1780/0f335474bbbf8fcf488150b7b411c33a.js"></script> -->

SOLUTION:
`a == b` is `false`,
`else` executes

`b` decreases by 5, becomes 5
`a == b` is `true`.
`if` block executes and `result` becomes `b (5)`.

QUESTION:
Trace the flow of the following program and determine the value of `result` at the end of it.

```java
int result = -3;
for(int i=1; i <= 7; i++) {
	if(i%2 == 1) { //is i an odd number?
		result = result + i;
	}
}
```

<!-- <script src="https://gist.github.com/gaurav1780/0302ce7e20a43b1807584b4ca7f49ce7.js"></script> -->

SOLUTION:

<table>
    <tr>
        <td>i</td>
        <td>i &lt;= 7</td>
        <td>i%2</td>
        <td>i%2==1</td>
        <td>result</td>
    </tr>
    <tr>
        <td>1</td>
        <td>true</td>
        <td>1</td>
        <td>true</td>
        <td>-3+1 = -2</td>
    </tr>
    <tr>
        <td>2</td>
        <td>true</td>
        <td>0</td>
        <td>false</td>
        <td></td>
    </tr>
    <tr>
        <td>3</td>
        <td>true</td>
        <td>1</td>
        <td>true</td>
        <td>-2+3 = 1</td>
    </tr>
    <tr>
        <td>4</td>
        <td>true</td>
        <td>0</td>
        <td>false</td>
        <td></td>
    </tr>
    <tr>
        <td>5</td>
        <td>true</td>
        <td>1</td>
        <td>true</td>
        <td>1+5 = 6</td>
    </tr>
    <tr>
        <td>6</td>
        <td>true</td>
        <td>0</td>
        <td>false</td>
        <td></td>
    </tr>
    <tr>
        <td>7</td>
        <td>true</td>
        <td>1</td>
        <td>true</td>
        <td>6+7 = 13</td>
    </tr>
    <tr>
        <td>8</td>
        <td>false</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>

QUESTION:
Trace the flow of the following code -

```java
int a = 4, b = 12, c = 3;
boolean d = false;
int result = 4;
if(a > b || b % c == 0) {
	if(d == true) {
		result = result + 1;
	}
	else {
		result = result - 1;
	}
	result = result * 2;
}

if(d == false && a == b/c) {
	result = result + 1;
	a = a + 1;
	d = true;
}

if(d == false && a == b/c) {
	result = result + 2;
}
else {
	b = b - 2;
	c = c - 1;
	d = false;
}

if(d == false && a == b/c) {
	result = result + 3;
}
```

<!-- <script src="https://gist.github.com/gaurav1780/0b8969cabc916cff8ed88cfcde631560.js"></script> -->

SOLUTION:
At the end of the code,
`a = 5`, `b = 10`, `c = 2`, `d = false`, `result = 10`.
Explanation -

```java
int a = 4, b = 12, c = 3;
boolean d = false;
int result = 4;
if(a < b || b % c == 1) {
	//a < b: false, b%c==0: true, false || true: true
	if(d == true) { //false == true: false
		result = result + 1;
	}
	else { //else block executes
		result = result - 1; //result becomes 4 - 1 = 3
	}
	result = result * 2; //result becomes 3 * 2 = 6
}

if(d == false && a == b/c) {
	//false==false: true, 4 == 12/3: true, true && true: true
	result = result + 1; //result becomes 6 + 1 = 7
	a = a + 1; //a becomes 4 + 1 = 5
	d = !d; //d becomes !false (true)
}

if(d == false && a == b/c) {
	//true==false: false, false && anything: false
	result = result + 2;
}
else { //else block executes
	b = b - 2; //b becomes 12-2 = 10
	c = c - 1; //c becomes 3-1 = 2
	d = !d; //d becomes !true (false)
}

if(d == false && a == b/c) {
	//false==false: true, 5==10/2: true, true&&true: true
	result = result + 3; //result becomes 7+3 = 10
}
```

<!-- <script src="https://gist.github.com/gaurav1780/7edd01a8e4ae3182e3ddd7f6166a0e53.js"></script> -->

# Relevant MQ Videos

{: .note}
The videos below include JUnit testing in Eclipse as well as VS Code. It is recommended you watch both, as the Eclipse video provides foundational information on using JUnit. Also, it's good to get familiar with some of the differences of working with different IDEs.

{% include youtube.html id="iFJwFq_KmXY" %}

{% include youtube.html id="iFJwFq_KmXY" %}

{% include youtube.html id="jWwRRzU5hfA" %}

{% include youtube.html id="e9Oj08kgd4A" %}

{% include youtube.html id="Yq_a35_skpw" %}
