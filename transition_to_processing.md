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

{: .readings}
Learning Processing: Introduction- Macquarie University Students [have access via the library](https://multisearch.mq.edu.au/permalink/61MACQUARIE_INST/1c87tk9/alma99244325146802171)

# Install Processing

[Processing is available for all desktop operating systems](https://processing.org/download/).  You can't run it on an iPad or a Chromebook however.

<div class="task" markdown="1">
[Download and install](https://processing.org/download/) the processing environment on your own computer.

Once you have done this, copy-and-paste the following code into the processing IDE and hit the run button.

```java
line(0,0,width, height);
line(0, height, width, 0);
```

What is the end result?

<details markdown="1"><summary>Solution</summary>
You should see an X drawn across a small window.  That window is a processing "sketch" that is being drawn in a small window according to your instructions.  In this course we will learn how to give processing very complex instructions to make very complex sketches.  These sketches are really just computer programs like any other but they are started by the processing IDE and you can inspect what is going on inside them with the debugger.
</details>
</div>

# How Processing Works

Programmers need to know how the machine they are programming actually work.  This is one of your primary tasks early on.  You can copy-and-paste some programs, and even make small changes to them, without understanding the underlying machine but you will run out of runway very quickly.

So, what exactly occurs when a processing program is run?  If we think of the process as a _conversation_ between different _actors_ we would see a conversation like this:

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

# Integer Division

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
