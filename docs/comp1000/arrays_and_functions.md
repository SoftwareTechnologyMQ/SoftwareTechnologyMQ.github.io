---
title: Arrays and Functions
permalink: /comp1000/arrays-and-functions
parent: COMP1000
nav_order: 14
---

- TOC
{:toc}


<!-- Assumed Knowledge -->
{% capture topic_prereq %}

  * [Variables]({{ site.baseurl }}/comp1000/variables)
  * [Conditions]({{ site.baseurl }}/comp1000/conditions)
  * [Loops]({{ site.baseurl }}/comp1000/loops)
  * [Arrays]({{ site.baseurl }}/comp1000/arrays)
{% endcapture %}
<!-- Learning Outcomes -->
{% capture topic_outcomes %}
  * Understand how to pass arrays to, and return arrays from, functions
{% endcapture %}

{% include prereq_outcomes.html prereq=topic_prereq outcomes=topic_outcomes %}

# Passing an array to a function

When you pass an array to a function, a reference copy of the actual parameter is made into the formal parameter. Thus, the array inside the function refers to the same array that was passed.

```java
void setup() {
	int[] data = {10, 70, 20, 90};
	int sum = total(data); //outputs 190
}

int total(int[] arr) {
	int result = 0;
	for(int i=0; i < arr.length; i++) {
		result+=arr[i];
	}
	return result;
}
```

Here, `arr` is a reference copy of `data`.
<img src="{{ site.baseurl }}/assets/comp1000/arrays-and-functions/passingArrayToFunction1.png" alt="Passing Array to Function Example 1"/>


Another example:
<img src="{{ site.baseurl }}/assets/comp1000/arrays-and-functions/passingArrayToFunction2.png" alt="Passing Array To Function Example 2"/>


## Modifying array contents inside a function

When you modify the **contents of** an array inside a function, the **contents of** the passed array are also modified, because we are operating on the reference copy (see previous diagram).

```java
void setup() {
	int[] data = {10, 70, 20, 90};
	negate(data);
	for(int i=0; i < data.length; i++) {
		print(data[i]+" ");
	} //outputs -10 -70 -20 -90
}

void negate(int[] arr) {
	int result = 0;
	for(int i=0; i < arr.length; i++) {
		arr[i]*=-1;
	}
}
```

<img src="{{ site.baseurl }}/assets/comp1000/arrays-and-functions/modifyingArrayContentsInsideFunction.png" alt="Modifying array Contents"/>


## Modifying an array itself inside a function

When you modify (re-reference) the array itself inside a function, the passed array is NOT modified, because we re-referenced the reference copy.

```java
void setup() {
	int[] data = {10, 70, 20, 90};
	expand(data);
	for(int i=0; i < data.length; i++) {
		print(data[i]+" ");
	} //outputs 10 70 20 90
}

void expand(int[] arr) {
	arr = new int[10];
}
```

<img src="{{ site.baseurl }}/assets/comp1000/arrays-and-functions/modifyingArrayInsideFunction.png" alt="Modifying Array Inside Function"/>

## Returning an array from a function

You can always create an array and return it from a function

### Example 1 (with memory diagram)
<img src="{{ site.baseurl }}/assets/comp1000/arrays-and-functions/functionReturningArray.png" alt="Example 1"/>


### Example 2

```java
void setup() {
	int[] data = {10, 70, -20, -90, 30, 80, 60, 0, -50};
	
	int[] sub = getFirst(data, 4);
	
	for(int i=0; i < sub.length; i++) {
		print(sub[i]+" ");
	} //outputs 10 70 -20 -90
	
	int[] bar = getFirst(data, 2);
	for(int i=0; i < bar.length; i++) {
		print(bar[i]+" ");
	} //outputs 10 70
	
	
	for(int i=0; i < data.length; i++) {
		print(data[i]+" ");
	} //outputs 10 70 -20 -90 30 80 60 0 -50
}

int[] getFirst(int[] arr, int n) { //we assume n>=0, n<arr.length
	int[] result = new int[n];
	for(int i=0; i < n; i++) {
		result[i] = arr[i];
	}
	return result;
}
```

### Example 3

```java
void setup() {
	int[] data = {10, 70, -20, -90, 30, 80, 60, 0, -50};
	
	int[] negs = getNegativeItems(data);
	
	for(int i=0; i < negs.length; i++) {
		print(negs[i]+" ");
	} //outputs -20 -90 -50
	
	for(int i=0; i < data.length; i++) {
		print(data[i]+" ");
	} //outputs 10 70 -20 -90 30 80 60 0 -50
}

int[] getNegativeItems(int[] arr) {
	int count = 0;
	for(int i=0; i < arr.length; i++) {
		if(arr[i] < 0) { //negative
			count++;
		}
	}
	
	int[] result = new int[count]; 
	
	int destIndex = 0;
	for(int i=0; i < arr.length; i++) {
		if(arr[i] < 0) { //negative
			result[destIndex] = arr[i];
			destIndex++;
		}
	}
	return result;
}
```

## Exercise 1

Complete the following function definition. The name of the function clearly indicates what is expected from the function.

```java
int countPositiveItems(float[] data) {
	int result = 0;
  for(int i=0; i < data.length; i++) {
    if(TRUE) { //replace TRUE with a boolean expression that checks if the current item is positive
      result+=data[i];
    }
  }
  return result;
}
```

## Exercise 2

Define a function that when passed an integer array, returns the number of odd numbers in the array.

## Exercise 3

Define a function that when passed two boolean arrays, returns `true` if they contain the same number of items, `false` otherwise. 

## Exercise 4

Define a function that when passed two floating-point arrays that are guaranteed to be of the same lengths, returns an array where each item is the product of the corresponding items in the passed arrays.

For example, if the arrays passed are `{1.2, 1.5, 1.3}` and `{1.8, 1.6, 1.9}`, the array returned should be `{1.2*1.8, 1.5*1.6, 1.4*1.9}`.

## Exercise 5

Define a function that when passed a `char` array, returns the reverse of the array. The array passed should NOT be modified.

## Exercise 6

Define a function that when passed an integer (say, `n`), returns an array that holds the first `n` prime numbers.
For example, if `n = 5`, return the array `{2, 3, 5, 7, 11}`.

