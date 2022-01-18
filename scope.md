---
layout: page
title: Scope
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge</summary>

  * [Variables](./variables)
  * [Conditions](./conditions)
  * [Loops](./loops)
  * [Functions](./functions)

</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes</summary>

  * Identify different scopes in a program
  * Identify which variable _declarations_ correspond to each variable _use_.

</details>

{: .keypoint}
Scope rules tell us what variable we are talking about when two variables have the same name.

# Why scope?

We have made it to the point where _we might have two totally separate variables with the same name_.  In truth, we got to that point earlier, but it was unlikely to occur.  Now we are in a world where it will happen a lot.  Lets look at an example where this might naturally occur.

Here is a program that will draw a UFO travelling across the screen at the top, and a shadow of that UFO tracking below it.  It has _three different variables in it_.  Each declartion of `xpos` creates a whole new slot in memory and there are three different declarations.  one on line 1, one on line 15 and one on line 20.

```java
int xpos;

void setup(){
  size(400,400);
  xpos = 0;
}

void draw(){
  background(255);
  ufoAt(xpos);
  reflectionAt(xpos);
  xpos = xpos + 1;
}

void ufoAt(int xpos){
  fill(255, 43, 98);
  ellipse(xpos, 10, 40, 20);
}

void reflectionAt(int xpos){
  fill(0,0,0);
  ellipse(xpos, height, 40,20);
}
```

The question that is answered by scope rules is _when I **use** the variable name `xpos`, which declaration will I get?_

Since the declaration and creation of these memory slots is dynamic, lets take a look at the running program to understand better.

<iframe width="560" height="315" src="https://www.youtube.com/embed/56eW-Ti88Nc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## The scoping rules

  * Each curly brace _introduces a new scope_ (not exactly true, see below, but it will do for now).
  * A variable is only alive in the scope in which it is declared.
  * If more than one variable with a certain name is alive, then the one declared in _the smallest enclosing scope_ is the one that is used.

As a side note, these rules mean you can't have two variables with the same name declared in exactly the same scope, and your compiler will enforce this and tell you when you have done so.

### Not exactly true?

For loop, conditions, and functions, the curly brace indicates a new scope, but the scope really starts before the curly brace, at the start of the expression.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pC7RUmHL2KY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
