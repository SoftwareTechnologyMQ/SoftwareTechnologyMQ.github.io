---
layout: page
title: Searching
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge</summary>

  * [Recursion](./recursion)
  * [Arrays](./composite_data)

</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes</summary>

  * Recognise the reasons binary search works
  * Be able to trace a binary search on a sorted array
  * Be able to write a binary search algorithm

</details>

# Binary search

In this section, we'll learn a fast way of searching through data, under one assumption...

**The collection (array in our case) must be sorted**

We can always tweak the algorithm based on the order of sorting.

Before explaining things descriptively, how about a video to illustrate binary search, from our good friends at HackerRank.

**IMPORTANT!!!**

The implementation discussed is recursive. We haven't covered recursion yet so only the first 2 minutes 40 seconds of the video are relevant.

<iframe width="560" height="315" src="https://www.youtube.com/embed/P3YID7liBug" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## The game is on!

Lets say that we are playing the game that has the following rules.

1. Person A (henceforth named Alice) thinks of a number between 1 and 31 (including 1 and 31). Let this number be `target`.
2. Person B (henceforth named Bob) tries to guess the number. Let Bob's guess be `g`.
3. Alice needs to tell Bob if,
	1. `target == g`, or,
	2. `target > g`, or,
	3. `target < g`
4. Based on Alice's response, Bob makes his next guess if required. That is, go to step 2.

<div class="task" markdown="1">Does it make sense for the first guess to be 5?
<details class="solution" markdown="1"><summary>solution</summary> No. Of course, you will find the target with any given guess with a small probability. Otherwise, in this case, if you are very lucky (4/31 probability), you'll be left with 4 numbers to guess from. However, the chances are (26/31 probability) that you'll be left with 26 numbers to guess from.
</details></div>

<div class="task" markdown="1">What is a clever first guess?
<details class="solution" markdown="1"><summary>solution</summary>
The first clever guess would be 16 since either that **is** the target (1/31) or in either of the remaining cases, you are left with 15 numbers to guess from (either 1 to 15, or 16 to 31).
</details> </div>

> If there are an even number of items (say, 10), then, excluding the middle
> item, the left half will have one more or one less item than the right half.
> This is ok :)


The strategy explained in the last exercise is the same strategy we use to find a particular page in a book, where we "approximate" our guess within the remaining pages at each stage.

For those of you who may have used the dictionary, it's again, the same strategy used to find a particular word in a dictionary.

## Visualising the game

Assume the numbers in contention being in green. Initially all the numbers are in contention

><span style="color:green">1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31</span>

Guess 1: 16. Feedback: target is higher than 16

><span style="color:red">1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,</span><span style="color:green"> 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31</span>

Guess 2: 24. Feedback: target is lower than 24

><span style="color:red">1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,</span><span style="color:green"> 17, 18, 19, 20, 21, 22, 23,</span><span style="color:red"> 24, 25, 26, 27, 28, 29, 30, 31</span>

Guess 3: 20. Feedback: target is lower than 20

><span style="color:red">1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,</span><span style="color:green"> 17, 18, 19,</span><span style="color:red"> 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31</span>

Guess 4: 18. Feedback: target is higher than 18

><span style="color:red">1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,</span><span style="color:green"> 19,</span><span style="color:red"> 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31</span>

Guess 5: 19. Feedback: target equals 19 - **FOUND!**

## Coding the game

Say the array `arr` is:

><span style="color:red">20, 60, 40, 10, 0, 30, 70, 50</span>

The first thing we need to do is to sort it. Depending on the order, the rest of the implementation will be tweaked. Say we sort it in ascending order as:

><span style="color:green">0, 10, 20, 30, 40, 50, 60</span>

Let us say that `target = 40`

Our first guess would be `30` as it would split the array down the middle.
Upon comparing `target` with the guess, we can see that if present, `target` is in the right half.

We update our search space by updating parameters `first` and `last` that hold first and last indices of the search space, respectively. The original values being:

```java
int first = 0;
int last = arr.length - 1;
```

Index of the middle item is computed at each iteration as:

```java
int median = (first+last)/2;
```

The three scenarios we have are:

1. `target == arr[median]`:
	* return `median` immediately
2. `target > arr[median]`:
	* first = median + 1 (to reflect searching in the right half)
3. `target < arr[median]`:
	* last = median - 1 (to reflect searching in the left half)

### Until when should we do this?

We do this as long as search space is not empty. If `first` becomes more than `last` it means the starting point of the search space is AFTER ending point of the search space which isn't possible. So the expression to carry on is:

```java
(first <= last)
```

What happens when `first > last` and the expression is no longer true? We have searched everywhere and not found the target. So we can return -1 (standard not-found index).

### Putting it all together

```java
public static int binarySearch(int[] arr, int target) {
	int first = 0;
	int last = arr.length - 1;
	while(first <= last) {
		int median = (first+last)/2;
		if(target == arr[median])
			return median;
		//we reach here only if target != arr[median]
		if(target > arr[median])
			first = median + 1;
		else
			last = median - 1;
	}
	return -1;
}
```

## Binary search performance

Let number of items at start be `n`. For simplicity, assume `n` is a power of 2, like 1, 2, 4, 8, 16, 32 and so on. We write this as `n` = 2<sup>k</sup>.

Just like square is the inverse of square root, logarithm is the inverse of power.

n = 2<sup>k</sup>

is also written as:

k = log<sub>2</sub>(n)

### Best case scenario

The best case is that the middle item is the target. In the best case, it takes only one iteration to find the target.

> Number of iterations in best case: 1

### Worst case scenario

The worst case is that the item doesn't exist in the array. In this case, we keep halving the search space.

* After iteration 1: 2<sup>k</sup> to 2<sup>k-1</sup>
* After iteration 2: 2<sup>k-1</sup> to 2<sup>k-1</sup>
* After iteration 3: 2<sup>k-2</sup> to 2<sup>k-1</sup>
* ...
* After iteration k: 2<sup>k-(k-1)</sup> or 2<sup>1</sup> to 2<sup>k-k</sup> or 2<sup>0</sup>

After `k` iterations, we'll reach our last item and after that the loop terminates as `first > last`.

This gives us the number of iterations in the worst case as `k`, or,

> Number of iterations in worst case: **log<sub>2</sub>(n)**
