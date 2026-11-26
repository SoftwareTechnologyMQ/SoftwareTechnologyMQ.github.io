---
title: Functions
permalink: /comp1010/comp1000-revision/functions
parent: COMP1000 Revision
grand_parent: COMP1010
nav_order: 4
---

- TOC
{:toc}

## Why functions?

A **function** is a named, reusable piece of code that takes some inputs, does some work, and (optionally) gives back a result. Functions let you:

- **avoid repetition**: write the logic once and use it many times,
- **break a big problem into small ones**: each function solves one well-defined sub-problem,
- **test pieces independently**: a function with clear inputs and outputs is easy to check.

In Java, functions are also called **methods**. In COMP1010 you will mostly write `static` methods to begin with.

## Anatomy of a function

```java
public static double average(int a, int b) {
    double result = (a + b) / 2.0;
    return result;
}
```

| Part               | In the example      | Meaning                                                |
|--------------------|---------------------|--------------------------------------------------------|
| return type        | `double`            | the type of the value the function gives back          |
| name               | `average`           | used to call the function                              |
| parameters         | `int a, int b`      | variables that receive the inputs, each with its own type |
| body               | `{ ... }`           | the statements that run when the function is called    |
| `return` statement | `return result;`    | ends the function and sends a value back to the caller |

The first line (`public static double average(int a, int b)`) is called the function's **header** or **signature**.

A function that doesn't give back a value has the return type **`void`**:

```java
public static void printBox(int width) {
    for (int i = 0; i < width; i++) {
        System.out.print("#");
    }
    System.out.println();
}
```

## Calling a function

```java
double avg = average(7, 10);
```

A call is an **expression**. It evaluates to the value the function returns. Here is what happens, step by step:

1. **The arguments are evaluated.** `7` and `10` are already values.
2. **Each argument is copied into its parameter.** `a` gets `7` and `b` gets `10`. These are brand-new variables that exist only while this call runs.
3. **The body runs.** `result` becomes `(7 + 10) / 2.0` → `17 / 2.0` → `8.5`.
4. **`return` sends the value back.** The call `average(7, 10)` evaluates to `8.5`, and the function's variables (`a`, `b`, `result`) disappear.
5. Back in the caller, the assignment finishes: `avg` gets `8.5`.

## Passing values is just assignment

Step 2 above is the key: **passing an argument to a parameter works exactly like assignment.** The argument is the RHS and the parameter is the LHS:

```java
average(7, 10);
// behaves like
int a = 7;
int b = 10;
```

So the [two-step rule]({{ site.baseurl }}/comp1010/comp1000-revision/variables-and-operators#assignment-is-a-two-step-operation) from Variables and Operators applies:

1. the argument expression is evaluated to a value of some type,
2. that value is copied into the parameter, **only if its type is compatible** with the parameter's type.

```java
public static double half(double x) {
    return x / 2;
}

half(7);       // OK: 7 (int) is copied into double x as 7.0, returns 3.5

public static int square(int n) {
    return n * n;
}

square(2.5);   // does NOT compile: 2.5 (double) cannot be copied into int n
```

The same rule applies to `return`: the returned value is copied into the function's return type.

```java
public static double third(int n) {
    return n / 3;       // compiles: int is widened to double...
}                       // ...but third(10) returns 3.0, not 3.33 (integer division!)

public static int twice(double x) {
    return x * 2;       // does NOT compile: double cannot be returned as int
}
```

## Parameters are copies

Because a parameter receives a **copy** of the argument's value, changing the parameter inside the function has no effect on the caller's variable:

```java
public static void addOne(int n) {
    n = n + 1;               // changes the copy only
}

public static void main(String[] args) {
    int x = 5;
    addOne(x);
    System.out.println(x);   // 5
}
```

`x` and `n` are two different variables. `n` started with a copy of `x`'s value, and only `n` changed. To get a result back out of a function, **return** it:

```java
public static int plusOne(int n) {
    return n + 1;
}

x = plusOne(x);   // x is now 6
```

{: .note}
> Arrays behave differently. The value copied into the parameter is a *reference* to the array, so a function *can* change the contents of an array passed to it. See [Arrays]({{ site.baseurl }}/comp1010/comp1000-revision/arrays#arrays-and-functions).

## Scope

A variable exists only inside the block (`{ ... }`) where it is declared. Parameters and variables declared inside a function are **local** to that function. They are created when the function is called and destroyed when it returns.

```java
public static int cube(int n) {
    int result = n * n * n;
    return result;
}

public static void main(String[] args) {
    int c = cube(3);
    System.out.println(result);   // does NOT compile: result only exists inside cube
}
```

Two functions can each have a variable called `result`. They are completely separate variables.

## `return` ends the function immediately

As soon as a `return` statement runs, the function ends. Code after it, in that call, does not run. This is useful for returning early:

```java
public static boolean isPrime(int n) {
    if (n < 2) {
        return false;
    }
    for (int d = 2; d < n; d++) {
        if (n % d == 0) {
            return false;    // found a divisor - stop immediately
        }
    }
    return true;             // only reached if no divisor was found
}
```

{: .warning}
> A non-`void` function must return a value on **every** possible path. If Java can find a way to reach the end of the function without a `return`, it reports `missing return statement`.

## Calling functions from functions

Functions can call other functions. Each call waits for the call inside it to finish:

```java
public static int square(int n) {
    return n * n;
}

public static int sumOfSquares(int a, int b) {
    return square(a) + square(b);
}

int s = sumOfSquares(3, 4);
// sumOfSquares(3, 4)
//   square(3) → 9
//   square(4) → 16
//   returns 9 + 16 → 25
// s = 25
```

## Exercises

{% capture f_p1 %}
For each call, give the value it returns, or explain why it doesn't compile.

```java
public static double area(double w, double h) {
    return w * h;
}

public static int perimeter(int w, int h) {
    return 2 * (w + h);
}
```

1. `area(3, 4)`
2. `perimeter(3, 4)`
3. `area(2.5, 4)`
4. `perimeter(2.5, 4)`
5. `int a = area(3, 4);`
{% endcapture %}
{% capture f_s1 %}
1. `12.0`. The `int` arguments are copied into the `double` parameters.
2. `14`
3. `10.0`
4. Does not compile. `2.5` (double) cannot be copied into `int w`.
5. Does not compile. `area` returns a `double`, which cannot be copied into `int a`.
{% endcapture %}
{% include exercise.html title="Exercise 1: Matching types" problem=f_p1 solution=f_s1 %}

{% capture f_p2 %}
What is the output?

```java
public static int mystery(int a, int b) {
    a = a + b;
    b = a - b;
    return a * b;
}

public static void main(String[] args) {
    int a = 2;
    int b = 3;
    int c = mystery(b, a);
    System.out.println(a + " " + b + " " + c);
}
```
{% endcapture %}
{% capture f_s2 %}
Inside `mystery`, the parameter `a` receives `3` (the caller's `b`) and parameter `b` receives `2` (the caller's `a`). The names don't matter, only the positions.

- `a = 3 + 2` → `5`
- `b = 5 - 2` → `3`
- returns `5 * 3` → `15`

The caller's `a` and `b` are unchanged. Output: `2 3 15`.
{% endcapture %}
{% include exercise.html title="Exercise 2: Copies and positions" problem=f_p2 solution=f_s2 %}

{% capture f_p3 %}
Write a function `countDivisors` that, given a positive integer `n`, returns how many positive integers divide `n` exactly. For example, `countDivisors(12)` returns `6` (1, 2, 3, 4, 6, 12).
{% endcapture %}
{% capture f_s3 %}
```java
public static int countDivisors(int n) {
    int count = 0;
    for (int d = 1; d <= n; d++) {
        if (n % d == 0) {
            count++;
        }
    }
    return count;
}
```
{% endcapture %}
{% include exercise.html title="Exercise 3: Count divisors" problem=f_p3 solution=f_s3 %}

{% capture f_p4 %}
Using `countDivisors` from Exercise 3, write a function `isPrime` that returns `true` if `n` is prime. (A prime has exactly two divisors.)
{% endcapture %}
{% capture f_s4 %}
```java
public static boolean isPrime(int n) {
    return countDivisors(n) == 2;
}
```
{% endcapture %}
{% include exercise.html title="Exercise 4: Reuse" problem=f_p4 solution=f_s4 %}

{% capture f_p5 %}
This function does not compile. Why? Fix it.

```java
public static String sign(int n) {
    if (n > 0) {
        return "positive";
    }
    else if (n < 0) {
        return "negative";
    }
}
```
{% endcapture %}
{% capture f_s5 %}
`missing return statement`: when `n` is `0`, neither branch runs and the function reaches its end without returning a value. Java doesn't analyse the conditions to work out that `0` is the only remaining case. It just sees a path with no `return`.

```java
public static String sign(int n) {
    if (n > 0) {
        return "positive";
    }
    else if (n < 0) {
        return "negative";
    }
    else {
        return "zero";
    }
}
```
{% endcapture %}
{% include exercise.html title="Exercise 5: Missing return" problem=f_p5 solution=f_s5 %}
