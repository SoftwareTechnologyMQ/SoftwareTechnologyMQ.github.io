---
layout: page
title: Introduction to Regular Expressions
---

Regular expressions, or regex, is used to identify patterns in a text. In this tutorial we will focus on regex in python, but during your degree you may see it in multiple languages such as javascript and scala.

## Syntax
Before starting, here's a list of useful special characters in Python's regex library to refer back to.
* `.` - any character except newline.
* `\n` - new line.
* `\s` - white space.
* `\t` - tab.
* `\d` - digit.
* `^` - the start of a string or line.
* `$` - the end of a string or line.
* `*` - repeats the previous character 0 or more times.
* `*?` - repeats the previous character 0 or more times (non-greedily).
* `+` - repeats the previous character 1 or more times.
* `+?` - repeats the previous character 1 or more times (non-greedily).
* `[abc]` - will match one of the characters in the set.
* `[^abc]` - will match any character not in the set.
* `[a-z]` - will match any character between `a` and `z` (inclusive).
* `a|b` - matches either a or b.
* `{n}` - matches exactly n occurrences.
* `{m,n}` - matches as many as possible of m to n occurrences.

## Getting started
To use regex in python you'll need to use the [re](https://docs.python.org/3/library/re.html) library. There's also a [regex](https://pypi.org/project/regex/) library but it's not yet needed. To find all the occurrences of a pattern you can use `re.findall()`, but to also get the location of those matches, `re.finditer()` is useful.

```py
import re

str = "Using regex for the first time"

match = re.findall('e', str)
print(match)

for m in re.finditer('i.', str):
    print(m) # Match object, position, match
```
Running the above code in python returns
```py
['e', 'e', 'e', 'e']
<re.Match object; span=(2, 4), match='in'>
<re.Match object; span=(21, 23), match='ir'>
<re.Match object; span=(27, 29), match='im'>
```

## Match a collection
The `[...]` sign will match any character inside it while  `[^...]` will match any character not inside it.
```py
import re

str = "H0w 0ur m1nds c4n d0 4m4z1ng 7h1ng5!"
match = re.findall('[mwn]', str)
print(match)
# if we want to match lower case letters instead
match = re.findall('[a-z]', str)
print(match)
# The above expression won't match the 'H', space and '!'
# To get them, match everything except the numbers
match = re.findall('[^0-9]', str)
print(match)
```
Running the above code in python returns
```py
['w', 'm', 'n', 'n', 'm', 'n', 'n']
['w', 'u', 'r', 'm', 'n', 'd', 's', 'c', 'n', 'd', 'm', 'z', 'n', 'g', 'h', 'n', 'g']
['H', 'w', ' ', 'u', 'r', ' ', 'm', 'n', 'd', 's', ' ', 'c', 'n', ' ', 'd', ' ', 'm',
 'z', 'n', 'g', ' ', 'h', 'n', 'g', '!']
```

## Match repeating characters
The `+` character can be used to match 1 or more occurrence while `*` matches 0 or more occurrences. They are both greedy unless directly followed by a `?`.

```py
import re

str = "The given student ids are 46125656, 87654321, 46464321, 46561256"
match = re.findall('[0-9]+', str)
print(match)
# Ending in 56
match = re.findall('[0-9]+56', str)
print(match)
# Ending in 56 (non-greedy)
match = re.findall('[0-9]+?56', str)
print(match)
# Matches 0 or more occurrences of the numbers before 56
match = re.findall('[0-9]*?56', str)
print(match)
```
Running the above code in python returns
```py
['46125656', '87654321', '46464321', '46561256']
['46125656', '46561256']
['461256', '4656', '1256']
['461256', '56', '4656', '1256']
```

## Exercises
This [link](https://regex101.com/) can be helpful to debug your code.
1. Find all the occurrences of `b`. Example sentence: *he made a bad bid for the bed*.
2. Find all the occurrences of the word `ever`. Example sentence: *We are never, ever, ever, ever getting back together. Make sure not to include everyone*.
3. Find all the occurrences of any of the characters in the word `ever`. Example sentence: *We are never, ever, ever, ever getting back together. Make sure not to include everyone*.
4. Find all the occurrences of the phrase `ev` or `re`. Example sentence: *We are never, ever, ever, ever getting back together. Make sure not to include everyone*.
5. Find all occurrences of substrings starting with `b` and ending with `d`. Example sentence: *Abid made a baaad bid for the bed and got hit in the abdomen*.
6. **Advanced:** Find all words in a text. The text can contain multiple sentences ending in one of `!?.`. Only words containing letters from the English alphabet should be included.
