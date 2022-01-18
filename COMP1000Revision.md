# REVISION OF COMP1000 CORE CONCEPTS 

This document covers the core components of introductory programming using Java programming language. Note that COMP1000 is taught using Processing, which is Java in disguise. 

We retain concepts common to Processing and Java and ignore Processing-specific concepts like `mousePressed` or `draw()` or `setup()` or for that matter, any animation-related topics.

COMP1010 is very much numerical in nature, in that, it's taught using numbers. This is because EVERYTHING can be translated to numbers - images, videos, databases, etc. So once you learn how to process a collection of numbers, everything else just builds on top. Also, I like numbers.

Questions marked with ^**CORE** make a significant impact on subsequent learning.

## Variables

1. Which one of the following is/are valid literals?
	1. chicken_LEGS
	2. COMP1000
	3. 1stOneIn
	4. #hashtag
	5. why?
	6. chicken-LEGS

2. What is the value of `n` when the following code executes?

	```java
	int n = 17/5;
	``` 

3. ^**CORE** What is the value of `n` when the following code executes? Note `double` is the preferred floating-point data type in Java (as opposed to `float` in Processing)

	```java
	double n = 17/5;
	``` 
	
4. What is the value of `n` when the following code executes?

	```java
	double n = 17/5.0;
	``` 

5. What is the value of `flag` when the following code executes?

	```java
	boolean flag = (5 > 3) && (6 == 2);
	``` 

6. ^**CORE** What is the value of `flag` when the following code executes?

	```java
	boolean flag = true || true && false;
	```	
	
## Boolean expressions

