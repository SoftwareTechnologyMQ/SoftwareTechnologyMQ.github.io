---
layout: page
title: Classes - UML Notation
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge:</summary>

  * [Classes](./classes_types)

</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes:</summary>

  * Understand Unified Modeling Language class diagrams and object diagrams.

</details>

## Author: Gaurav Gupta

# UML

Unified modeling language is used to visually convey the design of a system. In our cases, classes and objects.

We will only look at the aspects that concern us.

## Class diagram

Consider the class definition:

```java
class Rectangle {
	public int length, breadth;

	public Rectangle(int len, int bre) {
		length = len;
		breadth = bre;
	}

	public int area() {
		return length * breadth;
	}

	public boolean isSquare() {
		return length == breadth;
	}

	public void resize(double factor) { //assume factor>=0
		length*=factor;
		breadth*=factor;
	}
}
```
