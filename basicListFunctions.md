---
layout: page
title: Lists
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge</summary>

  * <a href="composite_data">Composite Data</a>
  * <a href="composite_data">Recursion</a>
</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes</summary>

  * Understand the underlying features of lists and how they differ from arrays.
  * Be able to use built-in Java lists
  * Be able to build a custom list class
  * Understand the time costs of various list operations
</details>

# What are lists?

Lists are data structures, much like arrays. The differences being,

### 1. Lists must hold objects

Arrays can hold a collection of primitive data types or a collection of objects, while lists can hold a collection of objects, **not** primitive data types.

### 2. Lists grow as required

The size of array needs to be specified at the time of creating an array. The size of a list need not be specified. You can add as many items as you want to a list (permitting system memory).

### 3. Lists have a range of instance methods

With arrays (assuming array name is `arr`), the only operators you have to work with are `arr.length` and `arr[i]`. Anything and everything you need to do must be done using these two operators. Several life-saving methods are applicable on list objects, such as:

- `get(int)` //similar to arr[i]
- `size()` //similar to arr.length
- `add(Object)`	//add item at the end of the list
- `remove(Object)` //parameter represents item to be removed
- `remove(int)` //parameter represents index
- `indexOf(Object)` //parameter represents item being searched
- `lastIndexOf(Object)` //parameter represents item being searched

# Why are arrays not good enough?

## Example - copying over a subset

Consider an array `src` holding 100 integers. Some negative, some positive.
We need to copy all negative items over to a new array `dest`.

As an example, if

`src` is `{10, 20, 50, 0, -40, 30, 90, 60, -10, -50, 80}`

`dest` should be `{-40, -10, -50}`

In order to do this, we need to,

1. Count the number of required (negative) values in the array `src`
2. Create an array `dest` of that size
3. Copy items over to `dest`.

### Step 1

```java
int count = 0;
for(int i=0; i < src.length; i++) {
	if(src[i] < 0) {
		count++;
	}
}
```

### Step 2

```java
int[] dest = new int[count];
```


### Step 3

We are copying,

`src[4]` into `dest[0]`

`src[8]` into `dest[1]`

`src[9]` into `dest[2]`

So, in addition to the current index of `src`, we also need to keep track of the current index of `dest` into which the item must be copied.

```java
int idx = 0; //index where item must be copied
for(int i=0; i < src.length; i++) {
	if(src[i] < 0) {
		dest[idx] = src[i]; //another item copied
		idx++; //move destination index forward
	}
}
```

### Final solution

```java
int count = 0;
for(int i=0; i < src.length; i++) {
	if(src[i] < 0) {
		count++;
	}
}

int[] dest = new int[count];

int idx = 0; //index where item must be copied

for(int i=0; i < src.length; i++) {
	if(src[i] < 0) {
		dest[idx] = src[i]; //another item copied
		idx++; //move destination index forward
	}
}
```

### Solution using List (just focus on how easy and intuitive it is)

A solution to the same problem when `src` and `dest` are lists instead of arrays is,

```java
ArrayList<Integer> dest = new ArrayList<Integer>();
for(int item: src) {
	if(item < 0) {
		dest.add(item);
	}
}
```

<!--## Example 2 - reading student names outcomes from a file

Consider a file that holds student names in the format `FIRST_NAME LAST_NAME`.
A sample file looks something like:

```
Cedric Diggory
Alvaro Morata
Rose Granger-Weasley
Albus Potter
Luna Lovegood
Lionel Messi
```

In order to store the names in an array, we need to do one of two things,

1. Create a String array so big that it will definitely be big enough to hold all items from the file.
2. Traverse the file once to count the number of names, then create an array of that size, and then traverse the file again, adding the items in the array.
-->
