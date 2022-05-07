---
layout: page
title: Python classes
within: programming
---

<details class="prereq" markdown="1">
<summary>Assumed Knowledge</summary>
  * Variables and Operators in Python
  * Control structures (conditions and loops)
  * Functions
</details>

<details class="outcomes" markdown="1">
<summary>Learning Outcomes</summary>
  * Be acquainted with classes in Python.
</details>

# Author: Gaurav Gupta

# Introduction

A class is a user-defined data type. It's used when something cannot be represented with primitive types (such as `int` or `bool`), and/or, has properties that require specific implementation.

For example, to represent a point in a 2-d coordinate system, you need x and y values. Sure, you can implement it by storing these values in two variables (`x` and `y`) but it means,

1. For the entire program, you need to remember to handle `x` and `y` together.
2. Functions that operate on these values should have both parameters passed, in the correct order.

Instead we *package* both values in one data type - `Point`. Each `Point` *object* has two attributes inside it - `x` and `y`. 


- For `Point a`, the attributes are accessed using `a.x`, `a.y`.
- For `Point b`, the attributes are accessed using `b.x`, `b.y`.

### Defining a class

A class needs to be *defined* only once.

#### Syntax:

```python
class <class_name>:
    attribute_1 = default_value_1
    attribute_2 = default_value_2
    ...
```

#### Example:

```python
class Point:
    x = 0
    y = 0
```

#### Exercise:

Repeat the same process for following classes:

1. `Rectangle`: attributes are `width` and `height`
2. `Person`: attributes are `name`, `age`, `gender`

### Creating objects of a class

Objects of a class are (almost) the same as variables of a type.

#### Syntax:

```python
object_name = class_name()
```

#### Example:

```python
p = Point()
```

#### Exercise:

Repeat the same process for classes `Rectangle` and `Person`, creating objects with names of your choice.

### Accessing attributes of an object

You can access (read/write) attributes of an object by using the dot (`.`) operator.

#### Syntax:

```python
print(object_name.attribute_name)
object_name.attribute_name = value
...
```

#### Example:

```python
print(p.x, p.y)
p.x = 17
p.y = 29
print(p.x, p.y)
```

#### Exercise:

Repeat the same process for classes `Rectangle` and `Person`, assigning values of your choice to the attributes. For `gender`, use one the values from `['Male', 'Female', 'Gender Diverse']`.

### The __init__ function

This is probably the most important function when it comes to classes. Instead of creating an object with default values, you can create objects with the values you want.

#### Syntax:

```python
class class_name:
    def __init__(self, attribute_1, attribute_2, ...):
        self.attribute_1 = attribute_1
        self.attribute_2 = attribute_2
        ...
```

Notice how you don't have to declare the attribytes separately any more. Python infers the attriutes from the parameter list.

#### Example:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

Exercice:

Repeat the same process for classes `Rectangle` and `Person` with the same attributes we have discussed earlier.

### Creating parameterized objects

Once the `__init__` function is defined inside the class, we can create parameterized objects.

#### Syntax:

```python
object_name = class_name(value_for_attribute_1, value_for_attribute_2, ...)
```

#### Example:

```python
p = Point(17, 29)
q = Point(92, 71)
print(p.x,.p.y) # 17 29
print(q.x, q.y) # 92 71
```

Note that if you pass the wrong parameters (insufficient/ excessive), you will get errors.

Example of errors:

```python
p = Point(17) # too few 
q = Point(17, 29, 31) # too many
```

Given that Python is a *dynamically-typed language*, one must also be careful to NOT pass the incorrect type of values as it might cause problems in subsequent code.

Example of no errors but potential problems:

```python
a = Point(17, 29)
a.x+=1 # this is fine

b = Point("Hi", "Bye")
b.x+=1 #this will cause a TypeError
```

#### Exercise:

Repeat the same process for classes `Rectangle` and `Person`, creating objects with names of your choice and attribute values of your choice as well.

### Adding functions inside classes

Any function inside a class automatically has access to the attributes of the instance on which the function is called.

#### Syntax:

```python
class class_name:
    def function_name(self, other_values_besides_attributes):
        function_body
```

#### Example:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_from(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5
```

In the first function `distance_from_origin`, all we need is the calling object, so no parameter besides `self`.

In the second function `distance_from`, we want to calculate the distance between the calling object (`self`) and another object, so we have to provide the second object as the parameter.

#### Exercise:

Repeat the same process for classes `Rectangle` and `Person`, creating functions `area`, `is_square` and `resize(percentage)` in `Rectangle`, and functions `get_first_name` and `can_drink_alcohol(legal_drinking_age)`.

### Calling functions on an object

You call functions on an object the same way you access attributes; using the dot (`.`) operator.

#### Syntax:

```python
object_name.function_name(parameters_besides_self)
```

#### Example:

```python
p = Point(2, 5)
q = Point(8, 3)
print(p.distance_from_origin())
print(q.distance_from(p))
```
        
#### Exercise:

Repeat the same process for classes `Rectangle` and `Person`, calling the functions created in the previous section.

# A complete working example

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_from(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def __eq__(self, other): # used when you compare object1 == object2
        if (isinstance(other, Point)):
            return self.x == other.x and self.y == other.y
        return False
    
    def __str__(self): #called when you display str(object)
        return "("+str(self.x)+", "+str(self.y)+")"

if __name__ == "__main__":
    p = Point(10, 20)
    q = Point(40, 30)
    r = Point(10, 20)

    print("Point p:",str(p))
    print("Point q:",str(q))
    print("Point r:",str(r))
    print("Distance of p from origin: {:.2f}".format(p.distance_from_origin()))
    print("Distance of p from q: {:.2f}".format(p.distance_from(q)))
    print("p same as q?",p == q)
    print("p same as r?",p == r)
```

## Exercise:

Write a complete working example for the following classes (in increasing order of difficulty):

1. `Circle`
2. `Rectangle`
3. `Cuboid` (or `Box`)
4. `Time` (as in time of day)
5. `Date` (as in date of year)
6. `Polygon` (represented by the points on the polygon)