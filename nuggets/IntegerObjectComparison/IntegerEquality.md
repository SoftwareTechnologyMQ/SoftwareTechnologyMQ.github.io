The output of `IntegerEquality.java` is:

```
-250,-250 are DIFFERENT using ==
-129,-129 are DIFFERENT using ==
-128,-128 are SAME using ==
-127,-127 are SAME using ==
126,126 are SAME using ==
127,127 are SAME using ==
128,128 are DIFFERENT using ==
250,250 are DIFFERENT using ==
-250,-250 are SAME using .equals
-129,-129 are SAME using .equals
-128,-128 are SAME using .equals
-127,-127 are SAME using .equals
126,126 are SAME using .equals
127,127 are SAME using .equals
128,128 are SAME using .equals
250,250 are SAME using .equals
```

Integer objects in the range [-128, 127] can be compared using ==. Integer objects outside this range cannot.

Nice summarization by "Eugene" on [StackOverflow](https://stackoverflow.com/questions/10285573/comparing-the-values-of-two-integers) -

*"...caches Integers from 0 to 127 and creates new instance for values higher then 127, hence == comparison returns false."*
