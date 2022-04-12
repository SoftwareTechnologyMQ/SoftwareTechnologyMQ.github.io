---
layout: page
title: Boolean Logic
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge:</summary>

<!--  * [Functions](./functions.html)
-->  

</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes:</summary>

  * Understand basic boolean operators: AND, OR, NOT
  * Determine outcome of boolean expressions.
  * Simplify boolean expressions.
  * Understand gate symbols and interpret simple circuits.
  * Understand universal gates.
  * Understand basic gates with multiple inputs.
  * Understand relationship between digital circuits and boolean algebra
  
</details>

## Author: Gaurav Gupta

# History behind "Boolean"

George Boole was an early 19th century English mathematician who worked in the field of differential equations and Boolean alegbra. Here's a link to his book, [The Laws of Thought](https://www.gutenberg.org/files/15114/15114-pdf.pdf) 

![](./assets/images/georgeBoole.jpg)

**Trivia time**: George Boole's house is at 5, Grenville Place, Cork.

# What is Boolean logic

Quite simply, boolean logic is the use of "and", "or", and "not" conditions. 

For example, "if it's raining OR if it's over 50 degrees celsius, take an umbrella" means that one must carry an umbrella if it's raining. One must also carry an umbrella if the temperature is over 50 degrees. On the other hand, "if it's raining AND if it's over 50 degrees celsius, take an umbrella" means that one must carry an umbrella if it's raining AND AT THE SAME TIME the temperature is over 50 degrees. 

"You are NOT stupid" explicitly means that the person is not unintelligent. But does it mean that the person is intelligent?!? Not really. Just like "The number is NOT positive" could mean the number being negative, or zero (which is neither positive nor negative).

"You are NOT NOT clever" means you are definitely clever!

# Why learn Boolean logic

Because of the complexity in data relationships leading to various outputs.

As a simple example, if I want to display all positive even numbers in red colour, all negative even numbers in green colour, and all (and only one) other even number in blue colour, I need to use Boolean logic.

# Boolean operators

## AND operator
`a AND b` is `true` when **both** `a` and `b` are `true`

| a | b | a AND b |
|---|---|------|
|false|false|false|
|false|true|false|
|true|false|false|
|true|true|true|

In Boolean algebra, `false` is represented by 0 and `true` is represented by 1. This is very handy because `AND` can be seen as **multiplication**.

| a | b | a AND b ( * ) |
|---|---|------|
|0|0|0|
|0|1|0|
|1|0|1|
|1|1|1|

## OR operator
`a OR b` is `true` when **either** `a` **or** `b` is `true`

| a | b | a OR b |
|---|---|------|
|false|false|false|
|false|true|true|
|true|false|true|
|true|true|true|

The `OR` operator can be seen as **addition**.

| a | b | a OR b ( + ) |
|---|---|------|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|1|

### Why is 1 + 1 = 1? 

Well, because we have binary states (0 or 1) so any overflow means you are limited to 1.

## NOT operator
`NOT a` is `true` when `a` is `false`.
`NOT a` is `false` when `a` is `true`.

| a | NOT a |
|---|---|
|false|true|
|true|false|
