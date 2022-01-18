---
layout: page
title: "Refactoring"
within: programming
---
<details class="prereq" markdown="1"><summary>Assumed Knowledge</summary>
  * [Primitive Operations](primitive_operations)
  * [Variables](variables)
  * [Loops](loops)
  * [Functions](functions)
  * [Compound Data](composite_data)
  * [Scope](scope)
</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes</summary>
  * Be able to identify why one program snippet is preferrable over another.
  * Be able to convert programs from a poorer version to a better version.
</details>

{: .keypoint}
We refactor code to _takeaway duplicate or similar code_, _to make our program easier to understand_, and _to improve code maintenance_.

<iframe width="560" height="315" src="https://www.youtube.com/embed/vcydPCZJMBc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Variables

### Renaming Variables

You want meaningful variable names.  If you find you have a variable that is not self-describing, give it a better name.

<div class="row">
	<div class="col-xs-5">
<pre><code>
int d = 20;

ellipse(width/2, height/2, d, d);
</code></pre>
	</div>
	<div class="col-xs-2 refactor">&nbsp;</div>
	<div class="col-xs-5">
<pre><code>
int diameter = 20;

ellipse(width/2, height/2, diameter, diameter);
</code></pre>
	</div>
</div>


### Magic Numbers

Any value that you are using _in multiple places_ but _for the same underlying concept_ is called a magic number and should be replaced by a variable

<div class="row">
	<div class="col-xs-5">
<pre><code>
ellipse(width/2, height/2, 20, 20);
</code></pre>
	</div>
	<div class="col-xs-2 refactor">&nbsp;</div>
	<div class="col-xs-5">
<pre><code>
int circleSize = 20;

ellipse(width/2, height/2, circleSize, circleSize);
</code></pre>
	</div>
</div>

# Conditions

### Common body of `if`

<div class="row">
	<div class="col-xs-5">
<pre><code>
if(x < 7)
	y = 4;
if(x > 23)
	y = 4;
</code></pre>
	</div>
	<div class="col-xs-2 refactor">&nbsp;</div>
	<div class="col-xs-5">
<pre><code>
if(x < 7 || x > 23)
	y = 4;
</code></pre>
	</div>
</div>


### Common `if` condition
<div class="row">
	<div class="col-xs-5">
<pre><code>
if(x < 7)
	y = 4;
if(x < 7)
	z = 9;
</code></pre>
	</div>
	<div class="col-xs-2 refactor">&nbsp;</div>
	<div class="col-xs-5">
<pre><code>
if(x < 7) {
	y = 4;
	z = 9;
}
</code></pre>
	</div>
</div>

### Nested `if` statements can sometimes be combined.

It is often possible to replace nested `if` statements with a single `if` statement that has a more complex condition.  You should take this option _as long as the condition does not become too complex itself_.
<div class="row">
	<div class="col-xs-5">
<pre><code>
if(x < 7){
	if (y < 7){
		y = 4;
	}
}
</code></pre>
	</div>
	<div class="col-xs-2 refactor">&nbsp;</div>
	<div class="col-xs-5">
<pre><code>
if(x < 7 && y < 7) {
	y = 4;
}
</code></pre>
	</div>
</div>

# Loops

### Simple formula

<div class="row">
	<div class="col-xs-5">
<pre><code>
ellipse(30, 30, 10, 10);
ellipse(60, 60, 10, 10);
ellipse(90, 90, 10, 10);
ellipse(120, 120, 10, 10);
ellipse(150, 150, 10, 10);
</code></pre>
	</div>
	<div class="col-xs-2 refactor">&nbsp;</div>
	<div class="col-xs-5">
<pre><code>
for(int i = 30; i <= 150; i += 30){
	ellipse(i, i, 10, 10);
}
</code></pre>
	</div>
</div>

### No simple forumla

Introduce an array to store the values you need and loop over the array.

<div class="row">
	<div class="col-xs-5">
<pre><code>
ellipse(30, 30, 10, 10);
ellipse(50, 50, 10, 10);
ellipse(110, 110, 10, 10);
ellipse(120, 120, 10, 10);
ellipse(160,160, 10, 10);
</code></pre>
	</div>
	<div class="col-xs-2 refactor">&nbsp;</div>
	<div class="col-xs-5">
<pre><code>
int[] z = {30, 50, 110, 120, 160};
for(int i = 0; i < z.length; i++){
	ellipse(z[i], z[i], 10, 10);
}
</code></pre>
	</div>
</div>

### Loop with calculation

Sometimes, in using a loop to position multiple things on the screen, we end up using a calculation based on the loop variable.  It is often possible to adjust the way that loop variable progresses instead.  You end up with more meaningful coe because the loop variable is taking exactly the values you need - it is a little-bit of documentation _and_ the code is simpler.

<div class="row">
	<div class="col-xs-5">
<pre><code>
for(int i = 0; i < 10; i++){
	ellipse(width/2, height/2, i*10, i*10);
}
</code></pre>
	</div>
	<div class="col-xs-2 refactor">&nbsp;</div>
	<div class="col-xs-5">
<pre><code>
for(int i = 0; i < 100; i = i + 10){
	ellipse(width/2, height/2, i, i);
}
</code></pre>
	</div>
</div>

# Functions

<iframe width="560" height="315" src="https://www.youtube.com/embed/GmWFXwyVW_E" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Common Code
Note that the following examples show cases where new functions could be created but in practical cases, we would be more likely to create a new function if:

  * it has a reasonable size or complexity
  * it will be used (or is likely to be used) in multiple places in the code

You might have similar code in two (or more) place in your program.  For example

~~~~~
stroke(0);
fill(255, 0, 0);
ellipse(255, 200, 40, 40);
~~~~~

in one place and

~~~~~
stroke(0);
fill(255, 0, 0);
ellipse(300, 250, 40, 40);
~~~~~

in another.

You should create a function to do that job

~~~~~
void drawRedEllipse(int x, int y){
	stroke(0);
	fill(255, 0, 0);
	ellipse(x, y, 40, 40);
}
~~~~~

and replace the other places with calls to this function.


## Common code but with one troublesome variation

Imagine you have, in one place in the code:

~~~~~
stroke(0)
fill(255, 0, 0);
ellipse(150, 200, 40, 40);
~~~~~

and at another place in the code:

~~~~~
stroke(0)
fill(255, 0, 0);
rect(300, 250, 40, 40);
~~~~~

The structure is the same, the numbers are the same, the intent is very similar, it would be great to have one place to put this code.

To achieve this, you should introduce a parameter that can be used to indicate which version of the major variation should be used. Create a new function and constants for the new parameter:

~~~~~
int SHAPE_ELLIPSE = 1;
int SHAPE_RECT = 2;

void drawRedShape(int x, int y, int shape) {
	stroke(0);
	fill(255, 0, 0);
	if(shape == SHAPE_ELLIPSE){
		ellipse(x, y, 40, 40);
	} else {
		rect(x, y, 40, 40);
	}
}
~~~~~

and in the first place, replace with:

~~~~~
drawRedShape(150, 200, SHAPE_ELLIPSE);
~~~~~

and in the second place, replace with:

~~~~~
drawRedShape(300, 250, SHAPE_RECT);
~~~~~

### Splitting big functions

The following function picks the (first) array element that is closest to the average

~~~~~
int closestToAverage(int[] a){

	int sum = 0;

	for(int i = 0; i < a.length; i++){
		sum += a[i];
	}

	float avg = (float)sum / a.length;

	println(avg);

	int closest = a[0];
	float smallestGap = abs(a[0] - avg);

	for(int i = 1; i < a.length; i++){
		float currentGap = abs(a[i] - avg);
		if(currentGap < smallestGap){
			smallestGap = currentGap;
			closest = a[i];
		}
	}

	return closest;
}
~~~~~

The function is really doing two separate tasks:

  * calculating the average
  * scanning the array to find the (first) element that is closest the average

We could create two functions to do these two tasks. The first function can calculate the average and the second function can be slightly generalised so that it will scan an array and find the (first) element that is closest to a particular value.

We now have two functions that are more likely to be used elsewhere in our programs than the original.


### `if` returns `true` and `false`

If you end up with `return true` or `return false` in the body of an if, then the condition probably contains all the information you need.

<div class="row">
	<div class="col-xs-5">
<pre><code>
if(x){
	return true;
} else {
	return false;
}
</code></pre>
	</div>
	<div class="col-xs-2 refactor">&nbsp;</div>
	<div class="col-xs-5">
<pre><code>
return x;
</code></pre>
	</div>
</div>

### dead code removal

You might have mutliple code paths in a function and you end up with mutliple `return` statements.  Make sure you don't have any redundant ones.

<div class="row">
	<div class="col-xs-5">
<pre><code>
if(x){
	return 1;
} else {
	return 2;
}
return 3;
</code></pre>
	</div>
	<div class="col-xs-2 refactor">&nbsp;</div>
	<div class="col-xs-5">
<pre><code>
if(x){
	return 1;
} else {
	return 2;
}
</code></pre>
	</div>
</div>

_Incomming: vid to come here (??)_
