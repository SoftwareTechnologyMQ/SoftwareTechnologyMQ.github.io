---
layout: page
title: Python lists
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
  * Be able to program with python lists.
</details>

# Author: Gaurav Gupta

## Defintion of a list

A Python *list* is a set of values (not necessarily of the same type, multiple occurrences of an item allowed). In terms of syntax, they are kept in square brackets, and separated by commas. For example,


```python
names = ['Aang', 'Bumi', 'Iroh', 'Katara', 'Sokka', 'Mei Mei', 'Zuko']
print("Characters:\n\t",names)
mixed_bag = [1729, "Guido Van Rossum", True, True, True]
print("Mixed Bag:\n\t",mixed_bag)
```

    Characters:
    	 ['Aang', 'Bumi', 'Iroh', 'Katara', 'Sokka', 'Mei Mei', 'Zuko']
    Mixed Bag:
    	 [1729, 'Guido Van Rossum', True, True, True]


## Number of items and indexing

Number of items in a list (say `myList`) is given by `len(myList)`. List items can be accessed using indices in square brackets. The index of the first item is 0, and the index of the last item is `len(myList)-1`. For example,


```python
print("Number of items:\n\t",len(names))
print("First item:\n\t",names[0])
print("Last item:\n\t",names[len(names)-1])
```

    Number of items:
    	 7
    First item:
    	 Aang
    Last item:
    	 Zuko


## Updating values in a list
Lists are *mutable*, meaning its elements can be changed unlike string or tuple. We can use the assignment operator `=` to change an item or a range of items. For example,


```python
names[0] = 'Ozai'
names[5] = 'Azula'
print(names)
```

    ['Ozai', 'Bumi', 'Iroh', 'Katara', 'Sokka', 'Azula', 'Zuko']


## Getting index of an item

The function `index` gives the index of a particular item. It generates `ValueError` if the item doesn't exist.

The list `index()` function can take a maximum of three arguments:

1. `element` - the element to be searched
2. `start` **(optional)** - start searching from this index
3. `end` **(optional)** - search the element up to this index

For example,


```python
print("Index of 'Katara':\n\t",names.index('Katara'))
print("Index of 'Superman':\n\t",names.index('Superman'))
```

    Index of 'Katara':
    	 3



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Input In [87], in <cell line: 2>()
          1 print("Index of 'Katara':\n\t",names.index('Katara'))
    ----> 2 print("Index of 'Superman':\n\t",names.index('Superman'))


    ValueError: 'Superman' is not in list


## Check before you call index

This is where the `in` and `not in` come in handy. You can check if an item exists (or doesn't exist) in the list with these operations. For example,


```python
if 'Iroh' in names:
    print("Index of 'Iroh':\n\t",names.index('Iroh'))
if 'Amy Santiago' in names:
    print("Index of 'Amy Santiago':\n\t",names.index('Amy Santiago'))
```

## Adding items to list

- Add an item to the end of the list using `append`.
- Add an item AT a given index using `insert`.
- Add multiple items to the end of the list using `extend`.

Examples,


```python
names.append('Mei Mei')
print(names)
names.insert(3, 'Appa')
print(names)
names.extend(['Toph', 'Sukki'])
print(names)
```

## Removing an item from the list

An item is removed by invoking the `remove` function on the list with the item as the parameter. 

**CAREFUL! ValueError is generated if the item you are trying to remove, doesn't exist in the list. So ensure it exists before you try and delete.**

For example,


```python
if 'Ozai' in names:
    names.remove('Ozai')
    print("After removing Ozai:\n\t",names)
if 'Jacob Peralta' in names:
    names.remove('Jacob Peralta')
    print("After removing Jacob Peralta:\n\t",names)
```

## Getting Sub-lists with slicing

You can get the sub-list by *slicing* the list. The syntax is `list_name[start_index : end_index]`. Note that `start_index` is inclusive but `end-index` is exclusive. For example,


```python
print("Original list:\n\t",names)
first_three = names[0:3]
print("Sub-list containing first three names:\n\t",first_three)
last_three = names[len(names)-3:len(names)] #you can also use negative index here
print("Sub-list containing last three names:\n\t",last_three)
print("Original list remains unchanged:\n\t",names)
```

## Creating a large list

You can use *replication* to create a large list with the same value for all the items (or a repeating pattern).

For example,


```python
data = [0] * 20
print("List with 20 zeroes:\n\t",data)
alternating_bits = [0, 1] * 10
print("List with alternating bits:\n\t",alternating_bits)
rgb = ['r', 'g', 'b'] * 5
print("List with primary colour components:\n\t",rgb)

```

## Passing lists to a function

Lists can be passed, just like any other variable, to a function. 
If you modify a list in a function, the actual list passed is also modified.


```python
def remove_first_item(list):
    print("list in function before modifiying:\n\t",list)
    list.remove(list[0]) # remove first item
    print("list in function after modifiying:\n\t",list)

my_list = ['super', 'nintendo', 'chalmers']
print("actual list before calling function:\n\t",my_list)
remove_first_item(my_list)
print("actual list after function finishes:\n\t",my_list)
```

## A few standard function examples with list parameters


```python
def sum(list): #assumes numerical list
    result = 0
    for item in list:
        result+=item
    return result

def count_negatives(list): #assumes numerical list
    count = 0
    for item in list:
        if item < 0:
            count+=1
    return count

def contains_item_in_range(list, low, high): ##assumes numerical list, low <= high
    '''
    Returns True if list contains an item that is in the range [low, high], False otherweise
    '''
    for item in list:
        if item >= low and item <= high:
            return True
    return False

def all_non_empty_items(list): ##assumes a list of strings
    '''
    Returns True if all items of the list have length of at least 1, False otherwise 
    '''
    for item in list:
        if len(item) == 0:
            return False
    return True

def negatives_removed(list): #assumes numerical list
    '''
    Return the passed list, with negative items removed.
    The passed list should NOT be modified
    '''
    result = []
    for item in list:
        if item >= 0:
            result.append(item)
    return result

print("sum of items in list [10, 70, 20, 90]:\n\t",sum([10, 70, 20, 90]))
print("number of negative items in list [-10, -70, 20, -90]:\n\t",count_negatives([-10, -70, 20, -90]))
print("does the list [10, 70, 20, 90] contain any item in the range 50 to 80?:\n\t",contains_item_in_range([10, 70, 20, 90],50, 80))
print("does the list [10, 70, 20, 90] contain any item in the range 75 to 80?:\n\t",contains_item_in_range([10, 70, 20, 90],75, 80))
print("does the list [10, 70, 20, 90] contain any item in the range 0 to 5?:\n\t",contains_item_in_range([10, 70, 20, 90],0, 5))
print("does the list [10, 70, 20, 90] contain any item in the range 150 to 180?:\n\t",contains_item_in_range([10, 70, 20, 90],150, 180))
print("are all the items of list ['medium', 'rare', 'steak'] non-empty?:\n\t",all_non_empty_items(['medium', 'rare', 'steak']))
print("are all the items of list ['medium', '', 'steak'] non-empty?:\n\t",all_non_empty_items(['medium', '', 'steak']))
list = [-10, -70, 20, -90, 30, -80, 40, 60, 0, 0]
print("list without negatives:\n\t",negatives_removed(list))
print("original list unchanged:\n\t",list)

```

    sum of items in list [10, 70, 20, 90]:
    	 190
    number of negative items in list [-10, -70, 20, -90]:
    	 3
    does the list [10, 70, 20, 90] contain any item in the range 50 to 80?:
    	 True
    does the list [10, 70, 20, 90] contain any item in the range 75 to 80?:
    	 False
    does the list [10, 70, 20, 90] contain any item in the range 0 to 5?:
    	 False
    does the list [10, 70, 20, 90] contain any item in the range 150 to 180?:
    	 False
    are all the items of list ['medium', 'rare', 'steak'] non-empty?:
    	 True
    are all the items of list ['medium', '', 'steak'] non-empty?:
    	 False
    list without negatives:
    	 [20, 30, 40, 60, 0, 0]
    original list unchanged:
    	 [-10, -70, 20, -90, 30, -80, 40, 60, 0, 0]

