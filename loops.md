---
layout: page
title: Loops
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge</summary>

  * [Primitive Operations](./primitive_operations)
  * [Variables](./variables)
  * [Conditions](./conditions)
</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes</summary>

  * Know the two types of loops
  * Understand how to use loops to draw multiple things in one frame
  * Understand syntax and semantics of loops
  * Be able to trace loops with tables

</details>

# Loops

Loops are similar to conditions except that after every iteration of the loop, the expression is checked again.

{: .readings}
Chapter 6 of [Learning Processing](https://learningprocessing.com) by Danel Shiffman.

<iframe width="560" height="315" src="https://www.youtube.com/embed/RtAPBvz6k0Y" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/esKLU3dJo70" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/h4ApLHe8tbk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Statement or Expression

Firstly, loops are _statements_ not expressions, for the same reasons as `if` statements.  That means they don't have an equivalent _value_.  Instead, they are useful because of what they _do_.

Both loops and `if` statements are called "control-flow" statements because they change the flow of the program from top-to-bottom to somethings more complex.  We will see another control flow statement when we see functions.

## A `while` loop


```java
while(boolean expression) {
	code inside loop
}
rest of the code
```

<center><img src="loopsFigs/whileLoop.png" style="width: 300px;"/></center>

Example:

```java
int a = 6;
int result = 1;
while(a > 0) {
	result = result * a;
	a = a - 1;
}
println(result);
```

<center><img src="loopsFigs/whileExample.png" style="width: 300px;"/></center>


The above code executes the loop 6 times (for `a` = 6,5,4,3,2,1 but not for 0) each time multiplying the current value of `a` into `result` and the final value of `result` is 6\*5\*4\*3\*2\*1 = 720.

There is a better way of tracing loops known as logic table construction. The logic table for the above example is given below.

{: .table}
| a 	| a > 0 	| result      	|
|---	|-------	|-------------	|
| 6 	| true  	| 1\*6 = 6     	|
| 5 	| true  	| 6\*5 = 30    	|
| 4 	| true  	| 30\*4 = 120  	|
| 3 	| true  	| 120\*3 = 360 	|
| 2 	| true  	| 360\*2 = 720 	|
| 1 	| true  	| 720\*1 = 720 	|
| 0 	| false 	|             	|

<iframe width="560" height="315" src="https://www.youtube.com/embed/VbGDp1FaDzc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Guidelines for constructing a logic table

While constructing a logic table, one is strongly encouraged to follow the following steps:

1. Identify all variables involved in the boolean expression in the loop header.
2. Create columns for each of the variables identified in step 1.
3. Create a column for the loop expression. Create multiple columns to simplify reaching the expression if complex. For example, if expression is `x==y && !z`, the variables involved are `x`, `y`, and `z` and the sub-expressions are `x==y` and `!z`.
4. Create columns for each variable (**unless column for the variable already present**) modified in the loop (in the order they are modified).

### Example for constructing a logic table

```java
int a = 10, b = 2, c = 100;
int result = 0;
while(a > b && c > a) {
	result = result + 1;
	a = a - 1;
	c = c / 2;
}
```

{: .table}
| a  	| b 	| c   	| a > b 	| c > a 	| a > b && c > a 	| result  	|
|----	|---	|-----	|-------	|-------	|----------------	|---------	|
| 10 	| 2 	| 100 	| true  	| true  	| true           	| 0+1 = 1 	|
| 9  	| 2 	| 50  	| true  	| true  	| true           	| 1+1 = 2 	|
| 8  	| 2 	| 25  	| true  	| true  	| true           	| 2+1 = 3 	|
| 7  	| 2 	| 12  	| true  	| true  	| true           	| 3+1 = 4 	|
| 6  	| 2 	| 6   	| true  	| false 	| false          	|         	|

Note that we don't have columns for `a` and `c` again even though they are modified inside the loop because columns for those variables are already present in the table by virtue of step 2.

<details markdown="1">
<summary>An alternative table</summary>

Such a table is not a formal document, it is _an aid to understanding_ and this means it is only valuable if it works _for you_.  To this end, here is another table for the same problem.  It is just as good as the other one, but might work better for you.  Further, you should experiment with your own style rather than stick rigidly to these examples.

{: .table}
| a  	| b 	| c   	| result  	| a > b 	  | && |  c > a        |
|----	|---	|-----	| --------	|-------	  | -- | -------       |
| 10 	| 2 	| 100 	| 0 	    | `10>2` = T | && |  `100>10` = T        |
|       |       |       |           | T       | && | T                 |
|       |       |       |           |         | T |                  |
| 9  	| 2 	| 50  	| 1 	    | `9>2` = T  | && |	  `50>9` = T   |
|       |       |       |           | T       | && | T                 |
|       |       |       |           |         | T |                  |
| 8  	| 2 	| 25  	| 2 	    | `8>2` = T  | && |	  `25>8` = T   |
|       |       |       |           | T       | && | T                 |
|       |       |       |           |         | T |                  |
| 7  	| 2 	| 12  	| 3     	| `7>2` = T  | && |	  `12>7` = T   |
|       |       |       |           | T       | && | T                 |
|       |       |       |           |         | T |                  |
| 6  	| 2 	| 6   	|         	| `6>2` = T  | && |	  `6>6` = F    |
|       |       |       |           | T       | && | F                 |
|       |       |       |           |         | F |                  |

</details>

## for-loop

A for-loop is more compact than the while loop and more common in real-life applications.

```java
for(initializations; boolean expression; update(s)) {
  code inside loop;
}
rest of the code;
```

<center><img src="loopsFigs/forLoop.png" style="width: 300px;"/></center>

Example:

```java
int result = 0;
for(int i=1; i <= 16; i*=2) {
  result = result + i;
}
println(result);
```

Trace (logic table):

{: .table}
| i  	| i<=16 	| result     	|
|----	|-------	|------------	|
| 1  	| true  	| 0+1 = 1    	|
| 2  	| true  	| 1+2 = 3    	|
| 4  	| true  	| 3+4 = 7    	|
| 8  	| true  	| 7+8 = 15   	|
| 16 	| true  	| 15+16 = 31 	|
| 32 	| false 	|            	|


<div class="task" markdown="1">
[Modify your animated blue circle](./conditions.html#two_way_animated_blue_circle) so that it is an animated blue [bullseye](https://www.google.com/search?q=bullseye) instead. Hint:  You can get a thin circle using `noFill` and a larger `strokeWeight` value;

<details class="solution" markdown="1"><summary>solution</summary>
Instead of drawing a simple circle, we draw three circles, each 10 pixels larger than the last.  Each has a 2 pixel border, making a bulleye shape.  Nothing else needs to change, the center of the bullsye animates in exactly the same way as the circle did.

~~~~~
int ypos;
int speed;

void setup(){
  ypos = 0;
  speed = 1;
}

void draw(){
  background(255);

  if (ypos == height){
    speed = -1;
  }
  if (ypos == 0){
    speed = 1;
  }
  noFill();
  stroke(92, 136, 218);
  strokeWeight(2);
  for(int i = 0; i < 40; i = i + 10){
    circle(width/2, ypos, i);
  }
  ypos = ypos + speed;

}
~~~~~

</details>
</div>

# Looking at loops _without_ the draw loop

<iframe width="560" height="315" src="https://www.youtube.com/embed/Z8s-7beNP1c" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

As discussed in the above video, the fact that processing is always in a "draw loop" can confuse things somewhat.  It is possible to see all the operation of loops free of this constraint if we work only on _the console_.  [The console is the black area below your program](./debugging) and it is available even when you do a "static" processing program (one that has no `setup` or `draw`).

<div class="task" markdown="1">
Using loops, draw five `^` (hat) characters to the console
<details class="solution" markdown="1"><summary>solution</summary>
~~~~~
for(int i = 0; i < 5; i++){
	print('^');
}
~~~~~

Notice that this program has no `setup` and no `draw` functions, it is a special type of non-animated Processing program.
</details>
</div>


## Nesting of control structures

Control structures are literally like lego blocks, you can arrange them as you want, depending on the situation. So you can put loops/conditions inside other loops/conditions (and then more loops/conditions inside that and so on).

<iframe width="560" height="315" src="https://www.youtube.com/embed/H7frvcAHXps" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/hk0nYHGma8M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Let's take some examples of a situation where such nesting is required.

### Nesting scenario 1

We would like to generate a pattern based on input integer `N > 0`


`N=4`

```
^
^ ^
^ ^ ^
^ ^ ^ ^
```

<p>&nbsp;</p>

`N=6`

```
^
^ ^
^ ^ ^
^ ^ ^ ^
^ ^ ^ ^ ^
^ ^ ^ ^ ^ ^
```

**STEP 1:** There are `N` lines.

Outer loop -

```java
for(int i=1; i<=N; i++) {
	display current line
	change line using println();
}
```

**STEP 2:** Line corresponding to a given value of `i` has `i` caps

(when `i = 1`, there is 1 cap, when `i = 2` there are 2 caps, and so on ...).

Inner loop -

```java
for(int k=1; k<=i; k++) {
	print("^");
}
```

**COMPLETE SOLUTION**

```java
for(int i=1; i<=N; i++) {
	for(int k=1; k<=i; k++) {
		print("^");
	}
	println();
}
```

<div class="task" markdown="1">
Change the code so that the symbols alternate between a cap (^) and a dash (-) between lines.

`N=6`

```
^
- -
^ ^ ^
- - - -
^ ^ ^ ^ ^
- - - - - -
```

The difference from scenario 1 is that if outer loop counter `i` is an odd number, it's a cap (`^`) while if the outer loop counter `i` is an even number, it's a dash (`-`).

So the earlier display statement

```
print("^");
```

will change to,

```
if(i%2 == 1) { //odd counter: cap
	print("^");
}
else { //even counter: dash
	print("-");
}
```

<details markdown="1"><summary>Solution</summary>

```java
for(int i=1; i<=N; i++) {
	for(int k=1; k<=i; k++) {
		if(i%2 == 1) { //odd counter: cap
			print("^");
		}
		else { //even counter: dash
			print("-");
		}
	}
	println();
}
```
</details>
</div>


<div class="task" markdown="1">
Change the code so that the symbols alternate between ^ and - within a line.

`N=6`

```
^
^ -
^ - ^
^ - ^ -
^ - ^ - ^
^ - ^ - ^ -
```
<details markdown="1"><summary>Solution</summary>
The only change required is to use `k` instead of `i` to decide what symbol to print

```
int N = 6;

for(int i=1; i<=N; i++) {
  for(int k=1; k<=i; k++) {
    if (k % 2 == 1)
      print("^");
    else
      print("-");
  }
  println();
}
```
</details>
</div>

<div class="task" markdown="1">

Change the code so that the symbols alternate between ^ and - within a line and also the first symbol on each line is different from the first symbol on the previous line

`N=6`

```
^
- ^
^ - ^
- ^ - ^
^ - ^ - ^
- ^ - ^ - ^
```
<details markdown="1"><summary>Solution</summary>
This seems like a curly problem until we realise that _adding_ `k` and `i` will give the pattern required because `i` goes up by one each line, swapping the "oddness" of each slot in that row.

```
int N = 6;

for(int i=1; i<=N; i++) {
  for(int k=1; k<=i; k++) {
    if ((k+i) % 2 == 0)
      print("^");
    else
      print("-");
  }
  println();
}
```
</details>
</div>

# Coding in the real world

Just like in conditions, lets see some real-world scenarios where we need to use loops.

But there is a problem. Loops usually iterate over a *collection* (an array, list, hashmap, etc). Since we can't assume knowledge of the same in this document, we're in a bit of a pickle, aren't we?

So, instead we'll iterate over numbers generated via a random-number generator.


### Assumption for scenarios

For scenarios 1 to 3, you may assume that `n` is generated using the following statement:

```java
int x = 1 + (int)random(100); //x can be any integer from 1 to 100
int n = 10*x; //n can be one of the values from [10, 20, ..., 1000]
```


<div class="task" markdown="1">
Write a piece of code that determines the number of times we get a 6 when a normal 6-faced die is rolled `n` times.
<details markdown="1"><summary>Solution</summary>

```
int x = 1 + (int)random(100); //x can be any integer from 1 to 100
int n = 10*x; //n can be one of the values from [10, 20, ..., 1000]

int total = 0;
for(int i = 0; i < n; i++){
  int thisRoll = (int)random(1,7);
  if (thisRoll == 6){
    total++;
  }
}
println(total);
```
</details>
</div>

<div class="task" markdown="1">
Write a piece of code that determines the average outcome when a normal 6-faced dice is rolled `n` times.
<details markdown="1"><summary>Solution</summary>
You should expect to get 3 just about every time right?

```
int x = 1 + (int)random(100); //x can be any integer from 1 to 100
int n = 10*x; //n can be one of the values from [10, 20, ..., 1000]

int total = 0;
for(int i = 0; i < n; i++){
  int thisRoll = (int)random(1,7);
  total = total+thisRoll;
}
println(total/n);
```
</details>
</div>

<div class="task" markdown="1">
For this scenario, you should assume that `n` is generated using the following statement:

```java
int n = (int)random(101); //n can be any integer from 0 to 100
```

Consider a party where there are 4 people. Call them Alice, Bob, Charles and Diane. Assuming they are all friendly and logical people, the following handshakes will take place:

- Alice with
	1. Bob
	2. Charles
	3. Diane
- Bob (already shook hands with Alice) with
	1. Charles
	2. Diane
- Chales (already shook hands with Alice and Bob) with
	1. Diane
- Diane (already shook hands with everyone)

Thus, there are 3+2+1 = 6 handshakes for 4 people.

If a fifth person (Eddie) joins the party, he shakes hands with all others.

Thus, there are **`4`**+3+2+1 = 10 handshakes for 5 people.

A table summarizing this pattern is given below,

{: .table}
| Number of people 	| Number of handshakes         	|
|------------------	|------------------------------	|
| 1                	| 0                            	|
| 2                	| 1                            	|
| 3                	| 2+1                          	|
| 4                	| 3+2+1                        	|
| 5                	| 4+3+2+1                      	|
| ...              	|                              	|
| n                	| (n-1) + (n-2) + .... + 2 + 1 	|

There is actually a very elegant formula to get this value, but for the purpose of our exercise, we'd like you to compute the number of handshakes in a party of `n` people using a loop.

<details markdown="1"><summary>Solution</summary>

```
int n = (int)random(101); //x can be any integer from 1 to 100


int handshakes = 0;

for(int i = n-1; i > 0; i--){
  handshakes = handshakes + i;
}

println(n + " people means");
println(handshakes + " handshakes");
```

</div>
