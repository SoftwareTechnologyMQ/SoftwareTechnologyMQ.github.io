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

![](./assets/images/important.gif)

First of all, **study** this chapter instead of *skimming over*. I promise you, the hour or so it takes for you to go through it will be worth it by the end of the session.

To begin COMP1010, the three most important skills are:

1. How to [trace control flow](#1-tracing-control-flow) when there are variables conditions, loops, arrays and functions in your program.
2. Be able to [define a basic to intermediate function](#2-define-functions). We assume that if you can define a function, you also know how to call it, which in some cases might not be true, but easily fixable.
3. Be able to [perform basic operations on an array](#3-operating-on-arrays) (Examples below).

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
	if(x/5 == 0) {
		a = sum(x);
	}
	else {
		a = product(x);
	}
	println(a);
}
```

<details class="prereq" markdown="1"><summary>Solution</summary>
Lines 20 -> 21 -> 22 -> 26 -> 11 -> 12 -> 13 > 14 -> 12 -> 13 > 14 -> 12 -> 13 > 14 -> 12 -> 13 > 14 -> 12 -> 16 -> 26 -> 28
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

## Example 2.2

Consider you putting mangoes (or whatever fruit you like) in trays. There are some variables here:

1. How many mangoes are there?
2. How many mangoes can fit in one tray?

Based on that, you'd like to determine how many trays are needed.

The slight twist is that it's possible that not all trays will be full. For example, if you have 45 mangoes, with each tray holding 10 mangoes, you need 5 trays.

Given this scenariom, define a function which when given the required information (think what that is), returns the number of trays required.

<details class="prereq" markdown="1"><summary>Solution</summary>
```java
int nTrays(int nFruits, int traySize) {
	int fullTrays = nFruits/traySize;
	int leftovers = nFruits%traySize;
	if(leftovers > 0) {
		return fullTrays + 1;
	}
	else {
		return fullTrays;
	}
}
```
</details>

Note that in the above solution, we have deliberately "spread" the solution out. We *could* have made it more compact. This is the trade-off between,

1. Spread-out code: Easier to read/explain/debug, but long.
2. Compact code: Short, but harder to read/explain/debug.

For the sake of completeness, here is the compact solution:

```java
int nTrays(int nFruits, int traySize) {
	return (nFruits + traySize - 1) / traySize; 
}
```

Yes, it will work, and is clever, but explaining to someone or debugging is a pain.

Sometimes, the simplest solution is the best solution.

## Example 2.3

Define a function that when passed two integers, returns,

- 1, if they are both positive,
- 2, if neither of them is positive,
- 3, if exactly one of them is positive

<details class="prereq" markdown="1"><summary>Solution</summary>
```java
int positivity(int a, int b) {
	if(a > 0 && b > 0) {
		return 1;
	}
	if(a <= 0 && b <= 0) {
		return 2;
	}
	//since we have eliminated scenarios 1 and 2, only scenario 3 is left
	return 3;
}
```
</details> 


## Activity 2.3

Based on the above example, define a function that when passed three integers, returns the smallest of the three.

<details class="prereq" markdown="1"><summary>Solution</summary>
```java
int smallest(int a, int b, int c) {
	if(a <= b && a <= c) {
		return a;
	}
	//guaranteed that either a > b or a > c so a cannot be the answer
	if(b <= c) {
		return b;
	}
	//guaranteed that b > c so b cannot be the answer either
	return c;
}
```

Note: the following solution will not work because there is no UNCONDITIONAL return, even though, mathematically, it is correct

```java
int smallestBuggy(int a, int b, int c) {
	if(a <= b && a <= c) {
		return a;
	}
	if(b <= a && b <= c) {
		return b;
	}
	if(c <= a && c <= b) {
		return c;
	}
}
```
</details> 

# 3. Operating on arrays

When we create an array, the array name is a *reference* (an indicator of where the items are stored). The memory location where the items are actually stored is called the *instance*.

When two references refer to the same instance, they are called *reference copies*.

When two references refer to two different instances, but the instances are identical, they are called *instance copies*. 

The [compound data lecture](https://softwaretechnologymq.github.io/compound_data) has much more information on this.

Performing simple operations such as finding the sum of all even numbers in an array, or the highest value in an array is something you should be able to do by the time you start COMP1010.

## Example 3.1

Our first example requires us to find the sum of all ODD numbers in an array. You may assume the array, say `data` has already been populated.

The algorithm is,

1. Initialize total to 0.
2. Go through each item of the array	
	1. if the current item is ODD (item%2 != 0, NOT item%2 == 1, since negative odd % 2 is -1, not 1)
		1. Add current item to the total  

Code,

```java
int total = 0;
for(int i=0; i < data.length; i++) {
	if(data[i]%2 != 0) {
		total+=data[i];
	}
}
```

The above code is called an *inline code*. Putting it into a function is hopefully straightforward, as you just need to return the total.

```java
int sumOdds(int[] data) {
	int total = 0;
	for(int i=0; i < data.length; i++) {
		if(data[i]%2 != 0) {
			total+=data[i];
		}
	}
	return total;
}
```

## Activity 3.1 

Based on the above example, write inline, and function versions of finding the number of negative items in an array.

<details class="prereq" markdown="1"><summary>Solution</summary>
```java
int count = 0;
for(int i=0; i < data.length; i++) {
	if(data[i] < 0) {
		count++;
	}
}
```

The above code is called an *inline code*. Putting it into a function is hopefully straightforward, as you just need to return the total.

```java
int countNegatives(int[] data) {
	int count = 0;
	for(int i=0; i < data.length; i++) {
		if(data[i] < 0) {
			count++;
		}
	}
	return count;
}
```
</details> 

## Example 3.2

Our second example is to check the highest item in an array. Return 0 if array is empty.

Algorithm version 1 (buggy):

1. Assume the highest item so far is 0.
2. Go through each item of the array.
	1. If the current item is more than the highest item so far
		1. Highest item so far is updated to the current item

While the algorithm looks ok, it will fail for the array {-1, -7, -2, -9} as none of the items is more than 0.

Algorithm version 2 (buggy too):

1. Assume the highest item so far is the first item.
2. Go through each item of the array.
	1. If the current item is more than the highest item so far
		1. Highest item so far is updated to the current item

The above algorithm will fail for an empty array when trying to assign the first, non-existent item, to highest item so far.

Algorithm version 3:

1. If array is empty
	1. Return 0 (as per specs)
2. Assume the highest item so far is the first item.
3. Go through each item of the array.
	1. If the current item is more than the highest item so far
		1. Highest item so far is updated to the current item


Here, we directly write the function version.

```java
int highest(int[] data) {
	if(data == null || data.length == 0) {
		return 0;
	}
	int result = data[0];
	for(int i=1; i < data.length; i++) {
		if(data[i] > result) {
			result = data[i];
		}
	}
	return result;
}
```

## Activity 3.2

Define a function that when passed an array, returns `true` if all items are positive, `false` otherwise. Return `true` if the array is empty (a ceoncept known as *vacuous truth*)
		
<details class="prereq" markdown="1"><summary>Solution</summary>
The logic is to find a single violation (an item that is NOT positive), and return `false` immediately. If no violations (that is, AFTER the loop), return `true`.

```java
boolean allPositives(int[] data) {
	for(int i=0; i < data.length; i++) {
		if(data[i] <= 0) { //a single violation
			return false;l
		}
	}
	return true;
}
```
</details> 
