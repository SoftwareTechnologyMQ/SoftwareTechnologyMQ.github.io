---
layout: page
title: Python File I/O
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge</summary>
  * [Python basics](python_cheat_sheet)
</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes</summary>

  * Be able to open a file for reading
  * Be able to write to a file
  * Be able to navigate a file structure

</details>

# Author: Gaurav Gupta

# File reading

Reading a file is perhaps the simplest of operations when it comes to File I/O.

There are a couple of ways to open a file for reading:

## 1. open

```python
f = open(<file to open>, "r")
<do something with f>
```

Example:

```python
f = open("input.xml, "r")
<do something with f>

g = open("C:\Documents\index.html", "r")
<do something with g>

h = open("usr/gauravgupta/grades.csv", "r")
<do something with h>
```

## 2. with - as - open

The advantage of opening files in this way is to not have to flush and close them (in case of write mode).

```python
with open(<file to open>, "r") as f:
	<do something with f>
```

Example:

```python
with open("input.xml", "r") as f:
	<do something with f>

with open("index.html", "r") as g:
	<do something with g>
	
with open("usr/gauravgupta/grades.csv", "r") as h:
	<do something with h>
```

We will continue using the second method from now on.

# Reading data from file opened

There are three main functions using which we can read data from files:

1. `read()`: returns the contents of entire file as a string.
2. `readline()`: returns the contents up to a newline character.
3. `readlines()`: returns a list of different lines in the file.

Say the file contents of file `data.txt` are:

```
This is a sample file.
It contains many sentences.
This being the last one.
```

## read()

```python
with open("data.txt", "r") as f:
	print(f.read())
```

Output:

```
This is a sample file.
It contains many sentences.
This being the last one.
```

## readline()

```python
with open("data.txt", "r") as f:
	print("Line:",f.readline())
	print("Line:",f.readline())
	print("Line:",f.readline())
```

Output:

```
Line: This is a sample file.
Line: It contains many sentences.
Line: This being the last one.
```

Reading the whole file line-by-line like this is possible, but awkward.

## readlines()

```python
with open("data.txt", "r") as f:
	lines = f.readlines()
	for line in lines:
		print("Line:",line)
```

Output:

```
Line: This is a sample file.
Line: It contains many sentences.
Line: This being the last one.
```

Of course, we can cut out the middle-person and reduce it to:

```python
with open("data.txt", "r") as f:
	for line in f.readlines():
		print("Line:",line)
```

## Easiest way to read line-by-line

After seeing those three ways, the easiest way to read a file line-by-line is using an iterator, and is given below:

```python
myfile = open("data.txt", "r")
for line in myfile:
    print(line)
```

## Handling headers

You can ignore header line or lines using the `next()` function.

Example is shown below:

Say the file `grades.csv` is:

```
StudentID, 	Grade

40404040, 		90
41234567,		60
41729000,		70
```

We would like to ignore the first two lines since the first line is the header and second line is blank.

Output:

```
Line: 40404040,  	90
Line: 41234567,		60
Line: 41729000,		70
```

You can store the data in a list or dictionary or whichever collection is most suitable.


```python
with open('grades.csv', 'r') as f:
	records = {}
	next(f) # ignore first line
	next(f) # ignore second line
	for line in f:
		line = line.strip()
		tokens = line.split(',')
		for i in range(len(tokens)):
    			tokens[i] = int(tokens[i].strip())
		# the above processing can also be done using the following:
		# tokens = [int(item.strip()) for item in line.strip().split(',')]
		records[tokens[0]] = tokens[1] # add to dictionary
	print(records)
```

Output (`records`):

```
{40404040: 90, 41234567: 60, 41729000: 70}
```

More compact (albeit complex) version of the same program:

```python
with open('grades_file.csv', 'r') as f:
	records = {}
	lines = f.readlines()[2:] # skip first two lines
	for line in lines:
		tokens = [int(item.strip()) for item in line.strip().split(',')]
		records[tokens[0]] = tokens[1] # add to dictionary
	print(records)
```

# File Writing

You open a file for writing the same way you open it from reading - using the `open` function, except that you use `"w"` mode.

Careful! Opening a file in write-mode overwrites the file, without any prompts.

```python
with open(<file to open for writing>, "w") as f:
	<write to file>
```

Example:

```python
with open("file.txt", "w") as f:
    f.write("Hi!\n")
    f.write("Nice to meet you :)\n")
    f.write("Bye!\n")
    # Can also use:
    # f.write("Hi!\nNice to meet you :)\nBye!\n");
```

We don't need to explicitly call the `close()` method. It is handled behind the scenes.

Contents of `file.txt` after the code is executed:

```
Hi!
Nice to meet you :)
Bye!
```

You can also open a file in append-mode by using `"a"` as the mode. Assuming `file.txt` already contains the three lines above, the following code will result in a fourth line appended to it.

```python
with open("file.txt", "a") as f:
    f.write("DONE.\n")
```

Contents of `file.txt` after the code is executed:

```
Hi!
Nice to meet you :)
Bye!
DONE.
```

# A practical example

Say, we have a csv file that holds student grades. We can read the file, store the data in a collection, perform analysis, and then output filtered information to a file. 

# Complete example: 
# [example\_python\_file\_io.zip](./assets/codes/COMP6010/example_python_file_io.zip)