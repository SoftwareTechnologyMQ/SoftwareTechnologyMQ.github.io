---
layout: page
title: Handling null arrays
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge</summary>

  * <a href="compound_data">Compound Data</a>
</details>
  * <a href="multi_dimensional_arrays">Multi-dimensional Arrays</a>
</details>
<details class="outcomes" markdown="1"><summary>Learning Outcomes</summary>

  * Understand why and how to perform `null` checks on arrays.
</details>

# Author: Gaurav Gupta

The first thing one must understand is that the "contents" of an array is a reference to the memory location where the items are stored. The *name* of the array is the *reference* while the actual collection of items is the *instance*.

This has been emphasized under [Compound Data](https://softwaretechnologymq.github.io/compound_data).

Second - things will be much much easier if you draw memory diagrams (as shown in [Compound Data](https://softwaretechnologymq.github.io/compound_data).

Let's dig in!

What happens when you declare an integer variable and print it?

```java
int a;
println(a); //compilation error
```

It will give you a compilation error: The local variable `a` may not have beenin itialized. To pacify Processing (or Java), you must initialize it to some value. 

Similarly, with an array, you must initialize it with a value. The special value `null` means the array (or in general, the object) has been declared but is not ready to refer to an instance. 

```java
int[] data;
println(data); //compilation error
```

```java
int[] data = null;
println(data); //will display null
```

Since a `null` array (or, in general, object) does not refer to an instance yet, it doesn't have any `length` attribute.

```java
int[] data = null;
println(data.length); //NullPointerException
```

And obviously, you cannot access its items either:

```java
int[] data = null;
println(data[0]); //NullPointerException
```

# Lesson 1: Before we access the `length` attribute of an array, we must ensure it's not `null`.

```java
//UNSAFE:
for(int i=0; i < data.length; i++) {
	//access item at index i
}
```

```java
//SAFE:
if(data != null) {
	for(int i=0; i < data.length; i++) {
		//access item at index i
	}
}
```

Similarly, for a two-dimensional array, either the 2d array itself can be `null` or one or more of its subarrays can be `null`. Following are two versions of a program that store the sum of all items in a variable `total`, the first one unsafe, and the second one safe.

## Version 1 (Unsafe)

```java
int total = 0;
for(int i=0; i < twoDimArray.length; i++) {
	for(int k=0; k < twoDimArray[i].length; k++) {
		total+=twoDimArray[i][k];
	}
}
```

Some of the examples for which the above code will generate run-time errors are:

```java
int[] taxi = null;
int[] cab = { {10, 70}, null, {20, 90} };
```


## Version 2 (Safe)

```java
int total = 0;
if(twoDimArray != null) {
	for(int i=0; i < twoDimArray.length; i++) {
		if(twoDimArray[i] != null) {
			for(int k=0; k < twoDimArray[i].length; k++) {
				total+=twoDimArray[i][k];
			}
		}
	}
}
```

This code will work for all possible two-dimensional sub-arrays such as:


```java
int[] data = {10, 70, 20, 90};
int[] taxi = null;
int[] cab = { {10, 70}, null, {20, 90} };
int[] mixedBag = { {10, 70, 20}, null, {90}, null, {} };
```

# Moral of the story: 

1. Always check an array is NOT null before accessing its length, and, 
2. Always check the index is within bounds before accessing an item at that index (our loop expressions are doing that in the above examples).