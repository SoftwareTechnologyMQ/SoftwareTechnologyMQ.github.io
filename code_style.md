---
layout: meta
title: Code-Style Rules
---

Here we explain _why_ we are following the coding styles that we are.

<details markdown = "1"><summary>Java-Style Indenting</summary>
[Details of the this style can be found here](https://en.wikipedia.org/wiki/Indentation_style#Variant:_Java).  The motivation for this style is to have a consistent treatment of _scope_.  It is natural to think of scope starting at an opening brace, but for many constructs the scope actually includes the preceeding parameter declaration and so having these two always on the same line is preferrable.
</details>

<details markdown="1"><summary>No getters/setters</summary>
It is generally considered a good idea to access fields of an object via getters and setters.  However, we don't code this way.  The use of getters/setters is, in fact, a way around a failing of the Object Oriented model.  Since we are teaching the mechanisms of statically typed, class-based OO languages, we prefer to expose the reality of field access rather than hide it.  This has the advantage of reducing the cognitive overhead of learning fields in objects.  NB: The "Practice of Programming" chapter explicitly deals with these OO design issues, they are not ignored, they are quarantined.
</details>
