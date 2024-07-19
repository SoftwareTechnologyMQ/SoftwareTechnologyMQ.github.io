---
layout: page
title: Boolean Expressions in Java
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge:</summary>

  * [Primitive Operations](./primitive_operations)
  * [Variables](./variables.html)

</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes:</summary>

  * Understand basic boolean operators: AND, OR, NOT
  * Determine outcome of boolean expressions.
  * Simplify boolean expressions.
  
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

# Boolean expressions

Any expression or operation that evaluates to a Boolean value is called a Boolean expression.

The simplest Boolean expressions involve comparing two values, for which we need *relational operators*.

## Relational operators

The following are the six relational operators we will use:

| Operator | Meaning | Example |
|---|---|------|
|`>`|Greater than|`5.4 > 3` = `true` while `3 > 5` = `false`|
|`<`|Lesser than|`5 < 3.6` = `false` while `3 < 5.1` = `true`|
|`>=`|Greater than or equal to|`5 >= 5` = `true` while `3 >= 5` = `false`|
|`<=`|Lesser than or equal to|`5 <= 3` = `false` while `5 <= 5` = `true`|
|`==`|Equal to|`5.2 == 5.2` = `true` while `6.4 == 6.5` = `false`|
|`!=`|Not equal to|`5 != 3.9` = `true` while `5 != 5` = `false`|

<iframe width="560" height="315" src="https://www.youtube.com/embed/FCM54REaY58" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# Boolean operators

For this section, we will assume that `a` and `b` are `boolean` values (`true` or `false`)

## `&&` (and) operator

`a && b` is `true` when **both** boolean operands, `a` and `b`, are `true`

| a | b | a && b |
|---|---|------|
|`false`|`false`|`false`|
|`false`|`true`|`false`|
|`true`|`false`|`false`|
|`true`|`true`|`true`|

Examples:

- `10/2 == 5 && 12/2 == 6` = `true` (because BOTH sub-expressions are `true`)
- `10/2 == 5 && 12/2 == 4` = `false` (because second sub-expression is `false`)
- `10/2 == 4 && 12/2 == 6` = `false` (because first sub-expression is `false`)
- `10/2 == 4 && 12/2 == 4` = `false` (because BOTH sub-expressions are `false`)


## `||` (or) operator
`a || b` is `true` when **either** of the boolean operands, `a` **or** `b`, is `true`.

<!-- &#124; is pipe -->

| a | b | a &#124;&#124; b |
|---|---|------|
|`false`|`false`|`false`|
|`false`|`true`|`true`|
|`true`|`false`|`true`|
|`true`|`true`|`true`|

<!--<table>
    <tr>
        <td><b>a</b></td>
        <td><b>b</b></td>
        <td><b>a || b</b></td>
    </tr>
    <tr>
        <td>false</td>
        <td>false</td>
        <td>false</td>
    </tr>
    <tr>
        <td>false</td>
        <td>true</td>
        <td>true</td>
    </tr>
    <tr>
        <td>true</td>
        <td>false</td>
        <td>true</td>
    </tr>
    <tr>
        <td>true</td>
        <td>true</td>
        <td>true</td>
    </tr>
</table>-->

Examples:

- `10/2 == 5 || 12/2 == 6` = `true` (because both sub-expressions are `true`)
- `10/2 == 5 || 12/2 == 4` = `true` (because first sub-expression is `true`)
- `10/2 == 4 || 12/2 == 6` = `true` (because second sub-expression is `true`)
- `10/2 == 4 || 12/2 == 4` = `false` (because BOTH sub-expressions are `false`)


## `!` (not) operator

The `!` (not) operator negates the boolean value to which it is applied.

| a | !a |
|---|---|
|`false`|`true`|
|`true`|`false`|

Examples:

- `!(10/2 == 5)` = `false` because the expression `(10/2 == 5)` which is `true` is negated by the `!`.
- `!(5 < 3)` = `true` because the expression `(5 < 3)` which is `false` is negated by the `!`.
- `!!!!(5 < 3)` = `false`.

<iframe width="560" height="315" src="https://www.youtube.com/embed/vsgYPNpvj-A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# Order of operations

Order of operations is,

1. Bracketed boolean sub-expressions
2. Then, Relational operators (left to right)
3. Then, `!`
3. Then, `&&`
4. Then, `||`

# Short-circuit logic

## Short-circuiting `&&`

If the first of the two values separated by `&&` is `false`, the expression is evaluated to `false` without evaluating the second value. That is,

```java
false && b = false //irrespective of the value of b
```
For example:

```java
int a = 3;
boolean b = a>=10 && a<=20;
```

Here, 

- `a>=10` is,
- `3>=10` which is, 
- `false`

Hence, the expression becomes:

```java
false && a<=20
```

But, both `false && false` and `false && true` are `false`.
So, no need to evaluate the second sub-expression.

## Short-circuiting `||`

If the first of the two values separated by `||` is `true`, the expression is evaluated to `true` without evaluating the second value. That is,

```java
true || b = true //irrespective of the value of b
```
|Short-circuit logic summary|
|---|
|<code>false && anything = false</code>|
|<code>true &#124;&#124; anything = true</code>|

Examples:

- `&&`

	`true && true && true && false && true && true && true` 

	= `true && true && false && true && true && true` 

	= `true && false && true && true && true` 

	= `false && true && true && true` 
	
	= `false`

- `||`

	`false || false || false || true || true || false || true` 

	= `false || false || true || true || false || true` 

	= `false || true || true || false || true`

	= `true || true || false || true` 
	
	= `true`


# Questions

What are the following Boolean expressions evaluated to?

1. `6 > 4`
1. `6 > 4 == true`
1. `6 < 4`
1. `6 < 4 == true`
1. `!true`
1. `!"Done"`
1. `!!!!true`
1. `!!false`
1. `6 >= 4 && 6 < 1`
1. `6 >= 4 || 6 < 1`
1. `6 >= 4 || 10`
1. `true || false && false`
1. `!(6 >= 4) && 6 < 1`
1. `!(6 >= 4) || 6 < 1`
1. `!(1 == 7 && 2 == 9)`
1. `1==2 || 3==4 || 5==6 || 7==8 || true`
1. `1==2 && 3==4 && 5==6 && 7==8 && true`
1. `!(1 == 7 && 2 == 9) && !(true && !false)`
1. `20 == 4 && 12*31 >= 41*9 && 1973%127 > 50 && 1000==1000`
1. `2+8 == 10 || 1729*9271 != 16029559 || 1000==2000`

For what values of `x` (and `y` if applicable) will the following Boolean expressions be `true`? Where convenient, you can give your answer in form of a sentence.

1. `x > 10`
2. `x >= 10`
3. `x % 5 == 0`
4. `x / 5 == 0`
5. `x % y == 0`
6. `x >= 10 && x <= 20`
7. `x > 1 && x < 6`
8. `x > 1 || x < 6`
9. `!(x >= 10 && x <= 20)`
10. `x % y == 0 && y % x == 0`

Fix the following expressions based on their stated intent:

1. Expression should evaluate to `true` if `x` is an even integer over 100. Current version: `x / 2 == 0 && x > 100`.
2. Expression should evaluate to `true` if `x` is a multiple of both 7 and 11. Current version: `x % 7 == 0 || x % 11 == 0`.
3. Expression should evaluate to `true` if either `x` or `y` is a positive integer. Current version: `x >= 0 || y >= 0`.
4. Expression should evaluate to `true` if both `x` and `y` are outside the range [1, 6]. Current version: `x < 1 || x > 6 && y < 1 || y > 6`.

# Solutions

Outcomes of Boolean expressions:

1. `6 > 4` = `true`
2. `6 > 4 == true` = `true` 
3. `6 < 4` = `false`
4. `6 < 4 == true` = `false` 
 	- `exp == true` and `exp` are the same. 
 	-  `exp == false` and `!exp` are the same.
5. `!true` = `false`
6. `!"Done"` invalid (`!` doesn't operate on String variables)
7. `!!!!true` = `true`
8. `!!false` = `false`
9. `6 >= 4 && 6 < 1` = `false`
10. `6 >= 4 || 6 < 1` = `true`
11. `6 >= 4 || 10` invalid (right hand side value is integer, not boolean)
12. `true || false && false` = `true` (`&&` is before `||` in precedence)
13. `!(6 >= 4) && 6 < 1` = `false`
14. `!(6 >= 4) || 6 < 1` = `false`
15. `!(1 == 7 && 2 == 9)` = `true`
16. `1==2 || 3==4 || 5==6 || 7==8 || true` = `true`
17. `1==2 && 3==4 && 5==6 && 7==8 && true` = `false`
18. `!(1 == 7 && 2 == 9) && !(true && !false)` = `false`
19. `20 == 4 && 12*31 >= 41*9 && 1973%127 > 50 && 1000==1000` = `false` (short-circuit `&&`)
20. `2+8 == 10 || 1729*9271 != 16029559 || 1000==2000` = `true` (short circuit `||`)


Values of variables for which expressions are `true`:

1. `x > 10`: when x is more than 10. If x is an integer, then 11, 12 ..., if x is a float, then 10.00001, 10.00002, ...
2. `x >= 10`: for any x that is 10 or more.
3. `x % 5 == 0`: for any x that is a multiple of 5, or in other words, any x that is divisible by 5.
4. `x / 5 == 0`: for any x between -4 and 4 (inclusive on both sides), represented by range [-4, 4]
5. `x % y == 0`: for an x, y pair such that x is divisible by y (or x is a multiple of y).
6. `x >= 10 && x <= 20`: for x in the range [10, 20]
7. `x > 1 && x < 6`: for x in the range (1, 6), excluding 1 and 6 themselves. This is represented by round brackets as opposed to square brackets.
8. `x > 1 || x < 6`: for any value of x (think :D)
9. `!(x >= 10 && x <= 20)`: for any value of x OUTSIDE the range [10, 20]
10. `x % y == 0 && y % x == 0`: for an x, y pair such that they are the same or negative of each other (x = 12, y = 12 or x = 12, y = -12), but NOT zero, because `0 % 0` will give a "divide by zero" error.

Fixed expressions:

1. Expression should evaluate to `true` if `x` is an even integer over 100. Current version: `x / 2 == 0 && x > 100`. Fixed version: `x % 2 == 0 && x > 100`.
2. Expression should evaluate to `true` if `x` is a multiple of both 7 and 11. Current version: `x % 7 == 0 || x % 11 == 0`. Fixed version: `x % 7 == 0 && x % 11 == 0`.
3. Expression should evaluate to `true` if either `x` or `y` is a positive integer. Current version: `x >= 0 || y >= 0`. Fixed version: `x > 0 || y > 0` (0 is a non-negative, non-positive number).
4. Expression should evaluate to `true` if both `x` and `y` are outside the range [1, 6]. Current version: `x < 1 || x > 6 && y < 1 || y > 6`. Fixed version: `(x < 1 || x > 6) && (y < 1 || y > 6)`. Because, in the absence of brackets, `&&` takes precedence over `||`.
