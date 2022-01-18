---
layout: page
title: Algorithms
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge</summary>

  * <a href="/primitive_operations">Primitive Operations</a>
</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes</summary>

  * Understand what an algorithm is
  * Be able to relate an algorithm to a function
  * Be able to pass values into a function
  * Be able to get values back from a function
  * Be able to write your own functions
</details>

<iframe width="560" height="315" src="https://www.youtube.com/embed/e_WfC8HwVB8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

So, "computer programming is all about writing _algorithms_" is it?  Lets now think more about these algorithms.  Let's think about the different forms they might take, pulling our inspiration from "real life".

Here, we will call algorithms "tasks" because that better matches our intuition.  Tasks can be done by you or by someone else, just as you might program an algorithm yourself or you may call a function to run that algorithm for you.

The easiest way to learn this is to think about real-life tasks such as:

  * personal tasks like getting dressed
  * mechanical tasks like washing clothes
  * computer tasks like working out the fastest route somewhere
  * etc.

A task should have a simple purpose, it might need some resources and carrying out the task might effect other things.  

#### Basic elements of an algorithm

We will define every task according to its:

  * **purpose**
  * **inputs**
  * **effect on the world**
  * **outputs**

Lets consider some tasks and put them into this framework

### Make some toast

  * **purpose:** create toast
  * **inputs:** bread or crumpet and a darkness setting
  * **effects:** none
  * **output:** toasted bread

so the inputs have told us we can't just say *"make some toast"*, we need to say *"make some toast from rye bread on setting 3"*.  This is useful.  Breaking down the tasks has helped us understand it better and be more precise about it.  Lets look at another.

### Make me a sandwich

  * **purpose:** make a sandwich
  * **input:** type of sandwich
  * **effects:** none
  * **output:** sandwich of the correct type

Again we can see we were not precise enough.  We should have said "make me a corn beef and pickle sandwich".

### Mow the lawn

  * **purpose:** make the grass short
  * **input:** area to mow lawn
  * **effects:** the grass in that area is shorter, the air smells of two-stroke.
  * **outputs:** hay

Here we are (assuming we ignore grass clippings) not interested in the _output_ of the task, we are interested in its _effect_.  This lawn mowing example brings up another axis we have not considered yet.  How you mow the lawn depends on the length of the grass.  If the grass is too long you have to mow on a high setting, then go back and mow again on the final setting.  So we really should have another dimension for our tasks, "globals".  Globals are things from the world that effect the tasks, the opposite of "effects" (things from the task that effect the world).

  * **purpose:** make the grass short
  * **input:** area to mow lawn
  * **effects:** the grass in that area is shorter, the air smells of two-stroke.
  * **outputs:** none

Mathematical tasks are a particular type, they generally don't have effects, they have only inputs and outputs.

### Add two numbers

  * **purpose:** get the sum of two numbers
  * **input:** two numbers
  * **effects:** none
  * **output:** a number

So, we have four axis on which to think about any task/algorithm/function.  We can give each combination a nickname, making it easier to remember

  * the purpose of a task is its _name_
  * if a task has inputs it is _informed_.
  * if a task has effects is a _changer_
  * if a task has outputs it is a _producer_

We can give out tasks nicknames now.  "create toast" is an _informed producer_.  "make a sandwich" is an _informed producer_.  "make the grass short" is an _informed changer_ and most mathematical tasks are _informed producer_ s.  You will find some nicknames come up much more often than others.


<iframe width="560" height="315" src="https://www.youtube.com/embed/cDA3_5982h8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# Algorithms in Processing

Programming itself is the creation of algorithms, of creating _recipies_ for the computer to follow.

But, we never write our programs from scratch, we always write them with help from existing algorithms.  That is exactly what you have been doing with your basic Processing programs.  Every time you write `line(0,0, 100, 100)` in Processing, you are saying "please do the _line_ algorithm with the inputs `0`, `0`, `100`, and `100`".  Such algorithms are called _built-in functions_ or _library functions_.  

As you use these build-in functions, you should think about what type of algorithm they are, i.e. which nickname should you give them.

<div class="task" markdown="1">
What is the most appropriate nickname for each of the following processing built-in functions?  You may like to consult the [processing reference](https://processing.org/reference/) to help you work out the answer:

  * `arc`
  * `hue`
  * `%`
  * `floor`

<details markdown="1"><summary>Solution</summary>

  * `arc` is an "informed changer"
  * `hue` is an "informed producer"
  * `%` is an "informed producer"
  * `floor` is an "informed producer"
</details>
</div>

# Basic Functions

Let’s start by reviewing some functions we have seen in Primitive Operations.

Draw line:

  * inputs: `float`, `float`, `float`, `float`
      * first two give x, y location for first point
      * last two give x, y location for second point
  * effects: draws line at the specified position
  * output: none

Draw-line is an informed changer. The draw-line task is implemented in Processing by the `line` function.

~~~~~
line(30, 50, 80, 70); 	// draw line from (30, 50) to (80, 70)
						// remember, you CAN pass integers as float
~~~~~

#### Draw rectangle

  * inputs: `float`, `float`, `float`, `float`
      * first two give x, y location of the top-left corner
      * third value gives width of the rectangle
      * fourth value gives height of the rectangle
  * effects: draws rectangle as specified
  * output: none

implemented in Processing as function `rect`

~~~~~~
rect(40, 30, 10, 15); 	// draw rectangle with top left corner
						// at (40, 30) with width 10 and height 15
~~~~~~

#### Set interior colour

  * input: red, green, blue
  * effects: affects subsequent shapes that are drawn
  * output: none

implemented in Processing as function `fill`and it is an informed changer.

~~~~~
fill(0, 200, 0);             // set interior colour to a shade of green
rect(40, 30, 10, 15);  // rectangle drawn as before but now with a green interior
~~~~~

We can create our own function that creates such a green rectangle.

Draw box:

  * input: none
  * global: none
  * effects: draws a green rectangle
  * output: none

In Processing we can implement this as:

~~~~~
void drawBox() {
    fill(0, 200, 0);      // set interior colour to a shade of green
    rect(40, 30, 10, 15); // draw rectangle
}
~~~~~

This is a simple function that doesn’t take any input.

Now we can draw that green rectangle by doing:

~~~~~
void draw() {
    drawBox();
}
~~~~~

Function `draw` will be explained shortly.

<div class="task" markdown="1">
Write a series of functions that draw parts of a face; use those functions in `draw` to draw the whole face.
</div>

`drawBox` is not a very exciting function because it always draws the same rectangle in the same position. It would be nice to have a function that would allow us to draw the rectangle at whatever position we wanted.

draw box (version 2):

  * input: where we want the top left corner of the rectangle (say `x`, `y`)
  * effects: draws a green rectangle at the specified position
  * output: none

Draw-box has progressed from an uninformed changer to an informer changer.

We can implement it in Processing as:

~~~~~
void drawBox2(int x, int y) {
    fill(0, 200, 0);      // set interior colour to a shade of green
    rect(x, y, 10, 15);   // draw rectangle
}
~~~~~

Now we can see that the first line of the function has two input parameters `x` and `y`. In Processing we need to say what sort of thing they are; we are supplying a and b as integer coordinates so they are integers and we tell Processing this by putting int before each parameter.
Now we can create a complete program that will draw three of our rectangles:

~~~~~
void setup() {
    drawBox2(10, 20);
    drawBox2(70, 40);
    drawBox2(20, 80);
}

void drawBox2(int a, int b) {
    fill(0, 200, 0);      // set interior colour to a shade of green
    rect(a, b, 10, 15);   // draw rectangle
}

~~~~~

The function `setup` is needed because it is the function that Processing runs. Anything that you want run needs to be invoked directly or indirectly from setup.

Inside `drawBox2` we can see that the function gets two parameters as input and they are the coordinates of the top left corner of the rectangle, so they get used as such when rect is used:

  * the first time `drawBox2` is used, `x` is `10` and `y` is `20`
  * the second time, `x` is `70` and `y` is `40`
  * the third time, `x` is `20` and `y` is `80`


Although Processing already has `+` built into it, we can write our own `add` function:

~~~~~
void setup() {
    add(3, 4);
}

int add(int p, int q) {
    return p + q;
}
~~~~~


We note:

  * since add is producing output, we need to say what kind of output it is producing; the sum of two integers is an integer so we want to say that the result is an integer; we do this by putting int before the function name
  * inside the function, we need to say what it is that we want to be the output, so we put return before the value we want output
  * Our program will calculate 3+4 but nothing is done with that value so the program will appear to do nothing. To get it to show us the result we use another function:

print line:

  * input: some value
  * global: none
  * effects: displays the input value
  * output: none

implemented in Processing as function `println`

Now add(3, 4) produces a value (7) which we can use as the input for println:

~~~~~
    println(add(3, 4));      // instead of just add(3, 4);
~~~~~

<div class="task" markdown="1">
Write an algorithm to describe [putting an animation on a computer screen](https://www.youtube.com/watch?v=X1TAdd9Vm7s).
<details class="solution" markdown="1">
  <summary>solution</summary>

  * input: nothing
  * effects: images appear on screen
  * output: none

  24 times a second, update the picture a little bit, put it on the screen, then go back and do it all again.

</details>
</div>

<div class="task" markdown="1">
Create another variant of drawBox that allows you to change some other aspect of the rectangle
</div>

<div class="task" markdown="1">
Write an algorithm that always returns the number 7
</div>

<div class="task" markdown="1">
Write an algorithm that returns the square of the number you give as input. For example, if the value passed is 6, it returns 36. If the value passed is 2.5, it returns 6.25.
</div>
