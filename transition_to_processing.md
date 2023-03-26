---
layout: page
title: Transition to Processing
within: programming
---

<details class="prereq" markdown="1">
<summary>Assumed Knowledge:</summary>

  * Basic Computer Literacy
  * Understands Files and Folders.
</details>

<details class="outcomes" markdown="1">
<summary>Learning Outcomes:</summary>

  * Become familiar with the Processing Programming Environment
  * Create your first Processing Programs on your Own Computer
  * Become familiar with the steps that occur when a processing program is run.
  * Be able to do arithmetic the way computers do.
 </details>

# Textbook

The textbook for this unit is "Learning Processing: A Beginner's Guide to Programming Images, Animation, and Interaction" by Daniel Shiffman. Scan the following QR Code or click on [this link](https://multisearch.mq.edu.au/permalink/61MACQUARIE_INST/467l3g/cdi_skillsoft_books24x7_bks00089202) to download it via Macquarie University. 

Steps to download the book:

1. Click on "Elsevier ScienceDirect Books Complete".
2. At ScienceDirect website, click on "Download all chapters" (you may need to authenticate yourself as an MQ student at this stage).

&nbsp;

<center>
## QR Code for textbook
</center>

<div>
<center><img src="assets/images/learningProcessing.png" style="width: 400px;"/></center>
</div>


# Install Processing

[Processing is available for most desktop operating systems](https://processing.org/download/). You can't run it on an iPad or a Chromebook however.

<div class="task" markdown="1">
[Download and install](https://processing.org/download/) the processing environment on your own computer. Install the latest stable version (ask on forums if unsure).

<iframe width="560" height="315" src="https://www.youtube.com/embed/YZnnzmkWXD8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# Processing Coordinates

When you open Processing an run an empty program you get a pop-up output (Applet), containing a dark grey square region inside it - *the display window*.
By default, Processing display window is of size 100 by 100, which means it's 100 pixels wide and 100 pixels high. Each pixel is a cell, much like Excel cell.

- The top-left pixel's address is at (0, 0) and is known as the *origin*.
- The pixel to the right of the origin is at (1, 0).
- The pixel to the right of (1, 0) is at (2, 0).
- and so on
- The pixel below the origin is at (0, 1).
- The pixel below (0, 1) is at (0, 2).

<iframe width="560" height="315" src="https://www.youtube.com/embed/7Kxqu26Yqpg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Exercise:

- What is the location of a pixel that is `a` pixels to the **right** of `(x, y)`?
- What is the location of a pixel that is `a` pixels to the **left** of `(x, y)`?
- What is the location of a pixel that is `a` pixels **above** `(x, y)`?
- What is the location of a pixel that is `a` pixels **below** `(x, y)`?

<details markdown="1"><summary>Solution</summary>
- a pixels to the right of (x, y): (x+a, y)
<br>
- a pixels to the left of (x, y): (x-a, y)
<br>
- a pixels above (x, y): (x, y-a)
<br>
- a pixels below (x, y): (x, y+a)
</details>

Exercise:

- What is the location of a pixel that is 10 pixels to the right and 30 pixels above (50, 70)?

<details markdown="1"><summary>Solution</summary>
(60, 40)
</details>

Exercise:

- What is the location of a pixel that is 10 pixels to the left and 30 pixels above (80, 40)?

<details markdown="1"><summary>Solution</summary>
(70, 10)
</details>

Exercise:

- What is the location of a pixel that is 40 pixels to the right and 50 pixels below (10, 40)?

<details markdown="1"><summary>Solution</summary>
(50, 90)
</details>


Exercise:

- What is the location of a pixel that is 40 pixels to the right and 50 pixels above (70, 50)?

<details markdown="1"><summary>Solution</summary>
(110, 0)
</details>

## Sample processing programs

### Example 1

Once you have done this, copy-and-paste the following code into the processing IDE and hit the run button.

```processing
line(0, 0, 100, 100);
line(0, 100, 100, 0);
```
Do you see any output window and if so, what is the end result? If not, what is the error message, and what do you think needs to be done to fix it?

<details markdown="1"><summary>Solution</summary>
You should see an X drawn across a small window.  That window is a processing "sketch" that is being drawn in a small window according to your instructions.  In this course we will learn how to give processing very complex instructions to make very complex sketches.  These sketches are really just computer programs like any other but they are started by the processing IDE and you can inspect what is going on inside them with the debugger.
</details>

### Example 2
 
Now, copy-and-paste the following code into the processing IDE and hit the run button.

```processing
line(0, 50, 50, 0)
line(50, 100, 100, 50);
```

Do you see any output window and if so, what is the end result? If not, what is the error message, and what do you think needs to be done to fix it?

<details markdown="1"><summary>Solution</summary>
Error message "Syntax error - Missing ";". To fix it, a semi-colon must be placed at the end of the first instruction.
</details>

Here is a short video we recorded to demonstrate downloading and installing Processing, and creating a simple program with a handul of functions.

<iframe width="560" height="315" src="https://www.youtube.com/embed/FAPel-Dds9k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Here are some more video about basic processing shapes and colors.

<iframe width="560" height="315" src="https://www.youtube.com/embed/DHnGGtm-fgM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/oCLBaGrvhTo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/g5ZSpzo7RzI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# How Processing Works

Programmers need to know how the machine they are programming actually work.  This is one of your primary tasks early on.  You can copy-and-paste some programs, and even make small changes to them, without understanding the underlying machine but you will run out of runway very quickly.

So, what exactly occurs when a processing program is run?  The syntax of a Processing program is:

```processing
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

<div class="task" markdown="1">
Given the following things have occurred during the execution of a processing program, what do you expect to happen next

  * compiler has checked the program
  * compiler has converted the program
  * `setup` has run
  * `draw` has run

<details markdown="1"><summary>solution</summary>
The next step is for the result of the `draw` function to be put on the screen by the operating system/computer.
</details>
</div>

<div class="task" markdown="1">
Which component is responsible for each of the following tasks:

  * convert text to a runnable program
  * work out what occurs in `draw`
  * put actual pictures on the screen
  * work out what occurs in `setup`

<details markdown="1"><summary>Solution</summary>
_The compiler_ will convert text to a runnable program.  _Processing_ will work out what occurs in draw.  _The computer (or the operating system)_ will put actual pictures on the screen.  _Processing_ will work out what occurs in `setup`.
</details>
</div>

<iframe width="560" height="315" src="https://www.youtube.com/embed/sUbcZkot8-A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

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

[COMP1000PracticePrograms.zip](./assets/COMP1000PracticePrograms.zip)

<!--## ADVANCED (HD-level for now) Test-driven development programs 

These are programs to help you get acquainted with test-driven development and help you with module exams (and also major work). Instructions file inside the package explains what needs to be done.

[COMP1000TestDrivenDevelopment.zip](./assets/COMP1000TestDrivenDevelopment.zip)
-->