---
title: Transition to Processing
permalink: /comp1000/transition-to-processing
parent: COMP1000
nav_order: 1
---

- TOC
{:toc}

<!-- Assumed Knowledge -->
{% capture topic_prereq %}
  * Basic Computer Literacy
  * Basic Understanding of Files and Folders.
{% endcapture %}
<!-- Learning Outcomes -->
{% capture topic_outcomes %}
  * Become familiar with the Processing Programming Environment
  * Create your first Processing Programs on your Own Computer
  * Become familiar with the steps that occur when a processing program is run.
  * Be able to do arithmetic the way computers do.
{% endcapture %}

{% include prereq_outcomes.html prereq=topic_prereq outcomes=topic_outcomes %}

## Textbook
 The textbook for this unit is "Learning Processing: A Beginner's Guide to Programming Images, Animation, and Interaction" by Daniel Shiffman. Scan the following QR Code or click on [this link](https://multisearch.mq.edu.au/permalink/61MACQUARIE_INST/467l3g/cdi_skillsoft_books24x7_bks00089202) to download it via Macquarie University.

 Steps to download the book:

1. Click on "Elsevier ScienceDirect Books Complete".
2. At ScienceDirect website, click on "Download all chapters" (you may need to authenticate yourself as an MQ student at this stage).

&nbsp;



<div style="text-align: center;">
  <h4>QR Code for textbook</h4>
  <div class="centred-img">
    <img src="{{ site.baseurl }}/assets/comp1000/learningProcessingQR.png" style="width: 200px;" alt="QR code for textbook"/>
  </div>
</div>


## Install Processing

[Processing is available for most desktop operating systems](https://processing.org/download/). You can't run it on an iPad or a Chromebook however.

[Download and install](https://processing.org/download/) the processing environment on your own computer. Install the latest stable version (ask on forums if unsure).

{% include youtube.html id="YZnnzmkWXD8" %}

## Processing Coordinates

When you open Processing an run an empty program you get a pop-up output (Applet), containing a dark grey square region inside it - *the display window*.
By default, Processing display window is of size 100 by 100, which means it's 100 pixels wide and 100 pixels high. Each pixel is a cell, much like Excel cell.

- The top-left pixel's address is at (0, 0) and is known as the *origin*.
- The pixel to the right of the origin is at (1, 0).
- The pixel to the right of (1, 0) is at (2, 0).
- and so on
- The pixel below the origin is at (0, 1).
- The pixel below (0, 1) is at (0, 2).

{% include youtube.html id="7Kxqu26Yqpg" %}

<!--Exercise 1-->
{% capture problem %}
- What is the location of a pixel that is `a` pixels to the **right** of `(x, y)`?
- What is the location of a pixel that is `a` pixels to the **left** of `(x, y)`?
- What is the location of a pixel that is `a` pixels **above** `(x, y)`?
- What is the location of a pixel that is `a` pixels **below** `(x, y)`?
{% endcapture %}

{% capture solution %}
- a pixels to the right of (x, y): (x+a, y)
<br>
- a pixels to the left of (x, y): (x-a, y)
<br>
- a pixels above (x, y): (x, y-a)
<br>
- a pixels below (x, y): (x, y+a)
{% endcapture %}

{% include exercise.html
  title="Exercise 1"
  problem=problem
  solution=solution
%}


<!--Exercise 2-->
{% capture problem %}
- What is the location of a pixel that is 10 pixels to the right and 30 pixels above (50, 70)?
{% endcapture %}

{% capture solution %}
(60, 40)
{% endcapture %}

{% include exercise.html
  title="Exercise 2"
  problem=problem
  solution=solution
%}

<!--Exercise 3-->
{% capture problem %}
- What is the location of a pixel that is 10 pixels to the left and 30 pixels above (80, 40)?
{% endcapture %}

{% capture solution %}
(70, 10)
{% endcapture %}

{% include exercise.html title="Exercise 3" problem=problem solution=solution %}

<!--Exercise 4-->
{% capture problem %}
- What is the location of a pixel that is 40 pixels to the right and 50 pixels below (10, 40)?
{% endcapture %}

{% capture solution %}
(50, 90)
{% endcapture %}

{% include exercise.html title="Exercise 4" problem=problem solution=solution %}

<!--Exercise 5-->
{% capture problem %}
- What is the location of a pixel that is 40 pixels to the right and 50 pixels above (70, 50)?
{% endcapture %}

{% capture solution %}
(110, 0)
{% endcapture %}

{% include exercise.html title="Exercise 5" problem=problem solution=solution %}

## Sample processing programs

<!-- Example 1 -->
{% capture my_problem %}
Copy-and-paste the following code into the processing IDE and hit the run button.

```
line(0, 0, 100, 100);
line(0, 100, 100, 0);
```
Do you see any output window and if so, what is the end result? If not, what is the error message, and what do you think needs to be done to fix it?
{% endcapture %}

{% capture my_solution %}
You should see an X drawn across a small window.  That window is a processing "sketch" that is being drawn in a small window according to your instructions.  In this course we will learn how to give processing very complex instructions to make very complex sketches.  These sketches are really just computer programs like any other but they are started by the processing IDE and you can inspect what is going on inside them with the debugger.
{% endcapture %}

{% include exercise.html
  title="Example 1"
  problem=my_problem
  solution=my_solution
%}

<!-- Example 2 -->
{% capture my_problem %}
Now, copy-and-paste the following code into the processing IDE and hit the run button.

```
line(0, 50, 50, 0)
line(50, 100, 100, 50);
```

Do you see any output window and if so, what is the end result? If not, what is the error message, and what do you think needs to be done to fix it?
{% endcapture %}

{% capture my_solution %}
```console?output
Syntax error - Missing ";".
```
{: .nolineno}

To fix it, a semi-colon must be placed at the end of the first instruction.
{% endcapture %}

{% include exercise.html
  title="Example 2"
  problem=my_problem
  solution=my_solution
%}

### Videos

Here is a short video we recorded to demonstrate downloading and installing Processing, and creating a simple program with a handul of functions.

{% include youtube.html id="FAPel-Dds9k" %}

Here are some more video about basic processing shapes and colors.

{% include youtube.html id="DHnGGtm-fgM" %}

{% include youtube.html id="oCLBaGrvhTo" %}

{% include youtube.html id="g5ZSpzo7RzI" %}

## How Processing Works

Programmers need to know how the machine they are programming actually work.  This is one of your primary tasks early on.  You can copy-and-paste some programs, and even make small changes to them, without understanding the underlying machine but you will run out of runway very quickly.

So, what exactly occurs when a processing program is run?  The syntax of a Processing program is:

```
void setup() {
 //code that executes once, at the beginning of the program
}

void draw() {
 //code that executes AFTER setup(), over and over
}
```
If we think of the process as a _conversation_ between different _actors_ we would see a conversation like this:

{: .chat.user.left}
Please run this program

{: .chat.compiler.right}
I'm checking the program for errors

{: .chat.compiler.right}
I'm converting the program to a runnable form

{: .chat.processing.left}
I'm running the code in `setup`

{: .chat.processing.left}
I'm running the code in `draw`

{: .chat.computer.right}
I'm displaying the results

{: .chat.processing.left}
I'm running the code in `draw`

{: .chat.computer.right}
I'm displaying the results

{: .chat.processing.left}
I'm running the code in `draw`

{: .chat.computer.right}
I'm displaying the results

{: .chat.processing.left}
I'm running the code in `draw`

{: .chat.computer.right}
I'm displaying the results

... and so on ad-infinitum until

{: .chat.user.left}
I'm shutting this thing down.

<!--Exercise 6-->
{% capture problem %}
Given the following things have occurred during the execution of a processing program, what do you expect to happen next

  * compiler has checked the program
  * compiler has converted the program
  * `setup` has run
  * `draw` has run
{% endcapture %}

{% capture solution %}
The next step is for the result of the `draw` function to be put on the screen by the operating system/computer
{% endcapture %}

{% include exercise.html title="Exercise 6" problem=problem solution=solution %}

<!--Exercise 7-->
{% capture problem %}
Which component is responsible for each of the following tasks:

- Convert text to a runnable program
- Work out what occurs in `draw`
- Put actual pictures on the screen
- Work out what occurs in `setup`
{% endcapture %}

{% capture solution %}
_The compiler_ will convert text to a runnable program.
_Processing_ will work out what occurs in `draw`.
_The computer (or the operating system)_ will put actual pictures on the screen.
_Processing_ will work out what occurs in `setup`.
{% endcapture %}

{% include exercise.html title="Exercise 7" problem=problem solution=solution %}


{% include youtube.html id="sUbcZkot8-A" %}

<!--# Integer Division

Processing insists that if you divide one integer by another, you should get an integer back as the result.  This is simple enough for `4/2` which is `2` but what answer should you get from `4/3`?  Processing will do integer division as a _quotient_ and _remainder_ just like you did in primary school.  `/` gets you the quotient and the new operation `%` gets you the remainder:

  - `4/2` = `2`
  - `4/3` = `1` because the full answer would be "1 remainder 1"
  - `8/3` = `2` because the full answer would be "2 remainder 2"
  - `7/3` = `2` because the full answer would be "2 remainder 1"
  - `4%3` = `1` because the full answer would be "1 remainder 1"
  - `8%3` = `2` because the full answer would be "2 remainder 2"
  - `7%3` = `1` because the full answer would be "2 remainder 1"

<div class="task" markdown="1">
Compute the following expressions according to rules of Processing:

  - `3+5`
  - `-2*5`
  - `12/3`
  - `17/5`
  - `17/6`
  - `12%3`
  - `17%5`
  - `17%6`
  - `12.0/5.0`

<details markdown="1"><summary>solutions</summary>
  - `3+5` = `8`<br>
  - `-2*5` = `-10`<br>
  - `12/3` = `4`<br>
  - `17/5` = `3`<br>
  - `17/6` = `2`<br>
  - `12%3` = `0`<br>
  - `17%5` = `2`<br>
  - `17%6` = `5`<br>
  - `12.0/5.0`= `2.4`
</details>
</div>
-->

## Practice programs

These are programs to help you start with simple sketches are work your way up to more complex animation (over the course of the session). Very helpful for incremental learning and assignments.

[COMP1000PracticePrograms.zip]({{ site.baseurl }}/assets/comp1000/transition-to-processing/COMP1000PracticePrograms.zip)

<!--## ADVANCED (HD-level for now) Test-driven development programs

These are programs to help you get acquainted with test-driven development and help you with module exams (and also major work). Instructions file inside the package explains what needs to be done.

[COMP1000TestDrivenDevelopment.zip]({{ site.baseurl }}/assets/comp1000/transition-to-processing/COMP1000TestDrivenDevelopment.zip)
--->


