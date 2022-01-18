---
layout: page
title: "Debugging in Java"
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge</summary>

  * [Transition to Java](transition_to_java)
</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes</summary>

  * Be able to identify input/output pairs that are good for debugging.
  * Be able to debug Java programs with appropriate tools.
  * Be able to do paper traces of Java code.

</details>

## Author: Gaurav Gupta

# Debugging

For any given problem, we design a solution and then implement it.

As an example, let's say that we are writing a program that gives you the number of digits in an integer. We expect the following *input-output mappings*.


| Input      | Output |
|------------|--------|
| 1729       | 4      |
| 1234567890 | 10     |
| 0          | 0      |
| -888       | 3      |
{: .table}

Now, it's possible that the actual outputs you get from your code are as follows,

| Input      | Output |
|------------|--------|
| 1729       | 4      |
| 1234567890 | 10     |
| 0          | 1      |
| -888       | 4      |
{: .table}

We need to find out why do some inputs have incorrect outputs. So we go through our design and implementation looking for possible bugs. A logical way to do this is to trace every variable at every stage and see where does the program deviate from the expected.

## Example 1

Consider the following code that is supposed to return the product of all integers from 1 to `n` (n >= 1).

<script src="https://gist.github.com/gaurav1780/71d8008cd4cc632dc6119b1594dcfe88.js"></script>

The input-output mappings are -

| Input      | Expected Output | Actual Output |
|------------|--|---|
| 4       | 24 	| 0 |
| 6 		| 720 	| 0 |
| 7      	| 5040	| 0 |
| 1      	| 1 	| 0 |
{: .table}

If you trace the program, you'll see that the loop executes when `i=1` and `result` becomes `result (0) * i (1) = 0`. And every subsequent time, `result` becomes `0 * i = 0`. A trace for `n=4` using *logic table* is provided below,

| i | i < 4 | result |
|---|-------|--------|
| 1 |  true | 0\*1 = 0|
| 2 |  true | 0\*2 = 0|
| 3 |  true | 0\*3 = 0|
| 4 |  false | |
{: .table}

Thus, the first bug is `result` should be initalized to 1 and not 0.

Our partially fixed code:

<script src="https://gist.github.com/gaurav1780/526b68d197c7c3a705780af2fcef93c1.js"></script>

The new input-output mappings are -

| Input      | Expected Output | Actual Output |
|------------|--|---|
| 4       | 24 	| 6 |
| 6 		| 720 	| 120 |
| 7      	| 5040	| 720 |
| 1      	| 1 	| 1 |
{: .table}

A trace for `n=4` using *logic table* is provided below,

| i | i < 4 | result |
|---|-------|--------|
| 1 |  true | 1\*1 = 1|
| 2 |  true | 1\*2 = 2|
| 3 |  true | 2\*3 = 6 (not the expected output)|
| 4 |  false | |
{: .table}

It can now be seen that the loop **should** execute for `i=4` and multiply it into the `result` but it doesn't. By changing `i < n` to `i <= n`, we fix this problem.

<script src="https://gist.github.com/gaurav1780/331fb94f328322b2fc4bd781ef22d18e.js"></script>

To confirm, we trace once more for `i=4`.

| i | i < 4 | result |
|---|-------|--------|
| 1 |  true | 1\*1 = 1|
| 2 |  true | 1\*2 = 2|
| 3 |  true | 2\*3 = 6|
| 4 |  true | 6\*4 = 24 (expected output)|
| 5 |  false | |
{: .table}

<div class="task" markdown="1">
Debug the following method for which the expected input-output mappings are provided in the javadoc (comment above the method).
<script src="https://gist.github.com/gaurav1780/111f98632dbb6068d4056df295341cf3.js"></script>
**CRITICAL STEP!!!** Write down the actual input-output mappings after every iteration of debugging
<details class="solution" markdown="1"><summary>solution</summary>
<script src="https://gist.github.com/gaurav1780/7556eea66978a974423447f544150841.js"></script>
</details>
</div>

## Performing debugging in Eclipse

Most of the modern Integrated Development Environments (IDEs) have a comprehensive debugging feature that let's you trace the variables as your program executes.

In the IDE we are using (Eclipse), the debugger relies of placing `breakpoints` that are like pitstops in car race. The program runs till the next breakpoint where you can see the values of all the variables and when you hit `resume`, it goes to the next breakpoint.

<iframe width="560" height="315" src="https://www.youtube.com/embed/NQTQVYhmsL0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

# Pen and paper methodology

At this point, it becomes tempting to throw away your notebook, you have everything you need in the programming environment right?

No.

Debugging is still mostly done in your head or on paper, so it is worth revisiting our programming tracing skills.  What follows is a set of exercises for you to get familiar with tracing Java code.  You should do all these exercises with just a pen/pencil and paper as the skill you are training is to be able to trace a program _without_ the aid of a computer.

<div class="task" markdown="1">
Trace the flow of the following program and determine the value of `result` at the end of it.
<script src="https://gist.github.com/gaurav1780/767824769b5456ddb080e63d84124d70.js"></script>
<details class="solution" markdown="1"><summary>solution</summary>
`a < b` is `true`

`b % a == 0` is `true`

`a % 2 == 0` is `false`

The expression becomes `true && true && false`

This is `false`

Hence, the `else` block executes and `result` becomes `b (10)`.
</details>
</div>

<div class="task" markdown="1">
Trace the flow of the following program and determine the value of `result` at the end of it.
<script src="https://gist.github.com/gaurav1780/0f335474bbbf8fcf488150b7b411c33a.js"></script>
<details class="solution" markdown="1"><summary>solution</summary>
a == b` is `false`,
`else` executes

`b` decreases by 5, becomes 5
`a == b` is `true`.
`if` block executes and `result` becomes `b (5)`.
</details>
</div>

<div class="task" markdown="1">
Trace the flow of the following program and determine the value of `result` at the end of it.
<script src="https://gist.github.com/gaurav1780/0302ce7e20a43b1807584b4ca7f49ce7.js"></script>
<details class="solution" markdown="1"><summary>solution</summary>
| i | i&lt;=7 | i%2 | i%2==1 | result |
| --- | --- | --- | --- | --- |
| 1 | true | 1 | true | -3+1 = -2 |
| 2 | true | 0 | false | |
| 3 | true | 1 | true | -2+3 = 1 |
| 4 | true | 0 | false | |
| 5 | true | 1 | true | 1+5 = 6 |
| 6 | true | 0 | false | |
| 7 | true | 1 | true | 6+7 = 13 |
| 8 | false | | | |
{: .table}

</details>
</div>

<div class="task" markdown="1">
Trace the flow of the following code -
<script src="https://gist.github.com/gaurav1780/0b8969cabc916cff8ed88cfcde631560.js"></script>
<details class="solution" markdown="1"><summary>solution</summary>
## Solution
At the end of the code,
`a = 5`, `b = 10`, `c = 2`, `d = false`, `result = 10`.
Explanation -
<script src="https://gist.github.com/gaurav1780/7edd01a8e4ae3182e3ddd7f6166a0e53.js"></script>
</details>
</div>
