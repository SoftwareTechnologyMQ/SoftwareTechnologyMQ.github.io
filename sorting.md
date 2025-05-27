---
layout: page
title: Sorting
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge</summary>

  * <a href="functions">Functions</a>
  * <a href="compositedata">Composite Data (Arrays)</a>
  * <a href="classesarrayofobjects">Classes</a>
  * <a href="lists">ArrayLists</a>
</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes</summary>

  * Understand why data needs to be sorted
  * Understand how data can be sorted
</details>

## Author: Gaurav Gupta and Greg Baker

<img src="./assets/images/margeSort.jpeg" width="400">

## Why perform sorting?

Sorting is a fundamental operation that,

1. improves the efficiency of several tasks, and, 
2. makes several other non-trivial tasks, well, trivial.
3. is often tested during job interviews

## Example 1: Finding the k-highest item in a collection

For an unsorted collection, you have to go through each item of the collection in order to get the first highest value, then again for second highest, etc.

For a sorted collection, the highest value will either be the first value or the last value. The <i>k</i>-highest is at the <i>k</i><sup>th</sup> position. Thus, it reduces to a single-operation task.


## Example 2: Search

Instead of starting at the beginning and checking every element in a
array, if it is sorted, you can jump into the middle of the array and
ask whether the element you are looking for is bigger or smaller. That
tells you you only need to search half as many elements.

Then you can jump into the half way point of the ones you need to search
and repeat the process.

(Bonus: instead of jumping half way, you can estimate how far you need to
jump.)

## Example 3: Finding the number of unique items in a collection

Consider the array `{10,70,20,20,20,90,10,90,20,70}`. The four unique items are 10, 70, 20 and 90.

For an unsorted collection, you can choose to see if the item is first of its kind, and only if so, increase a counter.

For an sorted collection, every time an item is not the same as the next item, you can increase the counter (that is initialized to 1) by 1. Zero is returned for empty and `null` collections.

The second approach is signficantly easier than the first.

## Sorting is good


Bottomline - It makes things MUCH easier!

### Bogosort

Bogosort repeatedly shuffles the data until it happens to be in order.  It is a
fantastic way to waste time and highlights why we care about algorithmic
complexity.  A short implementation is given in
[BogoSort.java](./assets/codes/sorting/BogoSort.java).

### Tree sort

But we learned how to sort when we created tree structures!

Tree sort inserts every element into a binary search tree and then reads the
values back by traversing the tree in order.

```
        40
       /  \
     20    70
       \   / \
       30 60  90
```

The implementation can be found in
[TreeSort.java](./assets/codes/sorting/TreeSort.java).

### Cost of sorting

Of course, we haven't considered the cost involved in sorting a collection. If the collection changes frequently, we need to maintain the sorting order. This can be done either by,

1. adding the item that has to be added at the appropriate place (Which more or less requires one iteration through the collection) - pretty good!
2. adding the item at the end and sorting the collection again - not so good.

What one must remember is that sorting is not free and has a cost associated with it.

Tree sort in particular stores every value in a node of a binary search tree.
That extra memory can be significant and, if the data arrives already
sorted, the tree degenerates into a linked list.  In that worst case the
insertions each scan most of the existing nodes giving an overall cost of
$O(n^2)$.



### Approaches to sorting

If I ask you to sort the collection, what would be your approach? Think about that for a few minutes and try to represent it as a [flowchart](https://www.code2flow.com).

> {40, 70, 20, 90, 30, 80, 20}

One approach can be to find the smallest item and make sure it's at the right place. That's 20, and belongs at the first position (where 40 sits). 

#### Sub-option 1

While putting it in its right place, we can either shift (one to the right) items before it and then place it at that location, so the collection becomes:

> {20, 40, 70, 90, 30, 80, 20}

After this we are guaranteed that the first item is correct and continue with the rest of the collection, completely ignoring the first value.

#### Sub-option 2

Another option to put 20 in the right place is to simply swap it with whatever is there. Here, the collection becomes:

> {20, 70, 40 90, 30, 80, 20}

Just like the first sub-option, we can totally forget about the first item once this is done, and carry on with the same process starting at the second item.

### Full trace using "shifting" approach

Sorted part and unsorted part put in their own *compartments*.

> | 40, 70, 20, 90, 30, 80, 20
> 
> 40 | 70, 20, 90, 30, 80, 20
> 
> 40, 70 | 20, 90, 30, 80, 20
> 
> 20, 40, 70, | 90, 30, 80, 20
> 
> 20, 40, 70, 90, | 30, 80, 20
> 
> 20, 30, 40, 70, 90, | 80, 20
> 
> 20, 30, 40, 70, 80, 90, | 20
> 
> 20, 20, 30, 40, 70, 80, 90 |
> 


### Full trace using "swapping" approach

Sorted part and unsorted part put in their own *compartments*.

> | 40, 70, 20, 90, 30, 80, 20
>
> 20, | 70, 40, 90, 30, 80, 20
>
> 20, 20, | 40, 90, 30, 80, 70
>
> 20, 20, 30, | 90, 40, 80, 70
>
> 20, 20, 30, 40, | 90, 80, 70
>
> 20, 20, 30, 40, 70, | 80, 90
>
> 20, 20, 30, 40, 70, 80, | 90 
>
> 20, 20, 30, 40, 70, 80, 90 | 
> 

## Bring it in!

Now that we've had an intuitive idea of what needs to be done, let's formalize our understanding.

- The shifting approach is what is known as *insertion sort*.
- The swapping approach is what is known as *selection sort*.

## Visualising different algorithms

https://sortvisualizer.fenilsonani.com/

[Visualgo](https://visualgo.net/en/sorting).

## Insertion Sort

<img src = "./assets/images/insertionSortAscendingLeft.png" width = 500>

See [InsertionSort.java](./assets/codes/sorting/InsertionSort.java) for a simple
implementation.

Note that we can have variations of the same algorithm. For instance, the following version of insertion sort sorts in ascending order, starting the sorting process from right to left.

<img src = "./assets/images/insertionSortAscendingRight.png" width = 500>

## Selection Sort

<img src = "./assets/images/selectionSort.png" width = 500>

The code in [SelectionSort.java](./assets/codes/sorting/SelectionSort.java)
implements this approach.

Note that we can have variations of the same algorithm. For instance, the following version of selection sort sorts in ascending order, starting the sorting process from right to left.

<img src = "./assets/images/selectionSortAscendingRight.png" width = 500>

Yes another version of selection sort sorts in descending order, starting the sorting process from right to left.

<img src = "./assets/images/selectionSortDescendingRight.png" width = 500>

## Bubble Sort

Bubble sort repeatedly swaps out-of-order adjacent items.  While simple to
understand, it is generally slower than insertion or selection sort.  See
[BubbleSort.java](./assets/codes/sorting/BubbleSort.java) for a demonstration.

## Quick Sort

Quick sort works by choosing a pivot, placing smaller values before the pivot and
larger values after it, and then recursively sorting the two partitions.  A
simple implementation is provided in
[QuickSort.java](./assets/codes/sorting/QuickSort.java).

A worked trace on the numbers `40, 70, 20, 90, 30, 80, 20`:

> | 40, 70, 20, 90, 30, 80, 20
>
> 20 | 40, 70, 90, 30, 80, 20
>
> 20, 20 | 40, 70, 90, 30, 80
>
> 20, 20 | 30, 40 | 70, 90, 80
>
> 20, 20, 30, 40 | 70, 90, 80
>
> 20, 20, 30, 40 | 70 | 90, 80
>
> 20, 20, 30, 40, 70 | 80, 90
>
> 20, 20, 30, 40, 70, 80 | 90
>
> 20, 20, 30, 40, 70, 80, 90 |

## Dual-Pivot Quick Sort

Dual-pivot quick sort extends the basic algorithm by selecting two pivots. Values less than the first pivot are placed on the left, those between the pivots stay in the middle and those greater than the second pivot move to the right.  This reduces comparisons and is the approach used by `Arrays.sort()` for primitive arrays in Java.

A simplified run on the same numbers with pivots 20 and 70:

> | 40, 70, 20, 90, 30, 80, 20
> 20 | 40, 30 | 70, 90, 80, 20
> 20, 20 | 30, 40 | 70, 80, 90
> 20, 20, 30, 40 | 70 | 80, 90
> 20, 20, 30, 40, 70, 80, 90 |

## Timsort

[https://sorting-visualizer.researchdatapod.com/](https://sorting-visualizer.researchdatapod.com/)

Timsort is a hybrid of merge sort and insertion sort.  It is designed to take
advantage of ordered subsequences in real data and is used by default when Java
sorts objects.

A simplified run of Timsort on the same numbers identifies runs and merges them:

> [40, 70], [20, 90], [30, 80], [20]
>
> [20, 40, 70, 90], [20, 30, 80]
>
> 20, 20, 30, 40, 70, 80, 90


## What's the best we can do?

Comparison-based sorting algorithms can't beat $O(n \log n)$ in the general
case because each comparison yields limited information.  

A comparison-based sorting algorithm only relies on comparing pairs of elements. Any such algorithm can be represented as a decision tree, where:

- Each internal node represents a comparison between two elements.

- Each branch corresponds to one of two outcomes ($\le$ or $>$).

- Each leaf node represents one possible permutation (sorted order).

### Step-by-step reasoning

1.	**Number of permutations:**
Sorting n distinct items could yield $n!$ possible outcomes.

2.	**Binary decision tree:**
A binary tree with height h has at most $2^h$ leaves.

3.	**Lower bound on height:**
Since you need at least as many leaves as possible outcomes, you must have:
$2^h \ge n!$

4.	**Use Stirling’s Approximation:**

For large n, Stirling’s approximation tells us:

$n! \approx \sqrt{2\pi n} \left(\frac{n}{e}\right)^n$

Taking logarithms (base 2) of both sides:

$h \ge \log_2(n!) \approx \log_2\left(\sqrt{2\pi n}\left(\frac{n}{e}\right)^n\right)$

This simplifies to:
$h \approx n \log_2 n - n \log_2 e + O(\log n) \quad\Rightarrow\quad h = \Omega(n \log n)$

## Exotic sort algorithms

To sort faster we need
to look for more unusual approaches where we don't compare numbers.

### Sleep sort

Sleep sort launches a thread for each value and relies on the operating system's
timing to print numbers in order.  It's more of a curiosity than a practical
algorithm.  The code in [SleepSort.java](./assets/codes/sorting/SleepSort.java)
shows how it works.

### Bead sort / Gravity sort

This method lets beads fall under gravity so that more beads collect on pegs for
larger values.  It only works for positive integers and illustrates how physical
processes can be used to sort.

[https://bead-sort.arithmetic.guru](https://bead-sort.arithmetic.guru)


## Radix Sort

[https://www.sortvisualizer.com/radixsort/]([https://www.sortvisualizer.com/radixsort/])

Radix sort processes the digits of numbers one position at a time, allowing
integers to be sorted in linear time when the number of digits is limited.  A
full implementation appears in
[RadixSort.java](./assets/codes/sorting/RadixSort.java).

A quick demonstration treats the digits from least significant to most
significant:

> 41, 70, 21, 79, 26, 78, 21
>
> (ones) 70, 41, 21, 21, 26, 78, 79
>
> (tens) 21, 21, 26, 41, 70, 78, 79


## Quantum acceleration?

It remains an open research question whether quantum computers can achieve more
than a constant factor speed-up for sorting.


## Sorting in the Java standard library

Java provides `Arrays.sort()` to sort arrays and `Collections.sort()` for lists.
Arrays of primitives use a tuned Quicksort while object arrays and lists are
sorted with Timsort.  Example usage:

```java
int[] data = {40, 70, 20};
Arrays.sort(data); // in-place

List<Integer> list = new ArrayList<>(List.of(40, 70, 20));
Collections.sort(list);
```

### Comparable and Comparator

`List.sort()` and `Arrays.sort()` rely on comparison logic rather than the `<` or `>` operators. If an object does not provide a natural order, Java offers two ways to supply one.

#### Comparable

Implement `Comparable<T>` to define how instances compare:

```java
public class Person implements Comparable<Person> {
    String name;
    int age;

    @Override
    public int compareTo(Person other) {
        return Integer.compare(this.age, other.age);
    }
}
```

Instances can then be sorted without extra arguments:

```java
List<Person> people = ...;
Collections.sort(people);  // uses compareTo
people.sort(null);         // also uses compareTo
Arrays.sort(personArray);  // also uses compareTo
```

#### Comparator

If the class does not implement `Comparable` or a different order is required, supply a `Comparator<T>`:

```java
people.sort(Comparator.comparing(p -> p.name));
Arrays.sort(personArray, (a, b) -> a.name.compareTo(b.name));
```

#### Under the hood

- A `Comparable` or `Comparator` must be available.
- The sort methods call comparison functions instead of `<` or `>`.
- Object sorting uses dual-pivot quicksort for `Arrays.sort()` and TimSort for `List.sort()`.
- Without a comparison strategy, a `ClassCastException` occurs.

Primitive arrays still use `<` and `>` directly with an optimised quicksort.

In short, objects must be comparable—either naturally or via a comparator—otherwise sorting fails at runtime.
