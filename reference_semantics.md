---
layout: page
title: "Reference Semantics"
within: programming
---
<details class="prereq" markdown="1"><summary>Assumed Knowledge</summary>
  * [Compound Data](composite_data)
</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes</summary>
  * Understand the difference between the value semantics of atomic data and the reference semantics of compound data
  * Understand the consequences for programming of reference semantics.
  * Understand how passing arrays to functions is a case of reference semantics
</details>

We discussed in the [compound data topic](composite_data) how compound data can't be stored directly in its memory slot.  Instead, that slot holds a _reference_ to some larger chunk of memory where the data is stored.

This different storage strategy leads to different behaviour for variables of these compound types.  We call the old way (the behaviour for `int`, `char`, and any other value that fits in its memory slot directly) _value semantics_ and we call the new behaviour (for arrays and objects) _reference semantics_.

There are no new rules to remember, but the existing rules result in things happening a little differently.

First, let's be reminded of all the ways a variable can be assigned a value:

  * `x = 6`: the value 6 is put in the memory slot named `x`.
  * `y = x`: the value stored in the slot named `x` is copied to the slot named `y`.
  * `foo(6)`: the value 6 is copied to the memory slot corresponding to the formal paramter of `foo`.
  * `foo(x)`: the value stored in the slot named `x` is copied to the memory slot corresponding to the formal paramter of `foo`.

The new and interesting thing is _what gets copied when the value stored in the slot is a reference?_.  Well, you can guess I am sure.  The reference gets copied.  Importantly, the larger chunk of data at the end of the reference does not get copied.  So, when the value is in the slot and the value gets copied, we call it value semantics.  When the reference is in the slot and the reference gets copied, we call it reference semantics.

The underlying concept is simple enough, now lets see some consequences that flow from it.

<iframe width="560" height="315" src="https://www.youtube.com/embed/iOSm0gQ-z1s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Arrays and functions

<iframe width="560" height="315" src="https://www.youtube.com/embed/M_wqSKvOsXs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

It's very common to pass an array to a function. Generally, we operate on an array passed to a function, but sometimes it's also useful to,

1. modify the contents of the passed array inside the function
2. return an array from the function that is copied into an array in the caller.

## Operating on an array passed to a function

When you pass an array to a function, a shallow copy of the actual
parameter is made into the formal parameter. For example, in the
following code, `data` becomes a shallow copy of `arr`.

```java
void caller() {
    int[] arr = {10, 70, 50};
    int sum = total(arr);
}

int total(int[] data) {
    int result = 0;
    for(int i=0; i < data.length; i++) {
        result+=data[i];
    }
    return result;
}
```

<div><center><img src="arraysAndFunctionsFigs/arraysAndFunctionMemoryDiagrams-figure0.png" style="width: 500px;"></center></div>

## Modifying contents of array passed

If you have a function that modifies the passed array, the contents of
the actual parameter will also change.

```java
void caller() {
    int[] arr = {10, -70, 0};
    negate(arr);
}

void negate(int[] data) {
    for(int i=0; i < data.length; i++) {
        data[i]=data[i]*-1;
    }
}
```

<div><center><img src="arraysAndFunctionsFigs/arraysAndFunctionMemoryDiagrams-figure1.png" style="width: 500px;"></center></div>

## Returning an array from a function

If a function returns an array (source) and the caller copies it into an
array (destination), it’s a shallow copy as demonstrated in the
following example.

If you have a function that modifies the passed array, the contents of
the actual parameter will also change.

```java
void caller() {
    int[] data = getDiceOutcomes(5);
}

int[] getDiceOutcomes(int n) {
    int[] outcomes = new int[n];
    for(int i=0; i < outcomes.length; i++) {
        outcomes[i] = (int)random(1, 7);
    }
    return outcomes;
}
```

<div><center><img src="arraysAndFunctionsFigs/arraysAndFunctionMemoryDiagrams-figure2.png" style="width: 500px;"></center></div>

# Multi-Dimensional Arrays

<iframe width="560" height="315" src="https://www.youtube.com/embed/nGyy4kcsglg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


All this also means it is possible to have an array of arrays.  These are called multi-dimensional arrays.  For two dimensions, they are declared as

```
int[][] multiDArray;
```

and when you do memory allocation you must give the size of the _outer_ array and the size of all the _inner_ arrays (in this case 2 elements in the outer array and 3 in each inner array)

```
multiDArray = new int[2][3];
```
Resulting in the following occuring in memory

<svg xmlns="http://www.w3.org/2000/svg" height="200" width="300" version="1.1" viewBox="0 0 79.375011 52.916666">
 <defs>
  <marker id="marker10561" refY="0" refX="0" orient="auto" overflow="visible">
   <path stroke-linejoin="round" d="m8.719 4.034-10.93-4.018 10.93-4.018c-1.746 2.372-1.736 5.618 0 8.036z" fill-rule="evenodd" transform="scale(-.6)" stroke="#000" stroke-width=".625"/>
  </marker>
  <marker id="marker8703" refY="0" refX="0" orient="auto" overflow="visible">
   <path stroke-linejoin="round" d="m8.719 4.034-10.93-4.018 10.93-4.018c-1.746 2.372-1.736 5.618 0 8.036z" fill-rule="evenodd" transform="scale(-.6)" stroke="#000" stroke-width=".625"/>
  </marker>
  <marker id="marker8146" refY="0" refX="0" orient="auto" overflow="visible">
   <path stroke-linejoin="round" d="m8.719 4.034-10.93-4.018 10.93-4.018c-1.746 2.372-1.736 5.618 0 8.036z" fill-rule="evenodd" transform="scale(-.6)" stroke="#000" stroke-width=".625"/>
  </marker>
  <marker id="marker9431" refY="0" refX="0" orient="auto" overflow="visible">
   <path stroke-linejoin="round" d="m8.719 4.034-10.93-4.018 10.93-4.018c-1.746 2.372-1.736 5.618 0 8.036z" fill-rule="evenodd" transform="scale(-.6)" stroke="#000" stroke-width=".625"/>
  </marker>
 </defs>
 <g transform="translate(22.16 -240.1)">
  <rect height="35.72" width="35.72" stroke="#263738" y="249.4" x="3.969" stroke-width=".245" fill="none"/>
  <g fill="none">
   <path marker-end="url(#marker9431)" d="m-3.969 248.1 6.992 3.032" stroke="#000" stroke-width=".2761"/>
   <g stroke="#263738">
    <g stroke-width=".2553px">
     <path d="m7.937 249.4v35.72"/>
     <path d="m11.91 249.4v35.72"/>
     <path d="m15.88 249.4v35.72"/>
     <path d="m19.84 249.4v35.72"/>
     <path d="m23.81 249.4v35.72"/>
    </g>
    <path stroke-width=".2507px" d="m27.78 249.4v35.72"/>
    <path stroke-width=".2553px" d="m31.75 249.4v35.72"/>
    <path stroke-width=".2553px" d="m35.72 249.4v35.72"/>
    <g stroke-width=".2646px">
     <path d="m3.969 253.3h35.72"/>
     <path d="m3.969 257.3h35.72"/>
     <path d="m3.969 261.3h35.72"/>
     <path d="m3.969 265.3h35.72"/>
     <path d="m3.969 269.2h35.72"/>
     <path d="m3.969 273.2h35.72"/>
     <path d="m3.969 277.2h35.72"/>
     <path d="m3.969 281.1h35.72"/>
    </g>
   </g>
   <path marker-end="url(#marker8703)" d="m5.292 250.7 10.59 2.6" stroke="#000" stroke-width=".2646px"/>
   <rect height="3.969" width="11.91" stroke="#263738" y="269.2" x="19.84" stroke-width=".5926"/>
  </g>
  <g font-size="3.836px" font-family="sans-serif">
   <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" line-height="1.25" y="272.62872" x="20.695171"><tspan y="272.62872" x="20.695171" stroke-width=".0959">0</tspan></text>
   <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" line-height="1.25" y="272.56442" x="24.589979"><tspan y="272.56442" x="24.589979" stroke-width=".0959">0</tspan></text>
   <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" line-height="1.25" y="272.65607" x="28.586056"><tspan y="272.65607" x="28.586056" stroke-width=".0959">0</tspan></text>
   <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" line-height="1.25" y="264.78445" x="5.0082393"><tspan y="264.78445" x="5.0082393" stroke-width=".0959">0</tspan></text>
   <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" line-height="1.25" y="264.72015" x="8.7841005"><tspan y="264.72015" x="8.7841005" stroke-width=".0959">0</tspan></text>
   <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" line-height="1.25" y="246.93231" x="-17.322205"><tspan y="246.93231" x="-17.322205" stroke-width=".0959">multiDArray</tspan></text>
  </g>
  <g fill="none">
   <rect height="3.969" width="3.969" stroke="#263738" y="249.4" x="3.969" stroke-width=".7650"/>
   <rect height="3.969" width="7.938" stroke="#263738" y="253.3" x="15.88" stroke-width=".7650"/>
   <path marker-end="url(#marker10561)" d="m17.2 256-10.58 5.3" stroke="#000" stroke-width=".2646px"/>
   <path marker-end="url(#marker8146)" d="m22.49 256-1.323 13.23" stroke="#000" stroke-width=".2646px"/>
  </g>
  <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" font-size="3.836px" y="264.72015" x="12.743206" font-family="sans-serif" line-height="1.25" fill="#000000"><tspan y="264.72015" x="12.743206" stroke-width=".0959">0</tspan></text>
  <rect height="3.969" width="11.91" stroke="#263738" y="261.3" x="3.969" stroke-width=".7650" fill="none"/>
 </g>
</svg>

Note that each slot of the outer array contains everything you need for another array, the reference to the chunk of memory and the chunk in some other spot.  The actual integers are stored in the secondary chunks.  This means you need _two_ slot numbers to get to any particular value.  The first will get you the slot in the _outer_ array and sthe second will get you the slot in _that_ _inner array_.  For example, here is what happens when I run

```
multiDArray[1][2] = 4;
```

<svg xmlns="http://www.w3.org/2000/svg" height="200" width="300" version="1.1" viewBox="0 0 79.375011 52.916666">
 <defs>
  <marker id="marker10561" refY="0" refX="0" orient="auto" overflow="visible">
   <path stroke-linejoin="round" d="m8.719 4.034-10.93-4.018 10.93-4.018c-1.746 2.372-1.736 5.618 0 8.036z" fill-rule="evenodd" transform="scale(-.6)" stroke="#000" stroke-width=".625"/>
  </marker>
  <marker id="marker8703" refY="0" refX="0" orient="auto" overflow="visible">
   <path stroke-linejoin="round" d="m8.719 4.034-10.93-4.018 10.93-4.018c-1.746 2.372-1.736 5.618 0 8.036z" fill-rule="evenodd" transform="scale(-.6)" stroke="#000" stroke-width=".625"/>
  </marker>
  <marker id="marker8146" refY="0" refX="0" orient="auto" overflow="visible">
   <path stroke-linejoin="round" d="m8.719 4.034-10.93-4.018 10.93-4.018c-1.746 2.372-1.736 5.618 0 8.036z" fill-rule="evenodd" transform="scale(-.6)" stroke="#000" stroke-width=".625"/>
  </marker>
  <marker id="marker9431" refY="0" refX="0" orient="auto" overflow="visible">
   <path stroke-linejoin="round" d="m8.719 4.034-10.93-4.018 10.93-4.018c-1.746 2.372-1.736 5.618 0 8.036z" fill-rule="evenodd" transform="scale(-.6)" stroke="#000" stroke-width=".625"/>
  </marker>
 </defs>
 <g transform="translate(22.16 -240.1)">
  <rect height="35.72" width="35.72" stroke="#263738" y="249.4" x="3.969" stroke-width=".245" fill="none"/>
  <g fill="none">
   <path marker-end="url(#marker9431)" d="m-3.969 248.1 6.992 3.032" stroke="#000" stroke-width=".2761"/>
   <g stroke="#263738">
    <g stroke-width=".2553px">
     <path d="m7.937 249.4v35.72"/>
     <path d="m11.91 249.4v35.72"/>
     <path d="m15.88 249.4v35.72"/>
     <path d="m19.84 249.4v35.72"/>
     <path d="m23.81 249.4v35.72"/>
    </g>
    <path stroke-width=".2507px" d="m27.78 249.4v35.72"/>
    <path stroke-width=".2553px" d="m31.75 249.4v35.72"/>
    <path stroke-width=".2553px" d="m35.72 249.4v35.72"/>
    <g stroke-width=".2646px">
     <path d="m3.969 253.3h35.72"/>
     <path d="m3.969 257.3h35.72"/>
     <path d="m3.969 261.3h35.72"/>
     <path d="m3.969 265.3h35.72"/>
     <path d="m3.969 269.2h35.72"/>
     <path d="m3.969 273.2h35.72"/>
     <path d="m3.969 277.2h35.72"/>
     <path d="m3.969 281.1h35.72"/>
    </g>
   </g>
   <path marker-end="url(#marker8703)" d="m5.292 250.7 10.59 2.6" stroke="#000" stroke-width=".2646px"/>
   <rect height="3.969" width="11.91" stroke="#263738" y="269.2" x="19.84" stroke-width=".5926"/>
  </g>
  <g font-size="3.836px" font-family="sans-serif">
   <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" line-height="1.25" y="272.62872" x="20.695171"><tspan y="272.62872" x="20.695171" stroke-width=".0959">0</tspan></text>
   <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" line-height="1.25" y="272.56442" x="24.589979"><tspan y="272.56442" x="24.589979" stroke-width=".0959">0</tspan></text>
   <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" line-height="1.25" y="272.65607" x="28.586056"><tspan y="272.65607" x="28.586056" stroke-width=".0959">4</tspan></text>
   <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" line-height="1.25" y="264.78445" x="5.0082393"><tspan y="264.78445" x="5.0082393" stroke-width=".0959">0</tspan></text>
   <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" line-height="1.25" y="264.72015" x="8.7841005"><tspan y="264.72015" x="8.7841005" stroke-width=".0959">0</tspan></text>
   <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" line-height="1.25" y="246.93231" x="-17.322205"><tspan y="246.93231" x="-17.322205" stroke-width=".0959">multiDArray</tspan></text>
  </g>
  <g fill="none">
   <rect height="3.969" width="3.969" stroke="#263738" y="249.4" x="3.969" stroke-width=".7650"/>
   <rect height="3.969" width="7.938" stroke="#263738" y="253.3" x="15.88" stroke-width=".7650"/>
   <path marker-end="url(#marker10561)" d="m17.2 256-10.58 5.3" stroke="#000" stroke-width=".2646px"/>
   <path marker-end="url(#marker8146)" d="m22.49 256-1.323 13.23" stroke="#000" stroke-width=".2646px"/>
  </g>
  <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" font-size="3.836px" y="264.72015" x="12.743206" font-family="sans-serif" line-height="1.25" fill="#000000"><tspan y="264.72015" x="12.743206" stroke-width=".0959">0</tspan></text>
  <rect height="3.969" width="11.91" stroke="#263738" y="261.3" x="3.969" stroke-width=".7650" fill="none"/>
 </g>
</svg>


When you work over these arrays, you need _nested loops_.  The outer will loop over the outer array and the inner loop will run all the way through for each inner array.

# Exercises

#### Exercise 1
Define a function that when passed an integer array, returns the sum of all even numbers in the array.

#### Exercise 2
Call the function defined in exercise 1 with an array of your choice and store the value returned in a variable `result`.

#### Exercise 3
Define a function that when passed two integer arrays, returns `true` if they are identical (same items in the same order), `false` otherwise.

#### Exercise 4
Define a function that when passed an integer array, returns `true` if all items in the array are positive, `false` otherwise.

#### Exercise 5
Define a function that when passed an integer array, returns `true` if there is any positive item in the array, `false` otherwise.

#### Exercise 6
Define a function that when passed a floating-point (`double`) array, returns an integer array containing the integer part of the items of the passed array. For example, if the array passed is `{-3.6, 0.8, 7.2, -2.5}`, the array returned should be `{-3, 0, 7, -2}`.

#### Exercise 7
Define a function that when passed an integer array, returns an array containing the positive items from the array. For example, if the array passed is `{1, -3, 0, -5, 7, 0, 0, 0, 2, 9}`, the array returned should be `{1, 7, 2, 9}`.

#### Exercise 8 (Advanced)
Define a function that when passed two integer arrays, returns `true` if they are the same (same items but not necessarily in the same order), `false` otherwise.


# Coding in the real world

## SCENARIO 1
Define a function that when passed an array containing outcomes of a series of dice rolls (6-faced dice), returns the number of times a 6 was rolled.

## SCENARIO 2
Define a function that when passed an array containing weekly salaries of a person, returns the amount of tax that should be withheld based on the following payroll department's withholding rules,

- income up to `$300` a week is tax-free
- income from `$301` to `$500` a week is taxed at 15%
- income from `$501` to `$800` a week is taxed at 20%
- income from `$801` to `$1000` a week is taxed at 25%
- income from `$1001` to `$1500` a week is taxed at 30%
- income over `$1500` a week is a week taxed at 35%

For example, if the array holding salaries is `{1200, 600}`, the first week's salary is taxed

`0.15*200 + 0.2*300 + 0.25*200 + 0.3*200 =  200`

and the second week's salary is taxed

`0.15*200 + 0.2*100 = 50`

Total tax: 250.

## SCENARIO 3
Time to time, we get a list of students and their marks. The list of students is in a `String` array, while the marks are in an integer array. Obviously, the size of both the arrays is the same. Also, the name of the first student is at index 0 of the names array and his/her marks are at index 0 in the marks array and so on.

Define a function that returns the name of the student with the highest mark. For the basic version, in case of a tie, return the name of the first student with the highest mark. For the advanced version, in case of a tie, return an array with the names of all the students who have the same highest mark.

## SCENARIO 4
During an experiment, our data was corrupted. While the valid values should be between 0 and 100, some values were inserted that are outside this range and therefore invalid.

Define a function to which we can pass an array containing the unfiltered values and it returns an array with the filtered values. For example, if the array passed is `{4, -1, 0, 89, 105, 67, 100}`, the method should return the array `{4, 0, 89, 67, 100}`.

## SCENARIO 5
Define a function that returns the number of distinct values in the array passed. For example, if the array passed is `{3, 7, 3, 3, 3, 20, 9, 20}`, return 4 as there are four distinct values (3, 7, 20 and 9).

## SCENARIO 6
Define a function that when passed an integer (store the value passed in the formal parameter `n`), returns an array that holds the first `n` prime numbers (a number is *prime* if it is more than or equal to 2 and is divisible by only 1 and itself).
