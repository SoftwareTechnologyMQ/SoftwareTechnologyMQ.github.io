---
layout: page
title: "Foundation for COMP1010"
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge</summary>

  * Variables
  * Conditions
  * Loops
  * Functions
  * Arrays
</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes</summary>

  * Understand any gaps in knowledge required to begin COMP1010 satisfactorily.

</details>

## Author: Gaurav Gupta

# What do you need to know to begin COMP1010?

To begin COMP1010, you need to know the following things:

1. How to [trace control flow](#1-tracing-control-flow) when there are variables conditions, loops, arrays and functions in your program.
2. Be able to [define a basic to intermediate function](#2-define-functions). We assume that if you can define a function, you also know how to call it, which in some cases might not be true, but easily fixable.
3. Be able to perform basic operations on an array (Examples below).

# 1. Tracing control flow

## Example 1

See the following example where we trace the flow of control of the following Processing program.

```java
void setup() {
	int a = 20, b = 5;
	if(a % b == 0) {
	   println("divisible");
	}
	else {
	   println("not divisible");
	}
	println("Ciao!");
}
```

First function to execute (and in this case the only function) is `setup()`. 

1. Line 2 is the first statement inside that function.
2. Next statement is on line 3. The boolean expression here evaluates to `true`. So it goes into the if-block.
3. The only statement inside the if-block is on line 4.
4. Exits the if-block and executes statement on line 9.

Thus, the lines executed are:

```
2 -> 3 -> 4 -> 9
```

Note that function headers, lines with JUST curly brackets (opening or closing), and empty lines are not considered while tracing.

Also, note our program doesn't have a `draw()` function, which is also fine.

## Activity 1.1

Based on our walkthrough, trace the flow of the following program and summarize with the sequence of lines that are executed.

```java
void setup() {
	int a = -7;
	if(a > 0) {
	   	println("Positive");
	}
	else {
		if(a == 0) {
			println("Zero (Non-positive, non-negative)");
		}
		else {
			println("Negative");
		}
	}
	println("Ciao!");
}
```

<details class="prereq" markdown="1"><summary>Solution</summary>
```
Lines 2 -> 3 -> 7 -> 11 -> 14
```
</details>

## Example 2

See the following example where we trace the flow of control of the following Processing program.

```java
int mystery(int n) {
	if(n%2 == 0) {
		return n+1;
	}
	else {
		return n-1;
	}
}

void setup() {
	int a = 1729;
	int b = mystery(a);
	println(b);
}

float average(int a, int b) {
   return (a+b)/2.0;
}
```

1. The first function to execute is `setup()` and hence the first STATEMENT to execute is `int a = 1729;` (line 11).
2. Next statement to execute is `int b = mystery(a);` on line 12 that transfers the control to the `mystery` function by passing the value of `a` into formal parameter `n`. The memory space where the formal parameter and other local variables in the context of a function call are held, is called *stack frame*.
3. Line 2 is the first to execute inside `mystery(1729)` stack frame. The boolean expression inside the condition-header evaluates to `false`. Hence, the else-block executes next.
4. Line 6 (`return n-1;`) is the only statement inside the else-block which returns 1728 to the calling statement (line 12). The stack frame for `mystery(1729)` is now deleted. The value returned replaces the call, effectively turning the statement into `int b = 1728;`. 
5. The last line of the program executes (line 13).
6. The function `average` is never called which is fine. There can be functions in your program that are never invoked.

If we summarize the above trace, the lines executed are:

```
11 -> 12 -> 2 -> 6 -> 12 -> 13
```

Wow! That's a very few lines actually being executed for a relatively large piece of code. And that is absolutely true of any code that has lots of conditions.

## Activity 1.2

Based on our walkthrough, trace the flow of the following program and summarize with the sequence of lines that are executed.

```java	
int square(int n) {
   int result = n*n;
   return result;
}

int cube(int n) {
   int result = n*n*n;
   return result;
}

void setup() {
	int x = 2;
	int y = cube(x);
	int z = square(y);
	println(x+" "+y+" "+z);
}
```

<details class="prereq" markdown="1"><summary>Solution</summary>
Lines 12 -> 13 -> 7 -> 8 -> 13 -> 14 -> 2 -> 3 -> 14 -> 15
</details>

## Example 3

```java
void setup() {
	int n = 4;
	int result = 0;
	for(int i=1; i<=n; i++) {
		result+=i;
	}
	println(result);
}
```
   
1. Line 2
2. Line 3
3. Line 4 - loop encountered, `i` initialized, loop expression checked. Is `true`.
4. Line 5
5. Line 4 - loop variable updated, loop expression checked again. Is `true`.
6. Line 5
7. Line 4 - loop variable updated, loop expression checked again. Is `true`.
8. Line 5
9. Line 4 - loop variable updated, loop expression checked again. Is `true`.
10. Line 5
11. Line 4 - loop variable updated, loop expression checked again. Is `false`.
12. Line 7

```
2 -> 3 -> 4 -> 5 -> 4 -> 5 -> 4 -> 5 -> 4 -> 5 -> 4 -> 7
```

A code that has a lot of loops will **often** have many more statements executed than lines in the program.

## Activity 1.3

Based on our walkthrough, trace the flow of the following program and summarize with the sequence of lines that are executed.

```java
void setup() {
	int a = 42;
	int b = 12;
	while(b != 0) {
		int temp = a%b;
		a = b;
		b = temp;
	}
	println(a);
}
```

<details class="prereq" markdown="1"><summary>Solution</summary>
Lines 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 4 -> 5 -> 6 -> 7 -> 4 -> 9 (loop executes twice)
</details>

## Activity 1.4

Now, all (conditions, functions, loops together)

```java
int sum(int n) {
	int result = 0;
	while(n > 0) {
		result+=n;
		n--;
	}
	return result;
}

int product(int n) {
	int result = 1;
	while(n > 1) {
		result*=n;
		n--;
	}
	return result;
}

void setup() {
	int x = 5;
	int a = 0;
	if(x%5 == 0) {
		a = sum(x);
	}
	else {
		a = product(x);
	}
	println(a);
}
```

<details class="prereq" markdown="1"><summary>Solution</summary>
Lines 20 -> 21 -> 22 -> 26 -> 11 -> 12 -> 13 > 14 -> 12 -> 13 > 14 -> 12 -> 13 > 14 -> 12 -> 13 > 14 -> 12 -> 26 -> 28
</details>

# 2. Define functions

A function is a contract. If it receives the type of values it expects, it promises to give you an answer (return value). There are two things to identify in a function:

1. Parameters (type of values a function expects)
2. Return type (type of the answer it will give)

## Example 2.1

Define a function that when passed an integer, returns its last digit.

The key skill you need to have to solve this problem is to know the `%` operator. It gives you the remainder. So `a%10` gives remainder when `a` is divided by 10, which is the last digit.

### Attempt 2.1.1

```java
int lastDigit(int n) {
	int result = n%10; 
	return result;
}
```

Here, the function will return the correct value if `n = 1729` but if `n = -1729`, it will return `-9` which is not really the last digit. This is because `negative % 10` is `negative`.

### Attempt 2.1.2

```java
int lastDigit(int n) {
	if(n < 0) {
		n = -n;
	}
	return n%10;
}
```

We just made sure `n` is non-negative before applying the `%` operator.

### Variation of attempt 2.1.2

Following is an equivalent version - just different style. We are performing the "moderation" on the result, rather than the input.

```java
int lastDigit(int n) {
	int result = n%10;
	if(result < 0) {
		return -result;
	}
	else {
		return result;
	}
}
```

## Activity 2.1

Based on the above example, define a function which when passed an integer, returns `true` if it is positive (think about whether you really know what defines a positive number), `false` otherwise.

<details class="prereq" markdown="1"><summary>Solution</summary>
```java
boolean isPositive(int n) {
	if(n > 0) { //not n >= 0
		return true;
	}
	else {
		return false;
	}
	//also valid: return n > 0; //as the outcome of n > 0 is what you are returning
}
```
</details>