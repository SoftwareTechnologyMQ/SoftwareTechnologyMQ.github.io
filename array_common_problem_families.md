---
layout: page
title: Classification Of Array-Based Problems
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge:</summary>

  * [Transition to Java](./transition_to_java)
  * [Compound Data](./composite_data)

</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes:</summary>

  * Identify the basic categories of array-based problems.
  * Quickly put a new problem into one of the categories to apply the *standardized* template.
  * Save time and energy by doing so.
</details>

# Classification Of Array-Based Problems

# Why talk about this?

In programming, we have to operate on collections very frequently. These collections are stored as arrays, lists, maps, dictionaries, tuples, etc.

What is important is a sound understanding of the underlying logic.

By realizing that most of the problems we'll encounter at this level (COMP1010) will lie in a handful of categories, and practising with these, we can improve our familiarity and save time and effort when we need to solve them.

So, let's jump in.

NOTE: the twenty problems I am using are just examples for demonstration purposes. You can have practically infinite problems belonging to one category.

## CATEGORY 1: Counting based on criteria

Consider the following examples (some might be equivalent but phrased differently),

1. Count the number of items in an array that are positive.
2. Count the number of items in an array that are negative.
3. Count the number of items in an array that are zero.
4. Count the number of items in an array that are non-zero.
5. Count the number of items in an array that are non-positive.
6. Count the number of items in an array that are non-negative.
7. Count the number of items in an array that are even.
8. Count the number of items in an array that are odd.
9. Count the number of items in an array that are even and positive.
10. Count the number of items in an array that are even or positive.
11. Count the number of items in an array that are neither even nor positive.
12. Count the number of items in an array that are even but not positive.
13. Count the number of items in an array that are odd but not negative
14. Count the number of items in an array that are even but non-zero.
15. Count the number of items in an array that are odd but non-zero.
16. Count the number of items in an array that are even or non-zero.
17. Count the number of items in an array that are odd or non-zero.
18. Count the number of items in an array that are neither odd nor zero.
19. Count the number of items in an array that are neither even nor zero.
20. Count the number of items in an array that are neither even nor non-zero.

And this is just in the context of two criteria (sign, divisibility by two).

What's common in all these problems is that,

1. have a counter to hold the final answer.
2. we need to go through and check EACH item of the array.
3. if the current item satisfies the criteria, increase the counter by 1.
4. when the loop terminates, return this counter.

So the generic code body would be,

```java
int counter = 0;
for(int i=0; i < data.length; i++) {
	if(check something on data[i]) {
		counter++;
	}
}
return counter;
```

As the first example, the part where you check something on `data[i]` is provided for some of the problems.

1. Count the number of items in an array that are positive: `data[i] > 0`.
2. Count the number of items in an array that are negative: `data[i] < 0`.
3. Count the number of items in an array that are zero: `???`
4. Count the number of items in an array that are non-zero: `data[i] != 0`.
5. Count the number of items in an array that are non-positive: `???`
6. Count the number of items in an array that are non-negative: `data[i] >= 0`.
7. Count the number of items in an array that are even: `???`
8. Count the number of items in an array that are odd: `data[i]%2 != 0`.
9. Count the number of items in an array that are even and positive: `data[i]%2 == 0 && data[i] > 0`.
10. Count the number of items in an array that are even or positive: `???`
11. Count the number of items in an array that are neither even nor positive: `data[i]%2 != 0 && data[i] <= 0`.
12. Count the number of items in an array that are even but not positive: `???`
13. Count the number of items in an array that are odd but not negative: `data[i]%2 != 0 && data[i] >= 0`.
14. Count the number of items in an array that are even but non-zero: `???`
15. Count the number of items in an array that are odd but non-zero: `???`
16. Count the number of items in an array that are even or non-zero: `data[i]%2 == 0 || data[i]!= 0` (all values of `data[i]` satisfy this :D)
17. Count the number of items in an array that are odd or non-zero `???` (only `data[i] == 0` dpes not satisfy this)
18. Count the number of items in an array that are neither odd nor zero: `???`
19. Count the number of items in an array that are neither even nor zero: `???`
20. Count the number of items in an array that are neither even nor non-zero: `data[i]%2 != 0 && data[i]!=0`.

The idea is: if you practice enough with such problems, then it becomes second nature to identify a problem that belongs to this category.

## CATEGORY 2: Accumulating based on criteria

The only difference will be that instead of increasing the counter by 1, we'll add the current item to it, and therefore, instead of calling it `counter`, we should call it `total` or `sum` or `aggregate` or something to that extent.


1. Add (or multiply) all items in an array that are positive.
2. Add (or multiply) all items in an array that are negative.
3. Add (or multiply) all items in an array that are zero.
4. Add (or multiply) all items in an array that are non-zero.
5. Add (or multiply) all items in an array that are non-positive.
6. Add (or multiply) all items in an array that are non-negative.
7. Add (or multiply) all items in an array that are even.
8. Add (or multiply) all items in an array that are odd.
9. Add (or multiply) all items in an array that are even and positive.
10. Add (or multiply) all items in an array that are even or positive.
11. Add (or multiply) all items in an array that are neither even nor positive.
12. Add (or multiply) all items in an array that are even but not positive.
13. Add (or multiply) all items in an array that are odd but not negative
14. Add (or multiply) all items in an array that are even but non-zero.
15. Add (or multiply) all items in an array that are odd but non-zero.
16. Add (or multiply) all items in an array that are even or non-zero.
17. Add (or multiply) all items in an array that are odd or non-zero.
18. Add (or multiply) all items in an array that are neither odd nor zero.
19. Add (or multiply) all items in an array that are neither even nor zero.
20. Add (or multiply) all items in an array that are neither even nor non-zero.

Design:

1. have a variable (say `result`) to hold the final answer and initialize to 0 (additive identity) or 1 (multiplicative identity).
2. we need to go through and check EACH item of the array.
3. if the current item satisfies the criteria, **add (or multiply) the current item** into `result`.
4. when the loop terminates, return this counter.

Generic code body would be,

```java
int result = 0 (or 1); //just a more suitable variable name
for(int i=0; i < data.length; i++) {
	if(check something on data[i]) {
		result+=data[i]; (or resut*=data[i])
		//this is the only real difference from category 1.
	}
}
return result;
```

Code for number 12 version 1 (adding all even but not positive):

```java
public static int sumNonPositiveEvens(int[] data) {
	int result = 0;
	for(int i=0; i < data.length; i++) {
		if(data[i]%2==0 && data[i]<=0) {
			result+=data[i];
		}
	}
	return result;
}
```

Code for number 12 version 2 (multiplying all even but not positive):

```java
public static int productNonPositiveEvens(int[] data) {
	int result = 1;
	for(int i=0; i < data.length; i++) {
		if(data[i]%2==0 && data[i]<=0) {
			result*=data[i];
		}
	}
	return result;
}
```

# CATEGORY 3 - "Validation" problems

1. Check if there is **any** item in the array that is  positive.
2. Check if there is **any** item in the array that is  negative.
3. Check if there is **any** item in the array that is  zero.
4. Check if there is **any** item in the array that is  non-zero.
5. Check if there is **any** item in the array that is  non-positive.
6. Check if there is **any** item in the array that is  non-negative.
7. Check if there is **any** item in the array that is  even.
8. Check if there is **any** item in the array that is  odd.
9. Check if there is **any** item in the array that is  even and positive.
10. Check if there is **any** item in the array that is  even or positive.
11. Check if there is **any** item in the array that is  neither even nor positive.
12. Check if there is **any** item in the array that is  even but not positive.
13. Check if there is **any** item in the array that is  odd but not negative
14. Check if there is **any** item in the array that is  even but non-zero.
15. Check if there is **any** item in the array that is  odd but non-zero.
16. Check if there is **any** item in the array that is  even or non-zero.
17. Check if there is **any** item in the array that is  odd or non-zero.
18. Check if there is **any** item in the array that is  neither odd nor zero.
19. Check if there is **any** item in the array that is  neither even nor zero.
20. Check if there is **any** item in the array that is  neither even nor non-zero.

Instead of directly going to the pseudo-code, we'll consider one example to build a prototype:

- Check if there is **any** item in the array that is even (number 7).

Le'ts say my array contains 10 items.

### STEP 1: Check the first item (Say, 17).

- Can you tell if there is any even item in the array just by looking at the first item (17)?
- Can you guarantee that there is **NO** even item in the array just by looking at the first item (17)?

### STEP 2: Check the second item (Say, -5).

- Can you tell if there is any even item in the array just by looking at the second item (-5)?
- Can you guarantee that there is **NO** even item in the array just by looking at the second item (-5)?

### STEP 3: Check the third item (Say, 12).

- Can you tell if there is any even item in the array just by looking at the first item (12)? YES! So we can immedaitely return `true`.

What happens if I check each item and none of them is even? The loop terminates, and it's then we can return `false`.

Generic code body would be,

```java
for(int i=0; i < data.length; i++) {
	if(check if data[i] satisfies required criteria) {
		return true;
	}
}
return false;
```

# CATEGORY 4 - "Violation" problems

1. Check if **all** items in the array are positive.
2. Check if **all** items in the array are negative.
3. Check if **all** items in the array are zero.
4. Check if **all** items in the array are non-zero.
5. Check if **all** items in the array are non-positive.
6. Check if **all** items in the array are non-negative.
7. Check if **all** items in the array are even.
8. Check if **all** items in the array are odd.
9. Check if **all** items in the array are even and positive.
10. Check if **all** items in the array are even or positive.
11. Check if **all** items in the array are neither even nor positive.
12. Check if **all** items in the array are even but not positive.
13. Check if **all** items in the array are odd but not negative
14. Check if **all** items in the array are even but non-zero.
15. Check if **all** items in the array are odd but non-zero.
16. Check if **all** items in the array are even or non-zero.
17. Check if **all** items in the array are odd or non-zero.
18. Check if **all** items in the array are neither odd nor zero.
19. Check if **all** items in the array are neither even nor zero.
20. Check if **all** items in the array are neither even nor non-zero.

Again, we'll use number 7.

- Check if **all** items in the array are even.

Le'ts say my array contains 10 items.

### STEP 1: Check the first item (Say, 17).

- Can you tell if there is any even item in the array just by looking at the first item (17)?
- Can you guarantee that there is **NO** even item in the array just by looking at the first item (17)? YES! Even if one item doesn't satisfy the criteria, we can return `false` immediately.

So, what you are checking if that the current item **DOES NOT** satisfy the criteria (to return `false`).

What happens if I check each item and none of them is NOT even? The loop terminates, and it's then we can return `true`.

Generic code body would be,

```java
for(int i=0; i < data.length; i++) {
	if(check if data[i] DOES NOT satisfy required criteria) {
		return false;
	}
}
return true;
```

# Category 5 - Checking all Pairs

This is inspired by *the handshake algorithm*. Useful when you want to check each item of an array against every other item.

Consider the array `{10,70,20,90}` (surprise!)

The pairs are:

`(10, 70)`, `(10, 20)`, `(10, 90)`

`(70, 20)`, `(70,90)`

`(20, 90)`

We don't consider the pairs `(10, 10)`, `(70, 70)`, `(20, 20)`, `(90, 90)` because an item will seldom be compared with itself.

Also, once we have compared 10 with 70 (indicated by `(10, 70)`), we don't need to compare 70 with 10 again. Hence, the pair `(70, 10)` is not in the list of pairs.

You can see that we compared:

1. the first item against,
	- the second item to the last item
2. the second item against,
	- the third item to the last item
3. ...
4. the second last item against,
	1. the last item (to the last item)


If `i` is the index of the first of the items in the pair and `k` is the index of the second item in the pair, we can get it by:

```
go through each i from 0 to array.length - 2:
	go through each k from (i+1) to array.length - 1:
		compare array[i] against array[k]
```

The equivalent code is:

```java
for(int i=0; i < data.length - 1; i++) {
	for(int k=i+1; k < data.length; k++) {
		//compare data[i] against data[k] for counting/accumulation/validation/violation/...
	}
}
```

## Example 1: Checking if array has any duplicates

```java
public static boolean containsDuplicate(int[] data) {
	for(int i=0; i < data.length - 1; i++) {
		for(int k=i+1; k < data.length; k++) {
			if(data[i] == data[k]) {
				return true;
		}
	}
	return false;
}
```

## Example 2: Checking if any two items add up to a certain target

```java
public static boolean pairAddingUpto(int[] data, int target) {
	for(int i=0; i < data.length - 1; i++) {
		for(int k=i+1; k < data.length; k++) {
			if(data[i] + data[k] == target) {
				return true;
		}
	}
	return false;
}
```

## Example 3 (bit advanced): Checking if all pairs are co-prime

Two numbers are *co-prime* if they have no common divisors (besides 1).

For example, 12 and 25 are co-prime since divisors of 12 are 2, 3, 4 and 6 while that of 25 is only 5. On the other hand 147 and 490 are NOT co-prime since they are both divisible by 7.

We will use the following helper method based on euclid's algorithm to determine if two numbers are co-prime:

```java
public static boolean areCoPrime(int a, int b) {
	while(b!=0) {
		int temp = a%b;
		a = b;
		b = temp;
	}
	return a == 1;
}
```

If trying to understand that method's logic caused some of the nerves in your brain to burst, you can use the following version instead. This belongs to category 4 algorithms (violation).

```java
public static boolean areCoPrime(int a, int b) {
	for(int i=2; i<=Math.min(a, b); i++) {
		if(a%i==0 && b%i==0) { //found a common divisor!
			return false;
		}
	}
	return true;
}
```
Now that we have our helper method, we can write the method to determine if they are all co-prime:

```java
public static boolean allPairsCoPrime(int[] data) {
	for(int i=0; i < data.length - 1; i++) {
		for(int k=i+1; k < data.length; k++) {
			if(!areCoPrime(data[i], data[k])) { //at least one pair is not co-prime
				return false;
		}
	}
	return true;
}
```

Instead, if we have to count the number of co-prime pairs, we count instead of immediately returning a value after the check:

```java
public static int countCoPrimePairs(int[] data) {
	int coPrimeCount = 0;
	for(int i=0; i < data.length - 1; i++) {
		for(int k=i+1; k < data.length; k++) {
			if(areCoPrime(data[i], data[k])) {  //another co-prime pair
				coPrimeCount ++;
			}
	}
	return coPrimeCount;
}
```

Counting pairs that are NOT co-prime!? If you have have already implemented the method `countCoPrimePairs`, then it becomes trivial, as,

```java
public static int countNonCoPrimePairs(int[] data) {
	return data.length - countCoPrimePairs(data);
}
```

If you haven't implemented it, just negate the expression for the condition.

```java
public static int countNonCoPrimePairs(int[] data) {
	int coPrimeCount = 0;
	for(int i=0; i < data.length - 1; i++) {
		for(int k=i+1; k < data.length; k++) {
			if(!areCoPrime(data[i], data[k])) {  //another non co-prime pair
				coPrimeCount ++;
			}
	}
	return coPrimeCount;
}
```

# CATEGORY 6: Generating a subset

1. Return a sub-array containing all items that are positive.
2. Return a sub-array containing all items that are negative.
3. Return a sub-array containing all items that are zero.
4. Return a sub-array containing all items that are non-zero.
5. Return a sub-array containing all items that are non-positive.
6. Return a sub-array containing all items that are non-negative.
7. Return a sub-array containing all items that are even.
8. Return a sub-array containing all items that are odd.
9. Return a sub-array containing all items that are even and positive.
10. Return a sub-array containing all items that are even or positive.
11. Return a sub-array containing all items that are neither even nor positive.
12. Return a sub-array containing all items that are even but not positive.
13. Return a sub-array containing all items that are odd but not negative
14. Return a sub-array containing all items that are even but non-zero.
15. Return a sub-array containing all items that are odd but non-zero.
16. Return a sub-array containing all items that are even or non-zero.
17. Return a sub-array containing all items that are odd or non-zero.
18. Return a sub-array containing all items that are neither odd nor zero.
19. Return a sub-array containing all items that are neither even nor zero.
20. Return a sub-array containing all items that are neither even nor non-zero.

(Psst... these becomes eeeeasy with lists)

*I'll have a number 7* (we are using number 7 - Return a sub-array containing all items that are even - as an example).

In such a scenario, we obviously need to know HOW MANY items are there are the array to be returned.

So, let's calculate that first!

```java
int n = 0;
for(int i=0; i < data.length; i++) {
	if(data[i]%2 == 0) {
		n++;
	}
}
```

So far, so good, yeah?

Now that we know the size of the array required, go ahead and create one :)

```java
int[] result = new int[n];
```

(Yes, the length COULD be zero, which is fine - it just creates an empty array).

The next step is populating the array result.

The key is to **keep a track of the index into which an item is being put**.

For example, if `data = {7,12,-5,9,18}`, we need to put,

1. `data[1]` into `result[0]`
2. `data[4]` into `result[1]`

The index for `data` will be handled by good old `i`.
We create a separate index `k` to hold index for `result`.

```java
int k = 0;
for(int i=0; i < data.length; i++) {
	if(data[i]%2 == 0) {
		result[k] = data[i];
		k++; //k only increases when another item put into result
	}
}
```

Lastly, return this array!

```java
return result;
```

Put it all together and you got yourself a solution.

```java
public static int[] getEvenItems(int[] data) {
int n = 0;
for(int i=0; i < data.length; i++) {
	if(data[i]%2 == 0) {
		n++;
	}
}

int[] result = new int[n];

int k = 0;
for(int i=0; i < data.length; i++) {
	if(data[i]%2 == 0) {
		result[k] = data[i];
		k++; //k only increases when another item put into result
	}
}

return result;
}
```
