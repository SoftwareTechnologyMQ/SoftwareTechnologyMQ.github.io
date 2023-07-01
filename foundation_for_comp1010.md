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

1. How to trace control flow when there are variables conditions, loops, arrays and functions in your program.
2. Be able to define a basic to intermediate function (Examples below). We assume that if you can define a function, you also know how to call it, which in some cases might not be true, but easily fixable.
3. Be able to perform basic operations on an array (Examples below).

# 1. Tracing control flow

See the following basic example where we trace the flow of control of the following Processing program.

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

Note that function headers, lines with JUST curly brackets (opening or closing), and empty lines are not considered while tracing.

Also, note our program doesn't have a `draw()` function, which is also fine.

# Now, you do it - 1

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

