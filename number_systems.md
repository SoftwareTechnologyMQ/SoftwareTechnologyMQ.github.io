---
layout: page
title: COMP6010 Week 2
within: programming
katex: True
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge:</summary>

  * [Week 1](./comp6010week1.html)  

</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes:</summary>

  * Represent integers (including negative integers) in different bases.
  * Convert from one base to other.
  
</details>

<!--# Table of contents

- [1. Representing Information](#1-representing-information)
- [2. Representing numbers in different bases](#2-representing-numbers-in-different-bases)
  - [2.1 Positional number systems](#21-positional-number-systems)
  - [2.2 Converting to base *b*](#22-converting-to-base-b)
- [3. Data Types](#3-data-types)
  - [3.1 Integers](#31-integers)
    - [3.1.1 Unsigned Integers](#311-unsigned-integers)
    - [3.1.2 Signed Integers](#312-signed-integers)
    - [3.1.3 One's Complement](#313-ones-complement)
    - [3.1.4 Two's Complement](#314-twos-complement)
  - [3.2 Floating Point Numbers (ADVANCED)](#32-floating-point-numbers-advanced)
    - [3.2.1 To IEEE format](#321-to-ieee-format)
    - [Example 1](#example-1)
    - [Example 2](#example-2)
    - [3.2.2 From IEEE format](#322-from-ieee-format)-->


# 1. Representing Information

How do we represent data in a computer? At a fundamental level, a computer is an electronic machine that works by controlling the flow of electrons

It is easy to recognize two scenarios:

1. presence of current flowing through - call this state "1"
2. absence of current flowing through - call this state "0"

# 2. Representing numbers in different bases

An integer in base $$b$$ consists of values from 0 to $$b-1$$.

Hexadecimal is base-16, so it has values rom 0 to 15. However, beyond 9, the following symbols are used:

<table>
<tr><th>Value</th><th>Symbol</th></tr>
<tr><td>10</td><td>a</td></tr>
<tr><td>11</td><td>b</td></tr>
<tr><td>12</td><td>c</td></tr>
<tr><td>13</td><td>d</td></tr>
<tr><td>14</td><td>e</td></tr>
<tr><td>15</td><td>f</td></tr>
</table>

A number $$n$$ in base $$b$$ is represented as $$n_b$$. That is the base is in the subscript. Absence of subscript means it is a decimal value.

For example, 

$$1101_2$$ is a base-2 or binary value.
$$1304_8$$ is a base-8 or octal value.
$$E2F_{16}$$ is a base-16 or hexadecimal value.
$$1603_6$$ is is an invalid number since base-6 can only have digits between 0 and (6-1 = 5).

Hexadecimal numbers are often prefixed with `0x`. For example `0x17c9` represents the hexadecimal number `17c9`.
Similarly, binary numbers are often prefixed with `0b`. For example `0b1101` represents the binary number `1101`.

## 2.1 Positional number systems

Consider these positions in a number system:

<table>
<tr>
<td>...</td>
<td>n<sup>3</sup></td>
<td>n<sup>2</sup></td>
<td>n<sup>1</sup></td>
<td>n<sup>0</sup></td>
</tr>
<tr>
<td>...</td>
<td>d<sub>3</sub></td>
<td>d<sub>2</sub></td>
<td>d<sub>1</sub></td>
<td>d<sub>0</sub></td>
</tr>
</table>

{% raw %}
$$
d_3 \times n^3 + d_2 \times n^2 + d_1 \times n^1 + d_0 \times n^0 
$$
{% endraw %}

Consider the number 350 in base 10 (radix 10). That is, n is 10, and thus: 

{% raw %}
$$
3 \times n^2 + 5 \times n^1 + 0 \times n^0 
$$
{% endraw %}

{% raw %}
$$
3 \times 100 + 5 \times 10 + 0 \times 1 
$$
{% endraw %}

Consider the number 10110 in base 2 (radix 2). That is, n is 2, and thus: 

{% raw %}
$$
1 \times n^4 + 0 \times n^3 + 1 \times n^2 + 1 \times n^1 + 0 \times n^0 
$$
{% endraw %}

{% raw %}
$$
1 \times 16 + 0 \times 8 + 1 \times 4 + 1 \times 2 + 0 \times 1 
$$
{% endraw %}

or 22 in base 10.

## 2.2 Converting between number systems

### 2.2.1 Converting from decimal to base *b*

1. Start with result = 0
2. If number is zero, go to step 5.
3. Divide the number by $$b$$ and put the remainder (a value between 0 and $$b-1$$ to the left of result. 
4. Go to step 2. 
5. Binary number is in the result.

In the operation $$\frac{a}{b}$$, if $$a \times d + r = b$$, we call $$d$$ the *quotient* and $$r$$ the *remainder*. Here $$a$$ is being divided by $$b$$ and $$a$$ is the *dividend* (numerator) while $$b$$ is the *divisor* (denomenator).

#### Examples

46 to binary:

| Divided | Divisor | Quotient | Remainder | Result |
|---|---|---|---|---|
| 46	| 2 | 23 | 0 | empty -> 0 |
| 23	| 2 | 11 | 1 | 0 -> 10 |
| 11	| 2 | 5 | 1 | 10 -> 110 |
| 5	| 2 | 2 | 1 | 110 -> 1110 |
| 2	| 2 | 1 | 0 | 1110 -> 01110 |
| 1	| 2 | 0 | 1 | 01110 -> 101110 |
| 0	| STOP |  |  |

73 to binary:

| Divided | Divisor | Quotient | Remainder | Result |
|---|---|---|---|---|
| 73	| 2 | 23 | 1 | empty -> 1 |
| 36	| 2 | 11 | 0 | 1 -> 01 |
| 18	| 2 | 5 | 0 | 01 -> 001 |
| 9	| 2 | 2 | 1 | 001 -> 1001 |
| 4	| 2 | 1 | 0 | 1001 -> 01001 |
| 2	| 2 | 0 | 0 | 01001 -> 001001 |
| 1	| 2 | 0 | 1 | 001001 -> 1001001 |
| 0	| STOP |  |  |

46 to base-3:

| Divided | Divisor | Quotient | Remainder | Result |
|---|---|---|---|---|
| 46	| 3 | 15 | 1 | empty -> 1 |
| 15	| 3 | 5 | 0 | 1 -> 01 |
| 5	| 3 | 1 | 2 | 01 -> 201 |
| 1	| 3 | 0 | 1 | 201 -> 1201 |
| 0	| STOP |  |  |

73 to base-16 (hexadecimal):

| Divided | Divisor | Quotient | Remainder | Result |
|---|---|---|---|---|
| 73	| 16 | 4 | 9 | empty -> 9 |
| 4	| 16 | 0 | 4 | 9 -> 49 |
| 0	| STOP |  |  |

2779 to base-16 (hexadecimal):

| Divided | Divisor | Quotient | Remainder | Result |
|---|---|---|---|---|
| 2779	| 16 | 173 | 11 (B) | empty -> B |
| 173	| 16 | 10 | 13 (D) | B -> DB |
| 10	| 16 | 0 | 10 (A) | DB -> ADB |


### 2.2.2 Converting from base *b* to decimal

1. $$weight = 1, result = 0$$
2. Start with right-most digit (least significant digit)
2. Multiply digit by $$weight$$ and add to $$result$$
3. Multiply $$weight$$ by $$b$$
4. If digit exists to the left of current digit, go to step 2
5. Result holds the decimal value 

Examples

$$1101_2$$ to decimal:

| Current Digit | Weight | Result |
|---|---|---|
| 1 |	 1	| 0 -> 0 + 1\*1 = 1 |
| 0 | 2	| 1 -> 1 + 0\*2 = 1 |
| 1 | 4 | 1 -> 1 + 1\*4 = 5 |
| 1 | 8 | 5 -> 5 + 1\*8 = 13 (result) |
 

$$ADB_{16}$$ to decimal:

| Current Digit | Weight | Result |
|---|---|---|
| B |	 1	| 0 -> 0 + B\*1 = 0 + 11\*1 = 11 (remember, b is 11) |
| D | 16	| 11 -> 11 + 13\*16 = 219 |
| A | 256 | 219 -> 219 + 10\*256 = 2779 (result) |

$$1201_3$$ to decimal:

| Current Digit | Weight | Result |
|---|---|---|
| 1 |	 1	| 0 -> 0 + 1\*1 = 1 |
| 0 | 3	| 1 -> 1 + 0\*3 = 1 |
| 2 | 9 | 1 -> 1 + 2\*9 = 19 |
| 1 | 27 | 19 -> 19 + 1\*27 = 46 (result) |

### 2.2.3 Converting between arbitrary bases

Say, we need to convert a number $$n$$ from base $$b_1$$ to base $$b_2$$.

1. Convert the number from base $$b_1$$ to decimal.
2. Convert the decimal version from decimal to base $$b_2$$.

Example(s):

Convert $$111001_2$$ to base-3.

1. First convert to decimal: $$111001_2$$ = $$57_{10}$$
2. Convert from decimal to base-3: $$2010_3$$

Convert $$4307_9$$ to base-16.

1. First convert to decimal: $$4307_9$$ = $$3166_{10}$$
2. Convert from decimal to base-3: $$C5E_{16}$$


# 3. Data Types

## 3.1 Integers

There are two categories of integers (whole numbers):

* Unsigned integers
 * Typically, each bit represents decreasing (from left to right) magnitudes of powers of 2
* Signed integers
 * Signed magnitude
 * 1's complement
 * 2's complement

Unsigned integers are all positive, and thus you can use all bits to represent positive numbers.

Signed integers use a bit to represent whether the integer is positive or negative.

### 3.1.1 Unsigned Integers

Let's see how many unsigned (non-negative) integers can we store using 4 bits.

<table>
<tr><th>Number</th><th>Bits</th></tr>
<tr><td>0</td><td>0000</td></tr>
<tr><td>1</td><td>0001</td></tr>
<tr><td>2</td><td>0010</td></tr>
<tr><td>3</td><td>0011</td></tr>
<tr><td>4</td><td>0100</td></tr>
<tr><td>5</td><td>0101</td></tr>
<tr><td>6</td><td>0110</td></tr>
<tr><td>7</td><td>0111</td></tr>
<tr><td>8</td><td>1000</td></tr>
<tr><td>9</td><td>1001</td></tr>
<tr><td>10</td><td>1010</td></tr>
<tr><td>11</td><td>1011</td></tr>
<tr><td>12</td><td>1100</td></tr>
<tr><td>13</td><td>1101</td></tr>
<tr><td>14</td><td>1110</td></tr>
<tr><td>15</td><td>1111</td></tr>
</table>

- **What is the largest unsigned integer using 16 bits?**
- **What is the largest unsigned integer using 32 bits?**

### 3.1.2 Signed Integers

But how can we represent negative numbers?

#### 3.1.2.1 Signed Magnitude

The simplest pattern (at least for humans) might be the "signed magnitude"... just use the left-most bit to mean negative.

<table>
<tr><th>Number</th><th>Bits</th></tr>
<tr><td>-7</td><td>1111</td></tr>
<tr><td>-6</td><td>1110</td></tr>
<tr><td>-5</td><td>1101</td></tr>
<tr><td>-4</td><td>1100</td></tr>
<tr><td>-3</td><td>1011</td></tr>
<tr><td>-2</td><td>1010</td></tr>
<tr><td>-1</td><td>1001</td></tr>
<tr><td>-0</td><td>1000</td></tr>
<tr><td>0</td><td>0000</td></tr>
<tr><td>1</td><td>0001</td></tr>
<tr><td>2</td><td>0010</td></tr>
<tr><td>3</td><td>0011</td></tr>
<tr><td>4</td><td>0100</td></tr>
<tr><td>5</td><td>0101</td></tr>
<tr><td>6</td><td>0110</td></tr>
<tr><td>7</td><td>0111</td></tr>
</table>

If we add 1 and -1, we should get zero. Using signed magnitude, it's 0001 + 1001 = 1010, which is -2. 
So, no good :(

#### 3.1.2.2 One's Complement

We can keep the left-most bit for sign and flip the others so `n` + `-n` is always `0000000` (Ignoring the sign bit).

<table>
<tr><th>Number</th><th>Bits</th></tr>
<tr><td>-7</td><td>1000</td></tr>
<tr><td>-6</td><td>1001</td></tr>
<tr><td>-5</td><td>1010</td></tr>
<tr><td>-4</td><td>1011</td></tr>
<tr><td>-3</td><td>1100</td></tr>
<tr><td>-2</td><td>1101</td></tr>
<tr><td>-1</td><td>1110</td></tr>
<tr><td>-0</td><td>1111</td></tr>
<tr><td> 0</td><td>0000</td></tr>
<tr><td> 1</td><td>0001</td></tr>
<tr><td> 2</td><td>0010</td></tr>
<tr><td> 3</td><td>0011</td></tr>
<tr><td> 4</td><td>0100</td></tr>
<tr><td> 5</td><td>0101</td></tr>
<tr><td> 6</td><td>0110</td></tr>
<tr><td> 7</td><td>0111</td></tr>
</table>

But this leads to two representations of 0 (positive zero and negative zero) - no good!

#### 3.1.2.3 Two's Complement

An $$n$$-bit two's complement represents integers in the range $$[-2^{(n-1)}, \hskip 2mm 2^{(n-1)} - 1$$] (That represents all integers from $$-2^{(n-1)}$$ to $$2^{(n-1)} - 1$$(inclusive on both sides).

A negative number $$k$$ is represented by,

1. Add 1 to $$k$$. Call this $$m$$. Note that $$m <= 0$$.
2. Negate $$m$$. Call this $$p$$. Note that $$p >= 0$$.
3. Flip the bits of $$p$$. 

This can be represented as 

{% raw %} 
$$
bin(k | k < 0) = flip(toBinary(negate(inc(k))))
$$ 
{% endraw %}

The order of operations should be:

**_I_**ncrement > **_N_**egate > **_To_** binary > **_F_**lip

You can remember it as "INToF"

In a 4-bit system, -6 would be represented by,

1. adding 1 to get -5, 
2. negating -5 to get 5,
3. flipping binary representation of 5 (`0101`) to get `1010`.


<table>
<tr><th>Number</th><th>Bits</th></tr>
<tr><td>-8</td><td>1000</td></tr>
<tr><td>-7</td><td>1001</td></tr>
<tr><td>-6</td><td>1010</td></tr>
<tr><td>-5</td><td>1011</td></tr>
<tr><td>-4</td><td>1100</td></tr>
<tr><td>-3</td><td>1101</td></tr>
<tr><td>-2</td><td>1110</td></tr>
<tr><td>-1</td><td>1111</td></tr>
<tr><td> 0</td><td>0000</td></tr>
<tr><td> 1</td><td>0001</td></tr>
<tr><td> 2</td><td>0010</td></tr>
<tr><td> 3</td><td>0011</td></tr>
<tr><td> 4</td><td>0100</td></tr>
<tr><td> 5</td><td>0101</td></tr>
<tr><td> 6</td><td>0110</td></tr>
<tr><td> 7</td><td>0111</td></tr>
</table>

Advantages:

* no negative zero 👍
* -1 + 1 = 1111 + 0001 = 0000 (overflow discarded). 👍

**What is the range of numbers represented in 16 bits using 2's complement?**

#### Examples

```
-46 in 8-bit binary
I: Increment: -46+1 = -45
N: Negate: -(-45) = 45
To: To binary = 00101101
F: Flip = 11010010
```

```
-793 in 16-bit binary
I: Increment: -793+1 = -792
N: Negate: -(-792) = 792
To: To binary = 0000001100011000
F: Flip = 1111110011100111
```

## 3.2 Floating Point Numbers (ADVANCED)

Could be used just to indicate where a decimal place

Used to represent really big numbers and really small numbers.

Consider that we have 32 bits to use. The *IEEE Standard for Floating Point Arithmetic* defined the following representation:

* 1 bit for the sign (0 = positive, 1 = negative)
* 8 bits for exponent (offset by 127)
* 23 bits for precision (leading 1 assumed)

### 3.2.1 To IEEE format

### Example 1 

Convert to IEEE floating-point representation:

{% raw %}
$$ 
-6 \dfrac{5}{8}
$$
{% endraw %}

#### 3.2.1.1 Convert to binary representation

<table>
<tr>
<td>n<sup>3</sup></td>
<td>n<sup>2</sup></td>
<td>n<sup>1</sup></td>
<td>n<sup>0</sup></td>
<th colspan="2">Decimal</th>
<td>n<sup>-1</sup></td>
<td>n<sup>-2</sup></td>
<td>n<sup>-3</sup></td>
<td>n<sup>-4</sup></td>
</tr>
<tr>
<td>d<sub>3</sub></td>
<td>d<sub>2</sub></td>
<td>d<sub>1</sub></td>
<td>d<sub>0</sub></td>
<td colspan="2">.</td>
<td>d<sub>-1</sub></td>
<td>d<sub>-2</sub></td>
<td>d<sub>-3</sub></td>
<td>d<sub>-4</sub></td>
</tr>
</table>


Just as before we see how many column values will go into a number, we continue for $$n^{-1}$$...

{% raw %}
$$
0 \times n^3 + 1 \times n^2 + 1 \times n^1 + 0 \times n^0 + 1 \times n^{-1} + 0 \times n^{-2} + 1 \times n^{-3}
$$
{% endraw %}

{% raw %}
$$
0 \times 8 + 1 \times 4 + 1 \times 2 + 0 \times 1 + 1 \times \dfrac{1}{2} + 0 \times \dfrac{1}{4} + 1 \times \dfrac{1}{8}
$$
{% endraw %}

or:

-0110.101

#### 3.2.1.2 Normalize

Move the decimal place to left or right to get a single 1 to the left of the decimal place. Count how many places and in which direction:

-0110.101

becomes:

-01.10101

with 2 moves (exponent).

#### 3.2.1.3 Add 127 to exponent, convert to binary

2 + 127 = 129

which is:

100000001

in binary.

#### 3.2.1.4 Combine, leaving off leading 1 of precision

1 100000001 10101

and pad to a total of 32 bits:

1 100000001 10101000000000000000000

### Example 2

$$ 
-6 \dfrac{5}{16}
$$

#### 3.2.1.1 Convert to binary representation

<table>
<tr>
<td>n<sup>3</sup></td>
<td>n<sup>2</sup></td>
<td>n<sup>1</sup></td>
<td>n<sup>0</sup></td>
<th colspan="2">Decimal</th>
<td>n<sup>-1</sup></td>
<td>n<sup>-2</sup></td>
<td>n<sup>-3</sup></td>
<td>n<sup>-4</sup></td>
<td>n<sup>-5</sup></td>
</tr>
<tr>
<td>d<sub>3</sub></td>
<td>d<sub>2</sub></td>
<td>d<sub>1</sub></td>
<td>d<sub>0</sub></td>
<td colspan="2">.</td>
<td>d<sub>-1</sub></td>
<td>d<sub>-2</sub></td>
<td>d<sub>-3</sub></td>
<td>d<sub>-4</sub></td>
<td>d<sub>-5</sub></td>
</tr>
</table>


Just as before we see how many column values will go into a number, we continue for $$n^{-1}$$...

{% raw %}
$$
0 \times n^3 + 1 \times n^2 + 1 \times n^1 + 0 \times n^0 + 0 \times n^{-1} + 1 \times n^{-2} + 0 \times n^{-3} + 1 \times n^{-4}
$$
{% endraw %}

{% raw %}
$$
=0 \times 8 + 1 \times 4 + 1 \times 2 + 0 \times 1 + 0 \times \dfrac{1}{2} + 1 \times \dfrac{1}{4} + 0 \times \dfrac{1}{8} + 1 \times \dfrac{1}{16}
$$
{% endraw %}
or:

-0110.0101

Rest remains the same.

### 3.2.2 From IEEE format

Consider:

00111101100000000000000000000000

Do the reverse:

#### 3.2.2.1 First digit is sign

Break into parts:

0 01111011 00000000000000000000000

It is positive!

#### 3.2.2.1 Next 8 bits is exponent, minus 127

Convert next 8 unsigned bits into decimal, and subtract 127:

01111011 is 123

123 - 127 = -4

#### 3.2.2.1 Get precision

Put a one in front of the last 23 bits:

1.00000000000000000000000

and move the decimal spot by the exponent. In this case, 4 places to the left:

0.000100000000000000000000000

Convert to decimal:

{% raw %}
$$
0 * \dfrac{1}{2} + 0 * \dfrac{1}{4} + 0 * \dfrac{1}{8} + 1 * \dfrac{1}{16} ...
$$
{% endraw %}

#### 3.2.2.1 All together

{% raw %}
$$
+ \dfrac{1}{16}
$$
{% endraw %}

<!--bibtex

@misc{colorado,
  title = {Chapter 2},
  howpublished = {https://www.cs.colostate.edu/~cs270/.Fall13/Notes/Lecture1(C1).pdf},
  note = {Accessed: 2015-09-09}
}

-->
