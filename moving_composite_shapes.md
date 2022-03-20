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

## Author: Gaurav Gupta

All the codes in this page are provided at [movingCompositeShapesCode.zip](./assets/codes/movingCompositeShapesCode.zip). 

A second version is also available at at [movingCompositeShapesCodeTrigonometryVersion.zip](./assets/codes/movingCompositeShapesCodeTrigonometryVersion.zip).

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
size(600, 400); //change to 100, 100 and see what happens
background(255);

rectMode(CENTER); //specify center coordinates instead of top-left coordinates
fill(255);
rect(300, 200, 200, 100); 

triangle(300, 200, 200, 150, 400, 150);

noStroke();
fill(200, 0, 0);
circle(300, 200, 25);

fill(50);
textAlign(CENTER, BOTTOM);
textSize(25);
text("Harry Potter", 300, 250);
```

The first problem is that if we want to relocate this shape to another position in the display window, we have to replace each of the `x` and `y` values.


However, if we store the `x` and `y` values in two variables, we only have to change it once in case we change our mind.


```processing
size(600, 400); //change to 100, 100 and see what happens
background(255);

float x = width/2;
float y = height/2;

rectMode(CENTER); //specify center coordinates instead of top-left coordinates
fill(255);
rect(x, y, 200, 100); 

triangle(x, y, x-100, y-50, x+100, y-50);

noStroke();
fill(200, 0, 0);
circle(x, y, 25);

fill(50);
textAlign(CENTER, BOTTOM);
textSize(25);
text("Harry Potter", x, y + 50);
```

### Magic numbers

This draws a triangle on a circle on a square. But that dimensions:

- `200` and `100` in `rect`, 
- `100` and `50` in `triangle`, 
- `25` in `circle`, and, 
- `50` in `text`

are hard-coded values, we call *magic numbers*. (As in, appearing magically).

To make the program scalable, we need to fix that. So we identify diameter, and then radius is always going to be half of that.

```processing
size(600, 400); //change to 100, 100 and see what happens
background(255);

float x = width/2;
float y = height/2;
float envelopeWidth = width/3;
float envelopeHeight = envelopeWidth/2;
float sealDiameter = envelopeHeight/4;

rectMode(CENTER); //specify center coordinates instead of top-left coordinates
fill(255);
rect(x, y, envelopeWidth, envelopeHeight); 

triangle(x, y, x-envelopeWidth/2, y-envelopeHeight/2, x+envelopeWidth/2, y-envelopeHeight/2);

noStroke();
fill(200, 0, 0);
circle(x, y, sealDiameter);

fill(50);
textAlign(CENTER, BOTTOM);
textSize(sealDiameter);
text("Harry Potter", x, y + envelopeHeight/2);
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

  background(255);

  float x = width/2;
  float y = height/2;
  float envelopeWidth = width/3;
  float envelopeHeight = envelopeWidth/2;
  float sealDiameter = envelopeHeight/4;

  rectMode(CENTER); //specify center coordinates instead of top-left coordinates
  fill(255);
  stroke(0);
  rect(x, y, envelopeWidth, envelopeHeight); 
  
  triangle(x, y, x-envelopeWidth/2, y-envelopeHeight/2, x+envelopeWidth/2, y-envelopeHeight/2);

  noStroke();
  fill(200, 0, 0);
  circle(x, y, sealDiameter);

  fill(50);
  textAlign(CENTER, BOTTOM);
  textSize(sealDiameter);
  text("Harry Potter", x, y + envelopeHeight/2);
}
```

## Trying to update state with local variables

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

Instead, we need to *retain* the value of the varying parameter, which is `y`.

Now, our variables need to be global because we need to *retain* their values from one iteration of draw to another.

Actually, in this scenario, only `y` needs to be global as others remain the same, but that would mean we can't make changes later on.

What if I need the shape to go left/right? Yes, it will be `x` that I vary.
What if I want the shape to becomes smaller/bigger? It will be `envelopeWidth `, `envelopeHeight` and `sealDiameter`.

So we keep all relevant variables global.

`x`, `y` and `envelopeWidth` depend on `width` and `height` and therefore need to be declared global but cannot be assigned the right value until size executes. 

`envelopeHeight` and `sealDiameter` then depend on `envelopeWidth ` so they are assigned values after `envelopeWidth` is assigned the right value.

> *Global Declaration, Local Initialization*

Finally, we get our answer:

```processing
float x;
float y;
float envelopeWidth;
float envelopeHeight;
float sealDiameter;

void setup() {
  size(600, 400);
  //once we know size, we can assign values to x, y, envelopeWidth
  x = width/2;
  y = height/2;
  envelopeWidth = width/3;

  /*
  and only after we know envelopeWidth, 
   can we assign values to envelopeHeight, sealDiameter
   */
  envelopeHeight = envelopeWidth/2;
  sealDiameter = envelopeHeight/4;

  background(255);
}

void draw() {
  background(255);

  rectMode(CENTER); //specify center coordinates instead of top-left coordinates
  fill(255);
  stroke(0);
  rect(x, y, envelopeWidth, envelopeHeight); 
  
  triangle(x, y, x-envelopeWidth/2, y-envelopeHeight/2, x+envelopeWidth/2, y-envelopeHeight/2);
  
  noStroke();
  fill(200, 0, 0);
  circle(x, y, sealDiameter);
  
  fill(50);
  textAlign(CENTER, BOTTOM);
  textSize(sealDiameter);
  text("Harry Potter", x, y + envelopeHeight/2);
  
  /*
  and finally update the aspect that needs updating
  here we move up, so y will decrease.
  
  if you want to expand the envelope, envelopeWidth will increase.
  but in that case, you will need to re-calculate envelopeHeight, sealDiameter
  */
  
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
x = x - 1;
```

and see what happens. 

You can also change the dimensions of the shape but in this case, you have to be careful.

If you only add the following, the envelope's height and seal's diameter won't change.

```processing
envelopeWidth = envelopeWidth + 1;
```

If you increase all three by 1, the *shape* will be lost.

```processing
envelopeWidth = envelopeWidth + 1;
envelopeHeight = envelopeHeight + 1;
sealDiameter = sealDiameter + 1;
```

What you need to do is to increase `envelopeWidth` and calculate the others based on it.

```processing
envelopeWidth = envelopeWidth + 1;
envelopeHeight = envelopeWidth/2;
sealDiameter = envelopeHeight/4;
```

Now you know how to move complex shapes/actors/characters around.