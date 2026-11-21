---
title: Python Introduction
custom-title: Python Introduction, Variables, Operators
permalink: /comp6010/python-introduction
parent: COMP6010
nav_order: 1
---

- TOC
{:toc}

<!-- Assumed Knowledge -->
{% capture topic_prereq %}
  * [Functions]({{ site.baseurl }}/comp1000/functions)

{% endcapture %}
<!-- Learning Outcomes -->
{% capture topic_outcomes %}
  * Install required software
  * Create variables
  * Perform basic arithmetic operations
{% endcapture %}

{% include prereq_outcomes.html prereq=topic_prereq outcomes=topic_outcomes %}



## Installation

1. Install [Python](https://www.python.org/downloads/) (version `3.10.2` at the time of writing these notes). For windows, make sure you add Python to class path.
2. Install [Visual Studio Code](https://code.visualstudio.com/) (or any other IDE of your preference). However, we will only troubleshoot VS Code issues.
3. Inside Visual Studio Code, install the extension [Python by Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

## Write your first program

1. Open Visual Studio Code
2. Click on New
3. Click on File
4. Type the following (without the line number and no leading spaces):

	```python
	print("Hello World!")
	```

5. Save as `my_first_python_program.py`.
6. Click on the Play icon on the top-right side.
7. You should see the output `Hello World!` in the terminal or console.

### History of Python

Python is not named after the non-venomous snakes, but after the acclaimed British comedy show *Monty Python*.

Developed by Guido van Rossum, Python is an interpreted language, and the most widely-used programming language according to TIOBE, as of 18th September, 2024.

