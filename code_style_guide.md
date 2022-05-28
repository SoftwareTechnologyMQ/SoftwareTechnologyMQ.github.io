---
layout: page
title: Code Style Guide
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge</summary>

  * [Primitive Operations](./primitive_operations)
  * [Variables](./variables)
  * [Conditions](./conditions)
  * [Loops](./loops)
  * [Functions](./functions)
  * [Arrays](./compound_data)
</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes</summary>

  * Name your variables suitably
  * Lay out your code well
  * Comment well
  * Further understand the need to delegate (readability)

</details>

# Code style guideline 

## 1. Indentation and variable-naming

### PICK A STYLE

Choose between one of the following and stick to it throughout your program.

- Java-style indentation + variable naming convention, OR, 
- C-style indentation + variable naming convention, 


### FUNDAMENTAL RULE

The three control structures are:

1. Conditions
2. Loops
3. Functions

You go forward/to the right (a tab or 4 spaces) when you enter a control structure.

### Java-style indentation

#### Conditions

```java
if(exp) {
	//if body
}
```

```java
if(exp) {
	//if body
}
else {
	//else body
}
```

## Example of good indentation:

```java
int a = 10, b = 20;
if(a%2 == 0) {
	a++;
	b--;
}
else {
	if(b%2 == 0) {
		b++;
		a--;
		if(a == b) {
			a = b;
		}
	}
}
```

## Example of bad indentation (1):

```java
int a = 10, b = 20;
if(a%2 == 0) {
a++;
b--;
}
else {
	if(b%2 == 0) {
		b++;
a--;
		if(a == b) {
		a = b;
			}
	}
}
```

## Example of bad indentation (2):

```java
int a = 10, b = 20;
if(a%2 == 0) {
	a++;
		b--;
	}
	else {
		if(b%2 == 0) {
			b++;
				a--;
				if(a == b) {
					a = b;
						}
							}
								}
```


#### Loops

```java
while(exp) {
	//loop body
}
```

```java
for(init; exp; update) {
	//loop body
}
```

## Example of good indentation:

```java
for(int i=0; i < 10; i++) {
	int a = 200;
	while(a > 10) {
		if(a%2 == 0) {
			counter++;
		}
		else {
			counter+=2;
		}
		a/=2;
	}
	for(int k=a; k > 1; k--) {
		counter*=2;
	}
}
```

## Example of bad indentation:

```java
for(int i=0; i < 10; i++) {
 int a = 200;
 while(a > 10) {
		if(a%2 == 0) {
		 counter++;
		}
		else {
		 counter+=2;
		}
		a/=2;
	}
	for(int k=a; k > 1; k--) {
			counter*=2;
	}
}
```

#### Function
```java
returnType funtionName(<parameters>) {
	//function body
}
```

## Example of good indentation:

```java
int mystery(int[] a) {
	int count = 0;
	
	//one blank line to separate logical sections, if needed
	for(int i=0; i < a.length; i++) {
		for(int k=i+1; k < a.length; k++) {
			if(a[i] == a[k]) {
				count++;
			}
		}
	}
	
	//again, at most one blank line
	return false;
}
```

## Example of decently-indented code with minor mistakes:

```java
int mystery(int[] a) {
	int count = 0;
	
	//one blank line to separate logical sections, if needed
	for(int i=0; i < a.length; i++) {
		for(int k=i+1; k < a.length; k++) {
			if(a[i] == a[k]) {
			count++; //this is not at the right indentation level
			}
		}
	}
	
	//again, at most one blank line
	return false;
}
```

Example of poorly-indented code:

```java
int mystery(int[] a) {


	//what's with all the extra emptylines!?


	for(int i=0; i < a.length; i++) {
	 for(int k=i+1; k < a.length; k++) {
		if(a[i] == a[k]) {
		 			return true;
				}
				}
		}
		return false;
}
```

#### Variable-naming

- camelCased
- finals are ALL\_UPPERS

Examples:

```java
boolean isHit = true; //if that doesn't drive the message home, nothing will
final int COUNT_SQUARES = 5;
```

### C-style indentation

#### Conditions

```java
if(exp) 
{
	//if body
}
```

```java
if(exp) 
{
	//if body
}
else 
{
	//else body
}
```

#### Loops

```java
while(exp) 
{
	//loop body
}
```

```java
for(init; exp; update) 
{
	//loop body
}
```

#### Function
```java
return type funtion(parameters) 
{
	//function body
}
```

#### Variable-naming

- Underscore-separated / snake_case
- finals are ALL\_UPPERS

Examples:

```java
boolean is_hit = true;
final int COUNT_SQUARES = 5;
```

## 2. Good variable names

Variables must convey their purpose clearly.
Variables must not be too short/ too long.

Examples of good variable names:

```java
boolean isHit = true;
int nStudents = 15;
double angle = Math.PI/2;
```

Examples of poor variable names (even if commented to indicate purpose):

```java
int totoro = 15; //a represents number of students

//you will be reported to the faculty if any code/comment is offensive
boolean f_u = true; 

double ngl = Math.PI/2;
```

## 3. Commenting

- Comments should be clear and within the screen. 
- Multi-line comments should be immediately before the code to which they relate.

Example:

```java
//assuming val is a floating-point number
/*
 * a holds the rounded-off value
 * by adding 0.5, any value which is of the form x.y,
 * where y < 0.5, will stay as x.z, thereby in the same
 * integer range. however, any value of the form x.y,
 * where y >= 0.5, will translate to (x+1).z, 
 * where z < 0.5, jumping to the next integer range.
 * Then we cast it to intger, to get x or x+1
 */
int a = (int)(val+0.5);
```

- Single-line comments, when they relate to a statement, should be at the end of the statement to which they relate.

```java
//assuming val is a floating-point number

int a = (int)(val+0.5); //a holds val casted to nearest integer
```

Note: this is the version where the reader isn't concerned with the underlying math.

- Over-commenting is bad!

Examples (over-commenting):

```java
int a = 10; 
a++; //increment a by 1
if(a < 10) { //if a is less than 10
	a/=2; //half it
}
```

- Commenting should explain the logic.

For example, for a code that reverses an array:

```java
for(int i=0, k=data.length-1; i < data.length/2; i++, k--) {
	int temp = data[i];
	data[i] = data[k];
	data[k] = temp;
}
```

Following comments would be useful:


```java
/*
 * We swap first item with the last,
 * second item with the second-last,
 * ...
 * item to the left of "middle line" with item to the right of the "middle line"
 */
for(int i=0, k=data.length-1; i < data.length/2; i++, k--) {
	int temp = data[i]; 
	data[i] = data[k];
	data[k] = temp;
}
```

The code to swap two variables is trivial at our level and need not be commented.

## Samples of submission

### Code (1) that is good in terms of indentation and commenting

```java
/*
	to determine if point (x, y) is inside the rectangle
	defined by top left corner at (minX, minY) and 
	bottom right corner at (maxX, maxY), 
	I will perform bound checking.
*/

boolean inside = false; //by default we'll assume it's outside

if(x >= minX && x <= maxX) {
	if(y >= minY && y <= maxY) {
		inside = true; //override because within bounds on both axes
	}
}
```

Note, we didn't comment the condition headers because the variable names make it self-explanatory.
		
### Code (1) that is NOT good in terms of indentation and commenting

```java
boolean inside = false;
if(x >= minX && x <= maxX) { //x is between minX and maxX
	if(y >= minY && y <= maxY) { //y is between minY and maxY
		inside = true; //update inside to true
	}
}
```

The comments on lines with conditional header are redundant.		

### Code (2) that is good in terms of indentation and commenting

```java
boolean allUnique(int[] data) {
	/*
		the logic of my design and implementation is to
		compare each item in the array with every OTHER
		item (not itself), and returning false as soon
		as two items at different indices are the same 
		in their value
	*/

	if(data == null) { //to avoid NullPointerException
		return false;
	}
	
	for(int i=0; i < data.length; i++) { //pivot item
		/*
			compare pivot item against all items AFTER
			it (indiated by k=i+1) since by comparing
			an item A against another item B that is after it,
			we have compared B against A as well, and
			therefore don't need to do it again
		*/
		for(int k=i+1; k < data.length; k++) {
			if(data[i] == data[k]) {
				return false;
			}
		}
	}
		
	/*
		the only way we can reach this control flow point
		is if no two items were the same
	*/
	return true;
}	
```

### Code (2) that is not good in terms of indentation, or commenting

The comments are fairly redundant in this example.

```java
boolean allUnique(int[] data) {
	if(data == null) { //if data is null
		return false;
	}
	
	for(int i=0; i < data.length; i++) { //for each item
	  	for(int k=i+1; k < data.length; k++) 
	  	{ 
		if(data[i] == data[k]) { //if they are equal
				return false;
		}
		}
	}
	
	return true;
}	
```

### Code (1) that is good in terms of delegation

```java
void setup() {
  size(600, 600);
  int x = width/3;
  int y = height/3;
  int dia = 100;
  drawHuman(x, y, dia);
}

void drawHuman(int x, int y, int dia) {
  strokeWeight(2);
  drawTorso(x, y, dia);
  drawLegs(x, y, dia);
  drawArms(x, y, dia);
  drawHead(x, y, dia);
}

void drawArms(int x, int y, int dia) {
  line(x, y+dia, x-dia, y+dia*.5);
  line(x, y+dia*1.1, x-dia, y+dia*.5);

  line(x, y+dia, x+dia, y+dia*.5);
  line(x, y+dia*1.1, x+dia, y+dia*.5);
}

void drawLegs(int x, int y, int dia) {
  line(x, y+dia*2, x-dia/2, y+dia*3);
  line(x, y+dia*1.8, x-dia/2, y+dia*3);

  line(x, y+dia*2, x+dia/2, y+dia*3);
  line(x, y+dia*1.8, x+dia/2, y+dia*3);
}

void drawTorso(int x, int y, int dia) {
  line(x, y, x, y+dia*2);
}

void drawHead(int x, int y, int dia) {
  drawHeadOutline(x, y, dia);
  drawEyes(x, y, dia);
  strokeWeight(2);
  drawNose(x, y, dia);
  drawMouth(x, y, dia);
}

void drawEyes(int x, int y, int dia) {
  strokeWeight(dia*.2);
  point(x - dia/4, y - dia/4);
  point(x + dia/4, y - dia/4);
}

void drawHeadOutline(int x, int y, int dia) {
  circle(x, y, dia);
}

void drawNose(int x, int y, int dia) {
  line(x, y-dia/10, x + dia/8, y+dia/10);
  line(x + dia/8, y+dia/10, x - dia/8, y+dia/10);
}

void drawMouth(int x, int y, int dia) {
  line(x - dia/5, y + dia/5, x + dia/5, y + dia/5);
  line(x - dia/5, y + dia/5, x - dia/4, y + dia/6);
  line(x + dia/5, y + dia/5, x + dia/4, y + dia/6);
}
```

### Code (1) that is NOT good in terms of delegation

```java
void setup() {
  size(600, 600);
  int x = width/3;
  int y = height/3;
  int dia = 100;

  strokeWeight(2);
  line(x, y+dia, x-dia, y+dia*.5);
  line(x, y+dia*1.1, x-dia, y+dia*.5);

  line(x, y+dia, x+dia, y+dia*.5);
  line(x, y+dia*1.1, x+dia, y+dia*.5);
  line(x, y+dia*2, x-dia/2, y+dia*3);
  line(x, y+dia*1.8, x-dia/2, y+dia*3);

  line(x, y+dia*2, x+dia/2, y+dia*3);
  line(x, y+dia*1.8, x+dia/2, y+dia*3);
  line(x, y, x, y+dia*2);
  strokeWeight(2);
  circle(x, y, dia);
  line(x, y-dia/10, x + dia/8, y+dia/10);
  line(x + dia/8, y+dia/10, x - dia/8, y+dia/10);
  line(x - dia/5, y + dia/5, x + dia/5, y + dia/5);
  line(x - dia/5, y + dia/5, x - dia/4, y + dia/6);
  line(x + dia/5, y + dia/5, x + dia/4, y + dia/6);
  strokeWeight(dia*.2);
  point(x - dia/4, y - dia/4);
  point(x + dia/4, y - dia/4);
}
```

### Code (2) that is good in terms of delegation (but not in terms of commenting)

```java
boolean isAlphabetic(String str) {
	if(str == null) {
		return false;
	}	
	
	for(int i=0; i < str.length(); i++) {
		if(!isAlphabet(str.charAt(i)) {
			return false;
		}
	}
	return true;
}

boolean isAlphabet(char ch) {
	if(isUpperCaseAlphabet(ch) || isLowerCaseAlphabet(ch)) {
		return true;
	}
	else {
		return false;
	}
}

boolean isUpperCaseAlphabet(char ch) {
	if(ch >= 'A' && ch <= 'Z') {
		return true;
	}
	else {
		retunr false;
	}
}

boolean isLowerCaseAlphabet(char ch) {
	if(ch >= 'a' && ch <= 'z') {
		return true;
	}
	else {
		retunr false;
	}
}
```

### Code (2) that is NOT good in terms of delegation

It does too many things in the same function

```java
boolean isAlphabetic(String str) {
	if(str == null) {
		return false;
	}	
	
	for(int i=0; i < str.length(); i++) {
		if((str.charAt(i) < 'a' || str.charAt(i) > 'z') &&
			(str.charAt(i) < 'A' || str.charAt(i) > 'Z')) {
			return false;
		}
	}
	return true;
}
```


### Code (1) that is good in terms of variable names

```java
float eyeCenterX = width/2;
float eyeCenterY = height/2;
float eyeWidth = width * 0.8;
float eyeHeight = height * 0.5;
float retinaDiameter = height * 0.4;

ellipse(eyeCenterX, eyeCenterY, eyeWidth, eyeHeight);
fill(0);
circle(eyeCenterX, eyeCenterY, retinaDiameter);
```

### Code (1) that is NOT good in terms of variable names

```java
float x = width/2;
float y = height/2;
float w = width * 0.8;
float h = height * 0.5;
float dia = height * 0.4;

ellipse(x, y, w, h);
fill(0);
circle(x, y, dia);
```

### Code (2) that is good in terms of variable names

```java
boolean distance(float x1, float y1, float x2, float y2) {
	float distanceX = abs(x1-x2);
	float distanceY = abs(y1-y2);
	float distanceBetweenPoints = sqrt(distanceX*distanceX + distanceY*distanceY);
	return distanceBetweenPoints;
}
```

### Code (2) that is NOT good in terms of variable names

```java
boolean distance(float x1, float y1, float x2, float y2) {
	float a = abs(x1-x2);
	float b = abs(y1-y2);
	float c = sqrt(a*a + b*b);
	return c;
}
```

# Refactoring and debugging

While refactoring and debugging, it's easier if you spread out your logic across multiple statements rather than have it all in one convoluted statement.

For example, the following condition header checks if the String `str` contains `keyPhrase` (case-insensitive).

```java
if(str.toLowerCase.indexOf(keyPhrase) >= 0`) {
	//...
}
```

However, it's doing too many things in one statement and it's difficult to identify, which part, if any, is buggy.

Instead, you can spread it across several statements, so you can inspect the status at each step.

```java
String lower = str.toLowerCase();
int firstIndex = lower.indexOf(keyPhrase);
boolean found = firstIndex >= 0;
if(found) {
	//...
}
```

# Miscellaneous tips

- It's good to have debugging print statements in the code but they should be remove (not just commented out) in the production code or the final code submitted for code style inspection.