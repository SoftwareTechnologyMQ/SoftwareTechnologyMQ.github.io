---
layout: page
title: Moving composite shapes
within: programming
---

<details class="prereq" markdown="1">
<summary>Assumed Knowledge</summary>
  * [Transition to Processing](./transition_to_processing)
</details>
  * [Variables](./variables)

<details class="outcomes" markdown="1">
<summary>Learning Outcomes</summary>
  * Be able to move a complex shape (or change some other attributes)
</details>

Note: ALl the codes in this page are provided at [movingCompositeShapesCode.zip](./assets/codes/movingCompositeShapesCode.zip)

# Moving composite shapes

Once you understand variables, moving simple shapes like circles and rectangles is hopefully straightforward.

```processing
float x;

void setup() {
	size(400, 300);
	//we need to wait until size executes to know the correct width
	x = width/2; 
	background(255);
}

void draw() {
	background(255);
	float dia = 50;
	
	/*
	our circle moves horizontally, 
	so we don't need to have y value in a variable
	*/
	fill(255, 0, 0);
	noStroke();
	circle(x, height/2, dia);
	
	x = x - 1; //in the next iteration, x will be one lesser
}
```	
	

Moving a composite shape is trickier than moving a basic shape. But the key there is to have ONE REFERENCE POINT, and everyhthing else relative to that.

Consider the following composite shape.

```processing
size(600, 400);
background(255);
noStroke();
fill(0, 0, 255);
rectMode(CENTER); //this means instead of top-left corner, we specify the center x and center y, applies to square too
square(300, 200, 50); //create a bounding box around the circle, to be drawn over the square
fill(255, 0, 0);
circle(300, 200, 50);
//to understand the following calculations, read this: https://processing.org/tutorials/trig
float onCircleX1 = 300 + 25*cos(2.25*PI);
float onCircleY1 = 200 + 25*sin(2.25*PI);
float onCircleX2 = 300 + 25*cos(2.75*PI);
float onCircleY2 = 200 + 25*sin(2.75*PI);
fill(0, 255, 0);
triangle(300, 200, onCircleX1, onCircleY1, onCircleX2, onCircleY2);
```

The first problem is that if we want to relocate this shape to another position in the display window, we have to replace 

- every single occurrence of `300` with the new `x` value
- every single occurrence of `200` with the new `y` value


However, if we store the `x` and `y` values in two variables, we only have to change it once in case we change our mind.


```processing
size(600, 400);
background(255);

float x = width/2;
float y = height/2;

noStroke();
fill(0, 0, 255);
rectMode(CENTER); //this means instead of top-left corner, we specify the center x and center y, applies to square too
square(x, y, 50); //create a bounding box around the circle, to be drawn over the square

fill(255, 0, 0);
circle(x, y, 50);

//to understand the following calculations, read this: https://processing.org/tutorials/trig
float onCircleX1 = x + 25*cos(2.25*PI);
float onCircleY1 = y + 25*sin(2.25*PI);
float onCircleX2 = x + 25*cos(2.75*PI);
float onCircleY2 = y + 25*sin(2.75*PI);

fill(0, 255, 0);
triangle(x, y, onCircleX1, onCircleY1, onCircleX2, onCircleY2);
```

### Magic numbers

This draws a triangle on a circle on a square. But that `25` and `50` are hard-coded values, we call *magic numbers*. (As in, appearing magically).

To make the program scalable, we need to fix that. So we identify diameter, and then radius is always going to be half of that.

```processing
size(600, 400);
background(255);

float x = width/2;
float y = height/2;

float diameter = random(50, 100);
float radius = diameter/2;

noStroke();
fill(0, 0, 255);
rectMode(CENTER); //this means instead of top-left corner, we specify the center x and center y, applies to square too
square(x, y, diameter); //create a bounding box around the circle, to be drawn over the square

fill(255, 0, 0);
circle(x, y, diameter);

//to understand the following calculations, read this: https://processing.org/tutorials/trig
float onCircleX1 = x + radius*cos(2.25*PI);
float onCircleY1 = y + radius*sin(2.25*PI);
float onCircleX2 = x + radius*cos(2.75*PI);
float onCircleY2 = y + radius*sin(2.75*PI);

fill(0, 255, 0);
triangle(x, y, onCircleX1, onCircleY1, onCircleX2, onCircleY2);
```

Similarly, the `2.25\*PI` and `2.75\*PI` are angles are magic numbers. Represent them properly, and we get:


```processing
size(600, 400);
background(255);

float x = width/2;
float y = height/2;

float diameter = random(50, 100);
float radius = diameter/2;

noStroke();
fill(0, 0, 255);
rectMode(CENTER); //this means instead of top-left corner, we specify the center x and center y, applies to square too
square(x, y, diameter); //create a bounding box around the circle, to be drawn over the square

fill(255, 0, 0);
circle(x, y, diameter);

//to understand the following calculations, read this: https://processing.org/tutorials/trig
float angle1 = 2.25*PI;
float angle2 = 2.75*PI;
float onCircleX1 = x + radius*cos(angle1);
float onCircleY1 = y + radius*sin(angle1);
float onCircleX2 = x + radius*cos(angle2);
float onCircleY2 = y + radius*sin(angle2);

fill(0, 255, 0);
triangle(x, y, onCircleX1, onCircleY1, onCircleX2, onCircleY2);
```

Next, put the shape into draw, but **not** move. Variables are *local* and not *global* since we don't need to remember their values from one iteration to another.

```processing
void setup() {
  size(600, 400);
  background(255);
}

void draw() {
  /*
  variables are local since we don't need to remember
  their values from one iteration to another
   */
  float x = width/2;
  float y = height/2;

  float diameter = random(50, 100);
  float radius = diameter/2;
  float angle1 = 2.25*PI;
  float angle2 = 2.75*PI;

  background(255); //so as to clear any previous shape
  noStroke();
  fill(0, 0, 255);
  rectMode(CENTER); //this means instead of top-left corner, we specify the center x and center y, applies to square too
  square(x, y, diameter); //create a bounding box around the circle, to be drawn over the square

  fill(255, 0, 0);
  circle(x, y, diameter);

  //to understand the following calculations, read this: https://processing.org/tutorials/trig
  float onCircleX1 = x + radius*cos(angle1);
  float onCircleY1 = y + radius*sin(angle1);
  float onCircleX2 = x + radius*cos(angle2);
  float onCircleY2 = y + radius*sin(angle2);

  fill(0, 255, 0);
  triangle(x, y, onCircleX1, onCircleY1, onCircleX2, onCircleY2);
}
```

Next, let's say we want the shape to move UP.

If you simply add,

```processing
y=y-1;
```

as the last statement, nothing will happen (seriously, try it!). This is because y decreases by 1 and is IMMEDIATELY destroyed in the memory upon completion of first iteration of `draw()`. Then, it is declared and assigned to `height/2` again at the start of the second iteration. Again, it is destroyed in the memory upon completion of second iteration of `draw()` and so on and so forth.

----------

- `draw()` iteration 1
- `y` declared and becomes `height/2`.
- on the last statement in `draw`, `y` decreases by 1, becomes `height/2 - 1`.
- `y` immediately destroyed and erased from memory upon completion of iteration 1.

----------

- `draw()` iteration 2
- `y` declared and becomes `height/2`.
- on the last statement in `draw`, `y` decreases by 1, becomes `height/2 - 1`.
- `y` immediately destroyed and erased from memory upon completion of iteration 2.

----------

- `draw()` iteration 3
- `y` declared and becomes `height/2`.
- on the last statement in `draw`, `y` decreases by 1, becomes `height/2 - 1`.
- `y` immediately destroyed and erased from memory upon completion of iteration 3.

----------

- forever and ever...

----------

Instead, we need to *remember* the value of the varying parameter, which is `y`.

Now, our variables need to be global because we need to *remember* their values from one iteration of draw to another.

Actually, in this scenario, only `y` needs to be global as others remain the same, but that would mean we can't make changes later on.

What if I need the shape to go left/right? Yes, it will be `x` that I vary.
What if I want the shape to becomes smaller/bigger? It will be `diameter`.

So we keep all relevant variables global.

`x` and `y` need to be declared global but cannot be assigned the right value until size executes. So - 

> *Global Declaration, Local Initialization*

Finally, we get our answer:

```processing
float x;
float y;
float diameter = random(50, 100);
float radius = diameter/2;
float angle1 = 2.25*PI;
float angle2 = 2.75*PI;
void setup() {
  size(600, 400);
  //once we know size, we can assign values to x, y
  x = width/2;
  y = height/2;
  background(255);
}
void draw() {
  background(255);
  noStroke();
  fill(0, 0, 255);
  rectMode(CENTER); //this means instead of top-left corner, we specify the center x and center y, applies to square too
  square(x, y, diameter); //create a bounding box around the circle, to be drawn over the square
  fill(255, 0, 0);
  circle(x, y, diameter);
  //to understand the following calculations, read this: https://processing.org/tutorials/trig
  float onCircleX1 = x + radius*cos(angle1);
  float onCircleY1 = y + radius*sin(angle1);
  float onCircleX2 = x + radius*cos(angle2);
  float onCircleY2 = y + radius*sin(angle2);
  fill(0, 255, 0);
  triangle(x, y, onCircleX1, onCircleY1, onCircleX2, onCircleY2);
  
  y = y - 1;
}
```

It is incredibly easy it is to change the varying aspect here.


Instead of,

```processing
y = y - 1;
```

try, 

```processing
angle1 = angle1 + 0.01; 
angle2 = angle2 + 0.01; 
```

and see what happens. It's pretty neat (we think!)

Now you know how to move complex shapes/actors/characters around.