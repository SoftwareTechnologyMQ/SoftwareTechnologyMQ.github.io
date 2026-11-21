---
layout: page
title: Matching longer Regex expressions
---

## Read and write in Python
To read and write to files in python, you can use the following functions.
```py
def read_file(file_name, encoding='utf-8'):
    file = open(file_name, 'r+', encoding='utf-8')
    content = file.read()
    file.close()
    return content

def write_file(file_name, content):
    f = open(file_name, 'w+', encoding="utf-8")
    f.write(content)
    f.close()
```

## Training with longer regular expressions
As regex is mainly used to find patterns in text, we are going to look at a few different text formats that you can extract information from. Remember to refer back to the examples in the [introduction](./indtroduction.md) page as needed.

### xml file
Here's an [xml file](.\practice_xml.py) containing practice questions from COMP1000 and COMP1010.

1. Find all of the question ids.
2. Find question id's with 4 digits.
3. Find the questions.
4. Find the question texts.
5. Find all answer boxes. Answer boxes are formatted as \{grade:question_type:answer ~ other correct/incorrect answers #possible feedback comment\}.
6. Find all feedback comments inside a valid answer box.
7. Find all correct answer inside a valid answer box. Correct answers start with `=`.

<details class="prereq" markdown="1"><summary>Hint q1 and a2</summary>
The format for questions are &lt;!-- question: ID  --&gt;
</details>
<details class="prereq" markdown="1"><summary>Hint q3</summary>
Find the opening and closing `question` tag. Multiple lines can be matched by using `re.MULTILINE` and `(.|\n)`
</details>
<details class="prereq" markdown="1"><summary>Hint q5</summary>
The first letter in the answer box will always be a digit. `\d` can be used to find this.
</details>

### Python file
Here's a small [python script](.\practice_python.py) for the following questions.

1. Find all function headers.
2. Replace all occurrences of the variable `abc` with  `a_valid_name` in a new file. Use `re.sub()` instead of `str.replace()` since it doesn't recognize regular expressions.

<details class="prereq" markdown="1"><summary>Hint q2</summary>
`re.finditer()` will match the String before you first modify it. So you will need an integer buffer variable to find the difference in position.
</details>

### Java file

### Markdown file

### html file
