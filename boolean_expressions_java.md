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
|`==`|Equal to|`5.2 == 5.8` = `true` while `6.4 == 6.5` = `false`|
|`!=`|Not equal to|`5 != 3.9` = `true` while `5 != 5` = `false`|

# Boolean operators

For this section, we will assume that `a` and `b` are `boolean` values (`true` or `false`)

## `&&` (and) operator

`a && b` is `true` when **both** boolean operands, `a` and `b`, are `true`

| a | b | a && b |
|---|---|------|
|false|false|false|
|false|true|false|
|true|false|false|
|true|true|true|


## `||` (or) operator
`a || b` is `true` when **either** of the boolean operands, `a` **or** `b`, is `true`.

<!-- &#124; is pipe -->

| a | b | a &#124;&#124; b |
|---|---|------|
|false|false|false|
|false|true|true|
|true|false|true|
|true|true|true|

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

## `!` (not) operator

The `!` (not) operator negates the boolean value to which it is applied.

| a | !a |
|---|---|
|false|true|
|true|false|

# Order of operations

Order of operations is,

1. Bracketed boolean sub-expressions
2. Then, Relational operators (left to right)
3. Then, `!`
3. Then, `&&`
4. Then, `||`

# Short-circuit logic

## Short-circuiting `&&`

If the first of the two boolean values is `false`, Processing or java doesn't bother evaluating the second boolean value.

For example:

```processing
int a = 3;
boolean b = a>=10 && a<=20;
```

Here, 

- `a>=10` is,
- `3>=10` which is, 
- `false`

Hence, the expression becomes:

```processing
false && a<=20
```

But, both `false && false` and `false && true` are `false`.
So, no need to evaluate the second sub-expression.

## Short-circuiting `||`

If the first of the two sub-expressions (`a`) is `true`, `a || b` becomes true.

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

# Solutions

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
