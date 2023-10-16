---
layout: page
title: Stacks and Queues
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge</summary>

  * <a href="functions">Functions</a>
  * <a href="compound_data">Compound Data (Arrays)</a>
  * <a href="classes_types">Classes as Data Type</a>
  * <a href="classes_methods">Classes (Methods)</a>
  * <a href="lists">ArrayLists</a>
</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes</summary>

  * Understand the scenarios in which stacks and queues are useful
  * Able to implement stacks and queues
</details>

## Author: Gaurav Gupta

## Entire code from this page is available in [stacksQueues.zip](./assets/codes/stacksQueues.zip).

- To use these in Eclipse, create a java project from scratch and copy the files into the `src` folder.
- To use these in VS Code, unzip and open the folder.

# Abstract Data Types (ADT)

- ADT is a way of thinking about a data structure
- Can be implemented in different ways
- Might have different performance properties
- Support the same interface (add, remove, get)

# Stacks and Queues

- Two ADTs that are really lists with more restricted interfaces
	- **Stack**: add items to, and remove items from, the top. This is known as **Last In First Out** (*LIFO*). 
	- **Queue**: add things to the back, remove from the front. This is known as **First In First Out** (*FIFO*).

# Motivation

Before we get into the details. . .

- Why would you have a type that is more restricted?
- Why would you prevent me doing things with my data?

The reason for the restrictions is two fold. From the perspective of the user of the type, having a restricted interface makes sense for certain algorithms. We’ll see that Stack and Queue work well for some useful algorithms - we could do the same with a List but it’s better to use the abstract data type that fits the algorithm.

From the point of view of the implementer of the ADT, having a more restricted interface means that I might be able to optimise the implementation of the ADT for these operations. So if I only ever want to add to the front of a Stack or Queue I can use a data structure that is optimised for that operation but poor for random access.

# Stack

- A stack is a data structure where elements are added and removed from the top - Called a LIFO data structure: *Last In First Out*.
- Basic operations: `push`, `pop`, `peek`.
- `push` adds a new item to the top of the stack
- `pop` removes the top item from the stack and returns it - peek returns the top item without removing it
- `isEmpty` returns `true` if the stack is empty, `false` otherwise.

## Stack operation examples

Operations, and stack status after the operation, are provided below:

- `push(10)`
	- 10 
- `push(20)`
	- 20 10 
- `peek()` returns 20 
	- 20 10  
- `push(5)`
	- 5 20 10
- `push(11)`
	- 11 5 20 10 
- `push(3)`
	- 3 11 5 20 10 
- `pop()` returns 3
	- 11 5 20 10 
- `pop()` returns 11
	- 5 20 10 	

What is the effect of `push(pop())`? What about `push(peek())`?

<details>
<summary>Answer</summary>
`push(pop())` has no effect since we are removing one item and then putting it right back. 
`push(peek())` will duplicate the top item on the stack.
</details>

## Implementing Stack using ArrayList

We can implement a stack in a variety of ways - using arrays, ArrayList, recursive data structures (that we will study soon).

Here, we present a very simple implementation using `ArrayList` class, so that Java takes care of all the re-sizing complexities.

The contents of the stack are kept in an `ArrayList`.


```java
import java.util.ArrayList;

public class MyStack {
	public ArrayList<String> items;
	
	public MyStack() {
		items = new ArrayList<String>();
    }
}
```

The method `push` requires a `String` that it adds to the beginning (interpreted as *top*) of the ArrayList.


```java
public void push(String item) {
    items.add(0, item);
}
```

The method `isEmpty` returns `true` if Stack is empty, `false` otherwise.


```java
public boolean isEmpty() {
    return items.isEmpty();
}
```

The method `pop` removes and returns the top item, if any, and returns `null` if Stack is empty.


```java
public String pop() {
   if(isEmpty()) {
       return null;
   }
   else {
       return items.remove(0);
   }
}
```

Finally, a `toString` method so we can display the Stack.


```java
public String toString() {
    return items.toString();
}
```

Putting it all together,


```java
import java.util.ArrayList;

public class MyStack {
	public ArrayList<String> items;
	
	public MyStack() {
		items = new ArrayList<String>();
    }
    
    public void push(String item) {
        items.add(0, item);
    }
    
    public boolean isEmpty() {
        return items.isEmpty();
    }
    
    public String pop() {
        if(isEmpty()) {
            return null;
        }
        else {
            return items.remove(0);
        }
    }
    
    public String toString() {
        return items.toString();
    } 
}
```

A client that uses our `MyStack` class:

```java
public class Client {
    public static void main(String[] args) {
        MyStack stk = new MyStack();
        stk.push("my young padawan");
        stk.push("you must have");
        stk.push("patience");
        System.out.println(stk);

        stk.pop();
        stk.push("something to eat");
        System.out.println(stk);
    }
}
```

## Using a Stack

- Stacks are at the core of computing.
- Many algorithms make use of stacks to store data as they run
Stacks – **Undo**.
- The **Undo** operation in your editor uses a stack.
- Each operation that changes the text is pushed on the stack.
- To undo we pop the operation from the stack and reverse it.

## Balanced Parentheses

- To check whether parentheses are balanced in an expression (or program) - Reading through the expression left-to-right
- When I see an open parenthesis (`(` or `{` or `[`), I push it to the stack
- When I see a close parenthesis (`)` or `}` or `]`), I ensure it matches with the last open bracket and if so, I pop the stack.
- At the end, the stack should be empty.

### Example 1

```
(()())))
```

1. Open round bracket means `push('(')`: Stack = `(`
2. Open round bracket means `push('(')`: Stack = `(, (`
3. Close round bracket means check if not empty and then for match, which passes, and `pop()`: Stack = `(`
4. Open round bracket means `push('(')`: Stack = `(, (`
5. Close round bracket means check if not empty and then for match, which passes, and `pop()`: Stack = `(`
6. Close round bracket means check if not empty and then for match, which passes, and `pop()`: Stack = empty
7. Close round bracket means check if not empty which fails, and hence invalid.

### Example 2

```
(]{}[]
```

1. Open round bracket means `push('(')`: Stack = `(`
2. Close **square** bracket means check if not empty and then for match, which fails, and hence invalid

### Example 3

```
(([{}]))
```

This will pass as every closing bracket matches with the top of the stack opening bracket (which is then popped).

```java
public static boolean isBalanced(String brackets) {
	MyStack stk = new MyStack();
	String opening = "([{";
	String closing = ")]}";
	for(int i=0; i < brackets.length(); i++) {
		char cur = brackets.charAt(i);
		if(opening.indexOf(cur)>=0) { //if it's an opening bracket
			stk.push(cur+""); //remember, ours is a stack that holds Strings
		}
		else if(closing.indexOf(cur)>=0) { //closing bracket
			if(stk.isEmpty()) { //no matching opening bracket
				return false;
			}
			String popped = stk.pop();
			if(opening.indexOf(popped) != closing.indexOf(cur)) { //not a match
				return false;
			}
		}
		else { //some other character
			return false;
		}
	}
	return stk.isEmpty(); //only if stack is empty
}
```
		

## Reverse Polish Notation

- Arithmetic expressions where the operator comes **AFTER** the operands. We will assume a space as a delimitor. The benefit of RPN expressions is that we don't need brackets to enforce priority.

- `3 + 4` becomes **`3 4 +`**.
- `5 + 6` becomes **`5 6 *`**.
- `17 - 29` becomes **`17 29 -`**.
- `92 / 71` becomes **`92 71 /`**.
- 3 + 4 * 5
	- First convert `4 * 5` to RPN: **`4 5 *`**.
	- Intermediate expression becomes `3 + ` **`4 5 *`**. 
	- Now, convert it to RPN: **`3 4 5 * +`**. 
- (3 + 4) * 5 will become **`3 4 + 5 *`**.

## Evaluating RPN

The process to evaluate a valid RPN stored in a String is very simple. We assume only 4 operators `+, -, *, /`. 

1. Start from the left.
2. If the next (space-delimited) item is a number, push it onto the stack.
3. If the next item is an operator, pop the two values from the stack, apply the operation, and push the result back onto the stack. Important:
	- For division, it's `second-from-top item` / `top item`. 
	- For subtraction, it's `second-from-top item` - `top item`.

### Example 1:

```
2 4 + 7 2 - /
```

1. Item = 2, Stack = `2.0`
2. Item = 5, Stack = `4.0 2.0`
3. Item = +, Stack = `6.0`
4. Item = 7, Stack = `7.0 6.0`
5. Item = 2, Stack = `2.0 7.0 6.0`
6. Item = -, Stack = `5.0 6.0`
7. Item = /, Stack = `1.2`

### Example 2:

```
5 2 / 6 3 - *
```

1. Item = 5, Stack = `5.0`
2. Item = 2, Stack = `2.0 5.0`
3. Item = /, Stack = `2.5`
4. Item = 6, Stack = `6.0 2.5`
5. Item = 3, Stack = `3.0 6.0 2.5`
6. Item = -, Stack = `3.0 2.5`
7. Item = *, Stack = `7.5`

## Code for evaluating RPN

Just a small variation of our `MyStack` class for this example:

```java
import java.util.ArrayList;

public class MyNumberStack {
    public ArrayList<Double> items;

    public MyNumberStack() {
        items = new ArrayList<Double>();
    }

    public void push(Double item) {
        items.add(0, item);
    }

    public boolean isEmpty() {
        return items.isEmpty();
    }

    public Double pop() {
        if (isEmpty()) {
            return null;
        } else {
            return items.remove(0);
        }
    }

    public String toString() {
        return items.toString();
    }
}
```

```java
public class MyNumberStackClient {

    public static void main(String[] args) {
        String s = "3 6 4 - /";
        System.out.println(evaluate(s));

        s = "3 6 4 - / 7 *";
        System.out.println(evaluate(s));
    }

    public static boolean isOperation(String s) {
        return s.length() == 1 && "+-*/".indexOf(s) >= 0;
    }

    public static Double evaluate(String rpn) {
        String[] tokens = rpn.split(" ");
        MyNumberStack stk = new MyNumberStack();
        for (int i = 0; i < tokens.length; i++) {
            if (isOperation(tokens[i])) { // operator
                if (stk.isEmpty()) { // first operand not there
                    return null;
                }
                double top = stk.pop();
                if (stk.isEmpty()) { // second operand not there
                    return null;
                }
                double secondFromTop = stk.pop();

                // apply the right operation and push it back
                if (tokens[i].equals("+")) {
                    stk.push(secondFromTop + top);
                }
                if (tokens[i].equals("-")) {
                    stk.push(secondFromTop - top);
                }
                if (tokens[i].equals("*")) {
                    stk.push(secondFromTop * top);
                }
                if (tokens[i].equals("/")) {
                    stk.push(secondFromTop / top);
                }
            } else {
                stk.push(Double.parseDouble(tokens[i])); // we assume it's a number
            }
        }
        double top = stk.pop();
        if (stk.isEmpty()) {
            return top;
        } else {
            return null; // something left on the stack
        }
    }
}
```

# Queues

Queues are **First-In-First-Out** (*FIFO*) data structure. The overall structure is very similar to stacks.

An example is provided below, and the client is in `MyQueueClient.java` in the zip file linked at the top.

```java
import java.util.ArrayList;

public class MyQueue {
    public ArrayList<String> items;

    public MyQueue() {
        items = new ArrayList<String>();
    }

    public void insert(String item) {
        items.add(item); // insert at the back
    }

    public boolean isEmpty() {
        return items.isEmpty();
    }

    public String remove() {
        if (isEmpty()) {
            return null;
        } else {
            return items.remove(0); // remove from the front
        }
    }

    public String toString() {
        return items.toString();
    }
}
```
