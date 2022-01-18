---
layout: page
title: Variables
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge</summary>

  * [Primitive Operations](./primitive_operations)
  * [Algorithms](./algorithms)
</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes</summary>

  * Understand what a variable is
  * Understand how variables are written in processing
  * Write code that requires variables
  * Understand how variables support animation
  * Understand how variables correspond to named memory slots

</details>

{: .keypoint}
Variables are a slot of memory in the computer with a name.

{: .readings}
Chapters 3 and 4 of [Learning Processing](https://learningprocessing.com) by Danel Shiffman.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ibW4oA7-n8I" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/UvSjtiW-RH8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/B-ycSR3ntik?list=PLRqwX-V7Uu6aFNOgoIMSbSYOkKNTo89uf" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/rZ36BzXFT6Q?list=PLRqwX-V7Uu6aFNOgoIMSbSYOkKNTo89uf" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/50Rzvxvi8D0?list=PLRqwX-V7Uu6aFNOgoIMSbSYOkKNTo89uf" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Expressions or Statements

Every part of a program can be clasified as a _statement_ or an _expression_ and it is useful to do so.

A _statement_ is a section of code that _does something_.  For example, it might update a memory location, or draw something to the screen

An _expression_ is a section of code that _has a value_.  For example `2` has the value 2 (obvioulsy).  A more complex example is

~~~~~
int x;
x = 5;
~~~~~

`x` is also an expression, it's value is 5.

### Rules

  * Values are expressions
  * Variables are expressions
  * Declations (such as `int x`) are statements
  * Assignments (such as `x = 5`) are statements

Notice that the assignment statement is made up of two expressions connected with an `=` symbol?

## How memory works

Before we can fully grasp this, we need to update our understanding of how a Processing program runs.  In [an earlier topic](./transition_to_processing) we saw program execution as a conversation between user, compiler, processing and computer.  This model still holds but we need to add to it.  When _processing_ is doing its thing, it has access to a bank of memory and it might put things in there or read things out of there.

From here on in, we will tend to leave out the conversation because it is the same every time, but we will often look to the memory bank to see what is going on in our program.

We visualise this memory bank as a grid of buckets (we will also call a bucket a "slot in memory").  Each bucket may hold a value.  A program with no variables, will have a memory that looks like a grid of empty holes

<svg xmlns="http://www.w3.org/2000/svg" height="200" width="400" version="1.1" viewBox="0 0 105.83333 52.916666">
 <g transform="translate(0 -244.1)">
  <rect height="37.04" width="35.72" stroke="#000" y="249.4" x="3.969" stroke-width=".2495" fill="none"/>
  <g stroke="#000" fill="none">
   <g stroke-width="0.26px">
    <path d="m7.937 249.4v37.04"/>
    <path d="m11.91 249.4v37.04"/>
    <path d="m15.88 249.4v37.04"/>
    <path d="m19.84 249.4v37.04"/>
    <path d="m23.81 249.4v37.04"/>
    <path d="m27.78 249.4v37.04"/>
    <path d="m31.75 249.4v37.04"/>
    <path d="m35.72 249.4v37.04"/>
   </g>
   <g stroke-width=".2646px">
    <path d="m3.969 253.3h35.72"/>
    <path d="m3.969 257.3h35.72"/>
    <path d="m3.969 262.6h35.72"/>
    <path d="m3.969 266.6h35.72"/>
    <path d="m3.969 270.5h35.72"/>
    <path d="m3.969 274.5h35.72"/>
    <path d="m3.969 278.5h35.72"/>
    <path d="m3.969 282.4h35.72"/>
   </g>
  </g>
 </g>
</svg>

Whereas a program that is using two slots to hold the values 1 and 15 will look like

<svg xmlns="http://www.w3.org/2000/svg" height="200" width="400" version="1.1" viewBox="0 0 105.83333 52.916666">
 <g transform="translate(0 -244.1)">
  <rect height="37.04" width="35.72" stroke="#000" y="249.4" x="3.969" stroke-width=".2495" fill="none"/>
  <g stroke="#000" fill="none">
   <g stroke-width="0.26px">
    <path d="m7.937 249.4v37.04"/>
    <path d="m11.91 249.4v37.04"/>
    <path d="m15.88 249.4v37.04"/>
    <path d="m19.84 249.4v37.04"/>
    <path d="m23.81 249.4v37.04"/>
    <path d="m27.78 249.4v37.04"/>
    <path d="m31.75 249.4v37.04"/>
    <path d="m35.72 249.4v37.04"/>
   </g>
   <g stroke-width=".2646px">
    <path d="m3.969 253.3h35.72"/>
    <path d="m3.969 257.3h35.72"/>
    <path d="m3.969 262.6h35.72"/>
    <path d="m3.969 266.6h35.72"/>
    <path d="m3.969 270.5h35.72"/>
    <path d="m3.969 274.5h35.72"/>
    <path d="m3.969 278.5h35.72"/>
    <path d="m3.969 282.4h35.72"/>
   </g>
  </g>
  <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" font-size="2.606px" line-height="1.25" y="252.33713" x="4.2684984" font-family="sans-serif" fill="#000000"><tspan y="252.33713" x="4.2684984" stroke-width=".06515">15</tspan></text>
  <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" font-size="2.606px" line-height="1.25" y="256.35089" x="4.3520851" font-family="sans-serif" fill="#000000"><tspan y="256.35089" x="4.3520851" stroke-width=".06515">1</tspan></text>
 </g>
</svg>

Or those same values might end up in other memory slots (buckets)

<svg xmlns="http://www.w3.org/2000/svg" height="200" width="400" version="1.1" viewBox="0 0 105.83333 52.916666">
 <g transform="translate(0 -244.1)">
  <rect height="37.04" width="35.72" stroke="#000" y="249.4" x="3.969" stroke-width=".2495" fill="none"/>
  <g stroke="#000" fill="none">
   <g stroke-width="0.26px">
    <path d="m7.937 249.4v37.04"/>
    <path d="m11.91 249.4v37.04"/>
    <path d="m15.88 249.4v37.04"/>
    <path d="m19.84 249.4v37.04"/>
    <path d="m23.81 249.4v37.04"/>
    <path d="m27.78 249.4v37.04"/>
    <path d="m31.75 249.4v37.04"/>
    <path d="m35.72 249.4v37.04"/>
   </g>
   <g stroke-width=".2646px">
    <path d="m3.969 253.3h35.72"/>
    <path d="m3.969 257.3h35.72"/>
    <path d="m3.969 262.6h35.72"/>
    <path d="m3.969 266.6h35.72"/>
    <path d="m3.969 270.5h35.72"/>
    <path d="m3.969 274.5h35.72"/>
    <path d="m3.969 278.5h35.72"/>
    <path d="m3.969 282.4h35.72"/>
   </g>
  </g>
  <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" font-size="2.606px" line-height="1.25" y="252.33713" x="4.2684984" font-family="sans-serif" fill="#000000"><tspan y="252.33713" x="12.2684984" stroke-width=".06515">15</tspan></text>
  <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" font-size="2.606px" line-height="1.25" y="256.35089" x="4.3520851" font-family="sans-serif" fill="#000000"><tspan y="265.35089" x="4.3520851" stroke-width=".06515">1</tspan></text>
 </g>
</svg>
But memory slots don't just fill themselves, they only get a value if we put one in there.  The way to put values in memory slots is to name a slot, then fill it, and that is what we do with variables.

~~~~~
int x;
x = 5;
~~~~~

is processing code to _pick a new slot and name it "x"_ (`int x`) and _put 5 in that slot_ (`x = 5`).  The end result is memory that looks like this

<svg xmlns="http://www.w3.org/2000/svg" height="200" width="400" version="1.1" viewBox="0 0 105.83333 52.916666">
 <defs>
  <marker id="Arrow2Mend" refY="0.0" refX="0.0" orient="auto" overflow="visible">
   <path stroke-linejoin="round" d="m8.719 4.034l-10.93-4.018 10.93-4.018c-1.746 2.372-1.736 5.618 0 8.036z" fill-rule="evenodd" transform="scale(.6) rotate(180) translate(0)" stroke="#000" stroke-width=".625"/>
  </marker>
 </defs>
 <g transform="translate(0 -244.1)">
  <rect height="37.04" width="35.72" stroke="#000" y="249.4" x="3.969" stroke-width=".2495" fill="none"/>
  <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" font-size="5.58px" line-height="1.25" y="253.92084" x="59.796474" font-family="sans-serif" fill="#000000"><tspan y="253.92084" x="59.796474" stroke-width=".2646">x</tspan></text>
  <g stroke="#000" fill="none">
   <path marker-end="url(#Arrow2Mend)" d="m58.21 250.7-49.9 0.4" stroke-width=".2761"/>
   <g stroke-width="0.26px">
    <path d="m7.937 249.4v37.04"/>
    <path d="m11.91 249.4v37.04"/>
    <path d="m15.88 249.4v37.04"/>
    <path d="m19.84 249.4v37.04"/>
    <path d="m23.81 249.4v37.04"/>
    <path d="m27.78 249.4v37.04"/>
    <path d="m31.75 249.4v37.04"/>
    <path d="m35.72 249.4v37.04"/>
   </g>
   <g stroke-width=".2646px">
    <path d="m3.969 253.3h35.72"/>
    <path d="m3.969 257.3h35.72"/>
    <path d="m3.969 262.6h35.72"/>
    <path d="m3.969 266.6h35.72"/>
    <path d="m3.969 270.5h35.72"/>
    <path d="m3.969 274.5h35.72"/>
    <path d="m3.969 278.5h35.72"/>
    <path d="m3.969 282.4h35.72"/>
   </g>
  </g>
  <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" font-size="2.606px" line-height="1.25" y="252.33713" x="4.2684984" font-family="sans-serif" fill="#000000"><tspan y="252.33713" x="4.2684984" stroke-width=".06515">5</tspan></text>
 </g>
</svg>

Alternately, the same code might make the following situation - we don't know the exact memory location that will be used, but _we do know_ it will be called `x`.
<svg xmlns="http://www.w3.org/2000/svg" height="200" width="400" version="1.1" viewBox="0 0 105.83333 52.916666">
 <defs>
  <marker id="Arrow2Mend" refY="0.0" refX="0.0" orient="auto" overflow="visible">
   <path stroke-linejoin="round" d="m8.719 4.034l-10.93-4.018 10.93-4.018c-1.746 2.372-1.736 5.618 0 8.036z" fill-rule="evenodd" transform="scale(.6) rotate(180) translate(0)" stroke="#000" stroke-width=".625"/>
  </marker>
 </defs>
 <g transform="translate(0 -244.1)">
  <rect height="37.04" width="35.72" stroke="#000" y="249.4" x="3.969" stroke-width=".2495" fill="none"/>
  <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" font-size="5.58px" line-height="1.25" y="253.92084" x="59.796474" font-family="sans-serif" fill="#000000"><tspan y="253.92084" x="59.796474" stroke-width=".2646">x</tspan></text>
  <g stroke="#000" fill="none">
   <path marker-end="url(#Arrow2Mend)" d="m58.21 250.7-39.9 12.4" stroke-width=".2761"/>
   <g stroke-width="0.26px">
    <path d="m7.937 249.4v37.04"/>
    <path d="m11.91 249.4v37.04"/>
    <path d="m15.88 249.4v37.04"/>
    <path d="m19.84 249.4v37.04"/>
    <path d="m23.81 249.4v37.04"/>
    <path d="m27.78 249.4v37.04"/>
    <path d="m31.75 249.4v37.04"/>
    <path d="m35.72 249.4v37.04"/>
   </g>
   <g stroke-width=".2646px">
    <path d="m3.969 253.3h35.72"/>
    <path d="m3.969 257.3h35.72"/>
    <path d="m3.969 262.6h35.72"/>
    <path d="m3.969 266.6h35.72"/>
    <path d="m3.969 270.5h35.72"/>
    <path d="m3.969 274.5h35.72"/>
    <path d="m3.969 278.5h35.72"/>
    <path d="m3.969 282.4h35.72"/>
   </g>
  </g>
  <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" font-size="2.606px" line-height="1.25" y="252.33713" x="4.2684984" font-family="sans-serif" fill="#000000"><tspan y="265.33713" x="12.2684984" stroke-width=".06515">5</tspan></text>
 </g>
</svg>

<iframe width="560" height="315" src="https://www.youtube.com/embed/5FSPd60GttU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<div class="task" markdown="1">
Draw what the computer memory will look like after the following code has run

~~~~~
int y;
int x;

y = 10;
x = y + 5;
~~~~~
<details><summary>Solution</summary>
  <svg xmlns="http://www.w3.org/2000/svg" height="200" width="400" version="1.1" viewBox="0 0 105.83333 52.916666">
 <defs>
  <marker id="Arrow2Mend" refY="0.0" refX="0.0" orient="auto" overflow="visible">
   <path stroke-linejoin="round" d="m8.719 4.034l-10.93-4.018 10.93-4.018c-1.746 2.372-1.736 5.618 0 8.036z" fill-rule="evenodd" transform="scale(.6) rotate(180) translate(0)" stroke="#000" stroke-width=".625"/>
  </marker>
 </defs>
 <g transform="translate(0 -244.1)">
  <rect height="37.04" width="35.72" stroke="#000" y="249.4" x="3.969" stroke-width=".2495" fill="none"/>
  <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" font-size="5.58px" line-height="1.25" y="253.92084" x="59.796474" font-family="sans-serif" fill="#000000"><tspan y="253.92084" x="59.796474" stroke-width=".2646">x</tspan></text>
  <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" font-size="5.58px" line-height="1.25" y="261.315" x="59.732178" font-family="sans-serif" fill="#000000"><tspan y="261.315" x="59.732178" stroke-width=".2646">y</tspan></text>
  <g stroke="#000" fill="none">
   <path marker-end="url(#Arrow2Mend)" d="m58.21 250.7-49.9 0.4" stroke-width=".2761"/>
   <g stroke-width="0.26px">
    <path d="m7.937 249.4v37.04"/>
    <path d="m11.91 249.4v37.04"/>
    <path d="m15.88 249.4v37.04"/>
    <path d="m19.84 249.4v37.04"/>
    <path d="m23.81 249.4v37.04"/>
    <path d="m27.78 249.4v37.04"/>
    <path d="m31.75 249.4v37.04"/>
    <path d="m35.72 249.4v37.04"/>
   </g>
   <g stroke-width=".2646px">
    <path d="m3.969 253.3h35.72"/>
    <path d="m3.969 257.3h35.72"/>
    <path d="m3.969 262.6h35.72"/>
    <path d="m3.969 266.6h35.72"/>
    <path d="m3.969 270.5h35.72"/>
    <path d="m3.969 274.5h35.72"/>
    <path d="m3.969 278.5h35.72"/>
    <path d="m3.969 282.4h35.72"/>
    <path marker-end="url(#Arrow2Mend)" d="m58.21 260-48.95-4"/>
   </g>
  </g>
  <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" font-size="2.606px" line-height="1.25" y="252.33713" x="4.2684984" font-family="sans-serif" fill="#000000"><tspan y="252.33713" x="4.2684984" stroke-width=".06515">15</tspan></text>
  <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" font-size="2.606px" line-height="1.25" y="256.35089" x="4.3520851" font-family="sans-serif" fill="#000000"><tspan y="256.35089" x="4.3520851" stroke-width=".06515">10</tspan></text>
 </g>
</svg>
</details>
</div>

<div class="task" markdown="1">
Draw what the computer memory will loop like after the following code has run

~~~~~
int x;
x = 5;
int y;
y = 25;

x = y;
y = x;
~~~~~

Was the result what you expected?
<details><summary>Solution</summary>
  <svg xmlns="http://www.w3.org/2000/svg" height="200" width="400" version="1.1" viewBox="0 0 105.83333 52.916666">
 <defs>
  <marker id="Arrow2Mend" refY="0.0" refX="0.0" orient="auto" overflow="visible">
   <path stroke-linejoin="round" d="m8.719 4.034l-10.93-4.018 10.93-4.018c-1.746 2.372-1.736 5.618 0 8.036z" fill-rule="evenodd" transform="scale(.6) rotate(180) translate(0)" stroke="#000" stroke-width=".625"/>
  </marker>
 </defs>
 <g transform="translate(0 -244.1)">
  <rect height="37.04" width="35.72" stroke="#000" y="249.4" x="3.969" stroke-width=".2495" fill="none"/>
  <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" font-size="5.58px" line-height="1.25" y="253.92084" x="59.796474" font-family="sans-serif" fill="#000000"><tspan y="253.92084" x="59.796474" stroke-width=".2646">x</tspan></text>
  <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" font-size="5.58px" line-height="1.25" y="261.315" x="59.732178" font-family="sans-serif" fill="#000000"><tspan y="261.315" x="59.732178" stroke-width=".2646">y</tspan></text>
  <g stroke="#000" fill="none">
   <path marker-end="url(#Arrow2Mend)" d="m58.21 250.7-49.9 0.4" stroke-width=".2761"/>
   <g stroke-width="0.26px">
    <path d="m7.937 249.4v37.04"/>
    <path d="m11.91 249.4v37.04"/>
    <path d="m15.88 249.4v37.04"/>
    <path d="m19.84 249.4v37.04"/>
    <path d="m23.81 249.4v37.04"/>
    <path d="m27.78 249.4v37.04"/>
    <path d="m31.75 249.4v37.04"/>
    <path d="m35.72 249.4v37.04"/>
   </g>
   <g stroke-width=".2646px">
    <path d="m3.969 253.3h35.72"/>
    <path d="m3.969 257.3h35.72"/>
    <path d="m3.969 262.6h35.72"/>
    <path d="m3.969 266.6h35.72"/>
    <path d="m3.969 270.5h35.72"/>
    <path d="m3.969 274.5h35.72"/>
    <path d="m3.969 278.5h35.72"/>
    <path d="m3.969 282.4h35.72"/>
    <path marker-end="url(#Arrow2Mend)" d="m58.21 260-48.95-4"/>
   </g>
  </g>
  <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" font-size="2.606px" line-height="1.25" y="252.33713" x="4.2684984" font-family="sans-serif" fill="#000000"><tspan y="252.33713" x="4.2684984" stroke-width=".06515">25</tspan></text>
  <text style="word-spacing:0px;letter-spacing:0px" xml:space="preserve" font-size="2.606px" line-height="1.25" y="256.35089" x="4.3520851" font-family="sans-serif" fill="#000000"><tspan y="256.35089" x="4.3520851" stroke-width=".06515">25</tspan></text>
 </g>
</svg>


<p>You might have expected one of the memory slots to hold `5` but if you trace the code, that can't ever happen.</p>
</details></div>

<div class="task" markdown="1">
What is the output of the following processing snippet?

```
int x = 4;
int y = x;
x = 7;
println(y);
```
<details markdown="1"><summary>Solution</summary>
The answer is `4`.  Some people will think the answer is `7` reasoning that after line 2 `x` and `y` are linked but variables don't work that way.  The value in slot `x` is copied to slot `y` in line 2 (i.e. `4`) but that is the only link between them
</details>
</div>

<div class="task" markdown="1"><a name="animated_blue_circle"></a>
Write a processing program that moves a blue circle from the top of the screen to the bottom of the screen over time.  If you have forgotten how to put a blue circle on the screen, you should review this [previous exercise](./primitive_operations.html#blue_circle).
<details class="solution" markdown="1"><summary>solution</summary>
The problem description does not directly relate to variables, so we need to "re-interpret" it to put it into "code-speak".  Another way to consider the problem statement (as a Processing programmer) is "write a program where a blue circle is drawn on the screen and every time it is drawn it moves downwards a little.""


Compared to the solution to the [previous exercise](./primitive_operations.html#blue_circle), we need to:

  * Introduce the `setup` and `draw` functions.  You can't have animated programs without them.
  * Stop using a set-value for the y-position of the circle and introduce a variable for this `ypos` instead.
  * Start that variable at 0 when the program starts.  `setup` is run once when the program starts, so that is the right place to put it.
  * Clear the background everytime the sketch is drawn so that old circles go away.
  * Change the value of the variable each time the sketch is drawn so it is set to a new value ready for the next screen drawing.

~~~~~
int ypos;

void setup(){
  ypos = 0;
}

void draw(){
  background(255);
  noStroke();
  fill(92, 136, 218);
  circle(width/2, ypos, 20);
  ypos++;
}
~~~~~
</details></div>

## Some more details of randomness

In processing, we can get a random real number between 0 and `n` (including 0 but **excluding** `n`) using,

```java
double r = random(n);
```

If we cast the result to an integer, that integer will be between 0 and `n` (including 0 but **excluding** `n`)

```java
int z = (int)r;
```

<div class="task" markdown="1"><a name="timed_animated_blue_circle"></a>
_Difficult:_ Write a processing program that moves a blue circle from the top of the window to the bottom of the window in exactly 200 frames of time, no matter what the size of the window is.  If you have forgotten how to put animate blue circle on the screen, you should review this [previous exercise](./variables#animated_blue_circle).
<details class="solution" markdown="1"><summary>solution</summary>
Here we need to use one variable (the `height` variable) to determine the value in another variable.  Another way to consider the problem statement (as a Processing programmer) is "write a program where a blue circle is drawn on the screen and every time it is drawn it moves downwards a little.  The amount it moves downward each time is 1/200th of the height of the window.""


Compared to the solution to the [previous exercise](./variables.html#animated_blue_circle), we need to start using a variable to control the speed of the circle.  That variable must be a `float` because we will be dividing the size of the screen by 200 and we have no idea what the size of the screen might be.  This means we also need to move to a `float` for the position on the screen.  NB: `circle` will happily accept an `int` or a `float`, so we have no further changes to make there.

~~~~~
float ypos;
float yspeed;

void setup(){
  size(800,800);
  ypos = 0;
  yspeed = height/200;
}

void draw(){
  background(255);
  noStroke();
  fill(92, 136, 218);
  circle(width/2, ypos, 20);
  ypos = ypos + speed;
}
~~~~~

Experiment with this program by changing what is in line 5 and checking the animation still takes the same amount of time.

**Hold-on!** It's not working????  This solution is actually wrong thanks to a subtlety of how `int`s and `float`s are divided.  See what happens when the height of the window goes below 200 (say 100)?  The circle does not move.  If we "think backwards from the problem to what must be happening" we see that `yspeed` must be getting set to `0`, but how?  Well `100/200` is 0.5 in `float` arithmetic, but it is `0` in `int` arithmetic.  So processing must be using `int` arithmetic. But why?  `height` is an `int`, and, because procesing uses the _left-most_ number to decide which type of arithmetic to use, `int`/`float` is done in `int` arithmetic, so we have to convert `height` to a `float` _first_. <aside>"tricky" rules like `int`/`float` being different from `float`/`int` are called _edge cases_ and are frequent sources of bugs.  You can't remember all the edge cases, so you often need to work backwards and think what "must be" true to find them</aside>

~~~~~
float ypos;
float yspeed;

void setup(){
  size(800,800);
  ypos = 0;
  float h = (float)height;
  yspeed = h/200;
}

void draw(){
  background(255);
  noStroke();
  fill(92, 136, 218);
  circle(width/2, ypos, 20);
  ypos = ypos + yspeed;
}
~~~~~

Experiment with _this_ program.  It works this time!
</details></div>

# Furthering your understanding

<iframe width="560" height="315" src="https://www.youtube.com/embed/uEbiuMOu2TM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
