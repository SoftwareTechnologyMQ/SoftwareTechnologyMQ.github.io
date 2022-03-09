---
layout: page
title: Primitive Operations of Processing
within: programming
---

<details class="prereq" markdown="1">
<summary>Assumed Knowledge</summary>
  * [Transition to Processing](./transition_to_processing)
</details>

<details class="outcomes" markdown="1">
<summary>Learning Outcomes</summary>
  * Be able to create static processing sketches and understand how they came to be.
  * Have the tools to create sketches based on your own imagination.
  * Understand the categories into which values might fit and the consequences of these categories.
</details>

# Drawing Primitives

## Reading

Chapters 1 and 2 of [Learning Processing](http://learningprocessing.com/) by Daniel Shiffman.  Macquarie University students have access to an electronic copy [via the library](https://multisearch.mq.edu.au/permalink/61MACQUARIE_INST/7h5qs5/alma99244413575302171).

<iframe width="560" height="315" src="https://www.youtube.com/embed/a562vsSI2Po" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/5N31KNgOO0g" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/n2oHuKG_BQc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Reading

[Coordinate System tutorial at processing.org](https://processing.org/tutorials/coordinatesystemandshapes).

## More Details

A processing program is made up of _expressions_ and _statements_.  Statements come later, this topic shows us how to build up expressions to get a program.

Processing has a whole pile of built in expressions you can use, most of which cause things to occur on the screen.  The full-set of expressions available are documented at [the processing reference page](https://processing.org/reference/) but we will list here all the ones you need in this text.  In processing, you also have a full suite of mathematical expressions available:

- Additive operators:
    - Addition (`+`), 
    - Subtraction (`-`), 
- Multiplicative operators:
    - Multiplication (`*`), 
    - Division (`/`),
    - Remainder (`%`)

Warning!: Division and remainder might now work the way you expect.  We will explain why in a later topic.

# Values and Types

So far, we have seen many _values_:

  * `1` is a value, the number one
  * `-34` is a value, the number -34
  * `3.4` is a value, the number 3.4

This might all seem terribly obvious, but it is about to become very important.

Values are grouped into _types_.  A type is a set of values that all work the same.  All the whole numbers work the same, so there is a type for these (`int`).  All the precise numbers work the same, so there is a type for these (`float`).  Here is a list of all the types you need to worry about:

  * `int` : whole numbers.  Examples are `1`,`2`,`-7`,`0`,`1023977389`.
  * `float`: numbers that might have decimal parts.  Examples are `1.2`,`2.45644`,`-13.0`,`0.0`.
  * `char`: single characters that might appear in text.  Examples include `c`, `g`, `^`, `$`, `@`, `z`.

<div class="task" markdown="1">
What type is each of the following values?

  * `12`
  * `41.0`
  * `0`
  * `0.0`
  * `'c'`
  * `'f'`
  * `'0'`
  * h
<details markdown="1">
<summary>solution</summary>

  * `12`: `int` (integer)
  * `41.0` : `float` (floating point number)
  * `0` : `int` (integer)
  * `0.0` : `float` (floating point number)
  * `'c'` : `char` (character)
  * `'f'` : `char` (character)
  * `'0'` : `char` (character)
  * h : **this is an error.  the processing compiler will reject values like this**
</details>
</div>

You must be careful to know what type any particular value has because it affects how the program runs.  For example, each of the basic operations we know about have particular effects based on the types it is working on.

<table border="1px" style="padding: 5px">
 <tr><th>type</th><th><code>+</code></th><th><code>-</code></th><th><code>*</code></th><th><code>/</code></th></tr>
    <tr><td><code>int</code></td><td>normal addition</td><td>normal subtraction</td><td>normal multiplication</td><td>integer division</td></tr>
    <tr><td><code>float</code></td><td>normal addition</td><td>normal subtraction</td><td>normal multiplication</td><td>normal division</td></tr>
    <tr><td><code>char</code></td><td>something strange</td><td>something strange</td><td>something strange</td><td>something strange</td></tr>
</table>

You will notice that mostly things work out as you expect, but you need to be aware of _integer division_ and _not doing arithmetic on characters_.  Don't ever try and do arithmetic on characters and as for integer division...


## But a `float` can be an `int`...

If you see the value `0`, how do you know if Processing thinks it is an `int` or a `float`?  Well, if you see `0`, it will think it is an `int` and if you see `0.0`, processing will think it is a `float`.  However, the back-and-forth between these two options gets complex once we get into more complicated code but for now, you need to be aware that it matters what Processing thinks a value is and you can make a pretty good guess at what it thinks.

Processing will also convert between some types if you ask it to.  In particular, it will very happily convert an `int` into a `float`.  You should be able to see why this is always OK.  It won't do the opposite though because not all floats have equivalent integers.

## Characters

While we are thinking about it, how does Processing know when I mean the _character_ `0` instead of the number `0`?  All characters are within inverted commas, so the character `0` will look like `'0'`.  The same holds for all other characters, they look like `'c'`, `'g'`, `'^'`, `'$'`, `'@'`, `'z'` in Processing code

<div class="task" markdown="1"><a name="blue_circle"></a>
Write processing code that will draw a blue circle that is 20 pixels wide in the center of the sketch window.  You should use [pantone 2178 C](https://www.pantone.com/color-finder/2718-C) as your inspiration.
<details markdown="1">
<summary>solution</summary>
~~~~~
noStroke();
fill(92, 136, 218); // These RGB values give the right shade of blue
circle(width/2, height/2, 20);
~~~~~
</details>
</div>

<div class="task" markdown="1">
Identify the _type_ of each item in the following code.
~~~~~
circle(width/2, height/2, 40);
~~~~~

  * What is the type of `width`
  * What is the type of `height`
  * What is the type of `2`
  * What is the type of `40`
  * What is the type of `width/2`
  * What is the type of `height/2`
  * `circle` expects `floats` according to the [processing reference](https://processing.org/reference/circle_.html).  How can you resolve this with your answers above.

<details markdown="1">
<summary>solution</summary>
  - <code>int</code> because it is set from <code>size</code> which only accepts <code>int</code>s
  - <code>int</code> because it is set from <code>size</code> which only accepts <code>int</code>s
  - <code>int</code> because if you don't say otherwise, processing treats numbers as integers
  - <code>int</code> because if you don't say otherwise, processing treats numbers as
  - <code>int</code> because dividing an <code>int</code> by another <code>int</code> will give you a third <code>int</code>
  - <code>int</code> because dividing an <code>int</code> by another <code>int</code> will give you a third <code>int</code>
  - It is always OK to give an <code>int</code> where a <code>float</code> should go, processing will automatically convert it for you.

</details>
</div>

## Order of operations

Fundamental rule is that when you apply an arithmetic operator on two values, say `a` and `b`, precision is maintained if at least one of them is a floating-point value. If they are both integer values, any precision (value after dot) is completely droppped.

For example,

- `17 + 5 = 22`
- `17 + 5.0 = 22.0`
- `17 - 5.3 = 11.7`
- `18.29 - 1 = 17.29`
- `7 * 5 = 35`
- `3 * 1.2 = 3.6`
- `17 / 5 = 3` (precision dropped)
- `17 / 5.0 = 3.4`
- `17.0 / 5.0 = 3.4`
- `5.0 / 1.2 = 4.16666`
- `17 % 5 = 2` (2 is what's left behind after creating 3 equal groups of 5 from 17)

### PRO-TIP: 

- `b` cannot be 0 in either `a / b` or `a%b`.
- `a / b` is non-negative when both a and b are non-negative, or when both a and b are negative.
- `a % b` is non-negative when a is non-negative.

The arithmetic operators we discussed earlier have the following order of precedence or priority:

1. Brackets `()`: Any operation inside a brackets must be perfomed before other operations outside the brackets.
2. Multiplicative operators `*, /, %`. In the order of occurrence in the expression.
3. Additive operators `+, -`. In the order of occurrence in the expression.

Examples:

- 5 + 20 / 3 = 5 + 6 = 11
- (5 + 20) / 3 = 25 / 3 = 8
- 5 + 20 / 3.0 = 5 + 6.6666 = 11.6666
- (5 + 20) / 3.0 = 25 / 3.0 = 8.3333
- 5 * 20 % 3 = 100 % 3 = 1
- 5 * (20 % 3) = 5 * 2 = 10
- (10 + 8) / ((20 - 15) * (12 / 5)) = 18 / (5 * 2) = 18 / 10 = 1
- (10 + 8) / ((20 - 15.0) * (12 / 5)) = 18 / (5.0 * 2) = 18 / 10.0 = 1.8

# Furthering your Understanding

<iframe width="560" height="315" src="https://www.youtube.com/embed/7FM0zvbHKnQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<p>

<iframe width="560" height="315" src="https://www.youtube.com/embed/y48q9MsztzE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
 
