---
title: Conditions
permalink: /comp1000/conditions
parent: COMP1000
nav_order: 8
---

- TOC
{:toc}

<!-- Assumed Knowledge -->
{% capture topic_prereq %}
  * [Primitive Operations]({{ site.baseurl }}/comp1000/primitive-operations)
  * [Variables]({{ site.baseurl }}/comp1000/variables)
{% endcapture %}
<!-- Learning Outcomes -->
{% capture topic_outcomes %}
  * Understand what a boolean expression is
  * Understand how boolean expressions can effect the flow of control in a program
  * Write code that requires `if-then-else` statements
  * Understand simple logical operations.
{% endcapture %}

{% include prereq_outcomes.html prereq=topic_prereq outcomes=topic_outcomes %}

{: .keynote}
Conditions allow different lines of code to run in different frames of the animation.

{: .readings}
* Chapter 5 of [Learning Processing](http://learningprocessing.com) by Danel Shiffman.

{% include youtube.html id="wsI6N9hfW7E" %}

{% include youtube.html id="mVq7Ms01RjA" %}

{% include youtube.html id="9857701OsDE" %}

{% include youtube.html id="_NJqfZUQ3i4" %}

{% include youtube.html id="YIKRXl3wH8Y" %}

## Statement or Expression

A conditional is a statement.  It _does_ one of two things.  However, the boolean that determines which branch is an expression, _it evalates to true or false_.

<!-- Exercise: One-Way Animated Blue Circle -->
{% capture my_problem %}
Write a program that draws a blue cirle that moves from the top to the bottom of the sketch and when reaching the bottom of the screen, will change direction and start moving up the screen.
{% endcapture %}

{% capture my_solution %}
The problem description does not directly relate to conditions, so we need to "re-interpret" it to put it into "code-speak".  Another way to consider the problem statement (as a Processing programmer) is "write a program where a blue circle is drawn on the screen and every time it is drawn it moves a little.  IF it has hit the bottom previously, it should move up, otherwiser it should move down".  This leads us more directly to some code.  We need a condition so that we can choose which code path will run on any individual frame (`if (hitBottom)`) and to make it work we need a boolean _recording_ if we have hit the bottom before.  Finally, we need an condition that checks everytime we draw the sketch if we just hit the bottom.

```java
int yPos;
boolean hitBottom;

void setup(){
  yPos = 0;
  hitBottom = false;
}

void draw(){
  background(255);

  if (yPos == height){
    hitBottom = true;
  }

  noStroke();
  fill(92, 136, 218);
  circle(width/2, yPos, 20);
  if (hitBottom){
    yPos--;
  } else {
    yPos++;
  }

}
```
{% endcapture %}

{% include exercise.html
  title="Exercise: One-Way Animated Blue Circle"
  problem=my_problem
  solution=my_solution
%}

We will now go over the material presented in the above videos, but we will be more _precise_ about what is going on to deepen your understanding.

Conditions are based on *boolean expressions* and the program takes a specific course based on whether these expressions evaluate to `true` or `false`.

## An `if` condition
An `if` condition executes the conditional code only if the `expression` is evaluated to `true` and then the rest of the code. If the `expression` is evaluated to `false`, it executes the `rest of the code` irrespectively afterwards.

```java
if(boolean expression) {
	conditional code
}
rest of the code
```

```mermaid
flowchart TD
  A@{ shape: hex, label: "Is boolean expression true or false?"}
  B(conditional code)
  C(rest of code)
  A -- true --> B
  A -- false --> C
  B --> C
```

Example:

```java
int x = 10;
int result = 5;
if(x > 8) {
	result = result + 1;
}
print(result);
```

```mermaid
flowchart TD
    A[x = 10; result = 5]
    B@{ shape: diamond, label: "x > 8"}
    D@{ shape: stadium, label: "println(result)"}
    A --> B
    B -- true --> C[result = result + 1]
    B -- false --> D
    C --> D
```


The above code executes the conditional code, increasing `result` by 1 and displaying the value 6.

{% include youtube.html id="1oVo6mYYeTs" %}

## An `if-else` condition
An `if-else` condition executes the `if` block if the `boolean expression` is evaluated to `true` and the `else` block if the `boolean expression` is evaluated to `false`. The `rest of the code` is executes afterwards irrespectively.

```java
if(boolean expression) {
	if-block statements
}
else {
	else-block statements
}
rest of the code
```

```mermaid
flowchart TD
    A[boolean expression]
    A -->|if| B(if-block statements)
    A -->|else| C(else-block statements)
    B --> D(rest of code)
    C --> D
```

Example:

```java
int x = 13;
boolean isEven;
if(x % 2 == 0) {
  isEven = true;
}
else {
  isEven = false;
}
println(isEven);
```

```mermaid
flowchart TD
    Y(x = 13)
    Y --- Z(boolean isEven)
    Z --- A@{ shape: hex, label: "Is x % 2 == 0 ?"}
    A -->|true| B(isEven = true)
    A --x|false| C(isEven = false)
    B --- D("println(isEven)")
    C ~~~ D
```


The else-block is executed in the above code, `isEven` becomes `false`, and is displayed on the console.

{% include youtube.html id="jgmZ2T8mWl0" %}

## Statements, not Expressions

An `if` is a _statement_ not an _expression_. Therefore, you are free to put any valid conditional code inside the scope of another condition.

{% include youtube.html id="jgmZ2T8mWl0" %}


<!--That means it has no intrinsic value, it exists only for what it can _do_.  For example, variables are _expressions_ because if  you put one in your code, it is the same as putting some value in that spot (the value stored in the variable).  However, an `if` may effect variables, or draw things on the screen, but the statement itself has no value, i.e. `if (1 < 2) {line(1,1,,1,);}` is not the same as putting some value in that spot.-->

<!-- Exercise -->
{% capture my_problem %}
Draw a flowchart for the following code and determine the values of `a, b, c` after the code executes.

```java
int a = (int)random(5), b = (int)random(5), c = (int)random(5);
if(a < b) {
	if(c == a) {
		c = c + 1;
	}
}
else {
	if(b < c) {
		b = c - a;
	}
	else {
		a = 0;
	}
}
```
{% endcapture %}

{% capture my_solution %}
```mermaid
flowchart TD
A("int a = 5, b = 2, c = 10")
A ==> B@{ shape: hex, label: "a < b?"}
B -->|true| C@{ shape: hex, label: "c == a?"}
C -->|true| D(c = c + 1)
C -->|false| H@{ shape: stadium, label: "end of code"}
B ==>|false| E@{ shape: hex, label: "b < c?"}
E ==>|true| F(b = c - a)
E -->|false| G(a = 0)
F ==> I("a = 5, b = 5, c = 10")
```
{% endcapture %}

{% include exercise.html
  title="Exercise"
  problem=my_problem
  solution=my_solution
%}

<!-- Exercise -->
{% capture my_problem %}
What is wrong with the following code? Draw a flowchart to illustrate the problem. Write the corrected code.

```java
int a = (int)random(6);
int b = (int)random(6);
int max;
if(a > b) {
	max = a;
}
if(b >= a) {
	max = b;
}
println(max);
```
{% endcapture %}

{% capture my_solution %}
Both assignment operators are conditional and it is possible, in terms of control flow, that neither of the assignment operators are executed (although mathematically it's not possible in this case). You will get a <strong>Variable max may not have been initialized</strong> error. Diagram of the buggy code:

```mermaid
flowchart TD
A("int a = (int)random(6)<br> int b = (int)random(6)<br> int max")
A --> B@{ shape: hex, label: "a > b?"}
B -->|true| C("max = a")
C --> D@{ shape: hex, label: "b > = a?"}
B -->|"false"| D
D -->|true| E("max = b")
E --> F("println(max)")
D -->|false| F
```

Corrected code:

```
int a = (int)random(6);
int b = (int)random(6);
int max;
if(a > b) {
	max = a;
}
else {
	max = b;
}
println(max);
```

```mermaid
flowchart TD
A("int a = (int)random(6)<br> int b = (int)random(6)<br> int max")
A --> B@{ shape: hex, label: "a > b?"}
B -->|true| C("max = a")
C --> D("println(max)")
B -->|false| E("max = b")
E --> D
```
{% endcapture %}

{% include exercise.html
  title="Exercise"
  problem=my_problem
  solution=my_solution
%}


<!-- Exercise: Two-Way Animated Blue Circle -->
{% capture my_problem %}
Adjust [your animated blue circle](#exercise-one-way-animated-blue-circle) so it also bounces off the top of the screen, thus always going up and down forever, never disapearing.  Note that there are two approaches to solving this.
{% endcapture %}

{% capture my_solution %}
We can simply use the `hitBottom` boolean in a smarter way.  What if we think of is as "moving up" instead?  Then it will be `false` at the start, and change to `true` when we hit the bottom, then `false` again when we hit the top.

```
int yPos;
boolean movingUp;

void setup(){
  yPos = 0;
  movingUp = false;
}

void draw(){
  background(255);

  if (yPos == height){
    movingUp = true;
  }
  if (yPos == 0){
    movingUp = false;
  }
  noStroke();
  fill(92, 136, 218);
  circle(width/2, yPos, 20);
  if (movingUp){
    yPos--;
  } else {
    yPos++;
  }
}
```

Notice that we _can't_ use an `else` on the `yPos` check.  Many new programmers will try this.  Why won't that work?
{% endcapture %}

{% capture my_solution_2 %}
Solution 1 is the simplest, but you will see many people suggest the following solution.  It works really well if _any more complex animation_ is required, so it is a good idea to understand it now.

In this solution we rephrase the task into the following "draw a blue circle that is moving each frame of the animation.  At first, it should move with a speed of +1 (i.e. down the screen) but when the circle hits the bottom of the screen its speed should reverse to -1 (i.e. up the screen).  Again it will reverse when it hit the top of the screen, etc."

Instead of keeping a boolean telling us what phase of the animation we are in, we are keeping a number telling us what speed the circle is moving, using the trick that a negative speed means we are moving up the screen instead of down.

```
int yPos;
int speed;

void setup(){
  yPos = 0;
  speed = 1;
}

void draw(){
  background(255);

  if (yPos == height){
    speed = -1;
  }
  if (yPos == 0){
    speed = 1;
  }
  noStroke();
  fill(92, 136, 218);
  circle(width/2, yPos, 20);
  yPos = yPos + speed;
}
```

Interestingly, this has saved us from one conditional!  It is perhaps a little harder to see at first, but the code is shorter.  The "variability" of the variable is doing the work of the condition.  Note also how we now have many more options, we can speed up the animation quite easily which we could not in solution 1.
{% endcapture %}

{% include exercise.html
  title="Exercise: Two-Way Animated Blue Circle"
  problem=my_problem
  solution=my_solution
  solution2=my_solution_2
%}

## Tracing "flow" (or control flow)

One of the pillars of programming is for the programmer to be able to trace how the program executes. Which is the next line to execute? With conditions, and later loops and functions, the program can take different paths. Hence, these three (conditions, loops and functions) are called *control flow structures*.

As an example, consider the following code:

```java
int a = (int)random(5), b = (int)random(5), c = (int)random(5);
if(a < b) {
  if(c == a) {
    c = c + 1;
  }
}
else {
  if(b < c) {
    b = c - a;
  }
  else {
    a = 0;
  }
}
```

There are four possibilities:

### Possibility 1

Lines 1 --> 2 --> 3--> 4

Effective program:

```java
int a = (int)random(5), b = (int)random(5), c = (int)random(5);
c = c + 1;
```

### Possibility 2

Lines 1 --> 2 --> 3

Effective program:

```java
int a = (int)random(5), b = (int)random(5), c = (int)random(5);
```

### Possibility 3

Lines 1 --> 2 --> 8 --> 9

Effective program:

```java
int a = (int)random(5), b = (int)random(5), c = (int)random(5);
b = c - a;
```

### Possibility 4

Lines 1 --> 2 --> 8 --> 12

Effective program:

```java
int a = (int)random(5), b = (int)random(5), c = (int)random(5);
a = 0;
```

A program that might look long and daunting actually reduces to a much-smaller final code if you can trace the code manually. Flowcharts are great, but manually being able to ***determine the next statement that will execute*** is just ... 🤌!

## Coding in the real world

In real life, we need to convert written/spoken descriptions of a case into precise code and in this section, we'll take a look as such scenarios.

<!-- Exercise -->
{% capture my_problem %}
A website offers discounts based on item categories and quantities. There are four categories - A, B, C, and D. For all categories except D, the following rules exist,

- Less than 2 items: no discount
- Between 2 and 5 items: 15% discount
- Between 6 and 10 items: 25% discount
- More than 10 items: 30% discount


For category D, there is a 1% discount for every item purchased, up to a maximum of 50 items (and hence a maximum of 50% discount).

Write a piece of code that outputs the percentage discount for a given category (stored in `char cateogry` that can be either 'A', 'B', 'C', or 'D') and quantity (stored in `int quantity`).

{% endcapture %}

{% capture my_solution %}
```java
int discountPercent = 0;

if(category == 'D') {
  if(quantity > 50) {
    discountPercent = 50;
  }
  else {
    discountPercent = quantity;
  }
}
else {
  if(quantity >= 2 && quantity <= 5) {
    discountPercent = 15;
  }
  if(quantity >= 6 && quantity <= 10) {
    discountPercent = 25;
  }
  if(quantity > 10) {
    discountPercent = 30;
  }
}
```
{% endcapture %}

{% include exercise.html
  title="Exercise"
  problem=my_problem
  solution=my_solution
%}

<!-- Exercise -->
{% capture my_problem %}
The shopping mall charges for parking based on the following rules:

- under 3 hours: free
- 3 hours to 3 hours 29 minutes: $4
- 3 hours 30 minutes to 3 hours 59 minutes: $7
- 4 hours to 4 hours 29 minutes: $11
- 4 hours 30 minutes to 4 hours 59 minutes: $16
- 5 hours to 5 hours 29 minutes: $22
- 5 hours 30 minutes to 5 hours 59 minutes: $30
- 6 hours or over: $40

Given the number of hours and minutes in two variables, write a piece of code that stores the parking cost in a variable `parkingFee`.
{% endcapture %}

{% capture my_solution %}
We have two solutions, this one only uses simple boolean expressions, but that creates a complex, nested set of `if` statements.

```java
int parkingFee = 0;

if (minutes >= 180) {
  if (minutes < 210) {
    parkingFee = 4;
  }
  else {
    if (minutes < 240) {
      parkingFee = 7;
    }
    else {
      if (minutes < 270) {
        parkingFee = 11;
      }
      else {
        if (minutes < 300) {
          parkingFee = 16;
        }
        else {
          if (minutes < 330) {
            parkingFee = 22;
          }
          else {
            if (minutes < 360) {
              parkingFee = 30;
            }
            else {
              parkingFee = 40;
            }
          }
        }
      }
    }
  }
}
```
{% endcapture %}

{% capture my_solution_2 %}
This second solution needs more complex boolean expressions, but that makes things simpler overall.

```java
int parkingFee = 0;

if (minutes >= 180 && minutes < 210) {
  parkingFee = 4;
}

if (minutes >= 210 && minutes < 240) {
  parkingFee = 7;
}

if (minutes >= 240 && minutes < 270) {
  parkingFee = 11;
}

if (minutes >= 270 && minutes < 300) {
  parkingFee = 16;
}

if (minutes >= 300 && minutes < 330) {
  parkingFee = 22;
}

if (minutes >= 330 && minutes < 360) {
  parkingFee = 30;
}

if (minutes >= 360) {
  parkingFee = 40;
}

```
{% endcapture %}

{% include exercise.html
  title="Exercise"
  problem=my_problem
  solution=my_solution
  solution2=my_solution_2
%}

<!-- Exercise -->
{% capture my_problem %}
Write a piece of code to address the same problem as in scenario 3, but an additional rule. Weekend (Sat, Sun) parking incurs a flat rate of $4 per 30 minutes. That is,

- 0 to 29 minutes: $4
- 30 to 59 minutes: $8
- 60 to 89 minutes: $12
- and so on...

An additional variable `dayOfWeek` is available and is 0 for Monday, 1 for Tuesday and so on.
{% endcapture %}

{% capture my_solution %}
```java
int parkingFee = 0;

if (dayOfWeek < 5) { //NOT the weekend
  if (minutes >= 180 && minutes < 210) {
    parkingFee = 4;
  }

  if (minutes >= 210 && minutes < 240) {
    parkingFee = 7;
  }

  if (minutes >= 240 && minutes < 270) {
    parkingFee = 11;
  }

  if (minutes >= 270 && minutes < 300) {
    parkingFee = 16;
  }

  if (minutes >= 300 && minutes < 330) {
    parkingFee = 22;
  }

  if (minutes >= 330 && minutes < 360) {
    parkingFee = 30;
  }

  if (minutes >= 360) {
    parkingFee = 40;
  }
  println("Weekday parking fee for "+minutes/60+" hours and "+minutes%60+" minutes: $"+parkingFee);
} else { //weekend
  parkingFee = 4 + 4 * (minutes/30);
  println("Weekend parking fee for "+minutes/60+" hours and "+minutes%60+" minutes: $"+parkingFee);
}
```
{% endcapture %}

{% include exercise.html
  title="Exercise"
  problem=my_problem
  solution=my_solution
%}

## Furthering Your Understanding

{% include youtube.html id="wUPc__xuCc0" %}
