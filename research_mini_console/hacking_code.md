---
layout: page
title: "Hacking on Complex Systems"
within: hacking
---

Doing ___real___ work requires working on ___real___ systems and real systems are ___really complex___.

Does that mean we need to spend months learning the system before we can start work? No (thankfully). In fact, it is impossible to become “expert” on any real programmed system, we are all working with imperfect information all the time.

Our entry into complex systems comes from finding a small “chink in the armour” and building from there. In this workshop we will explore strategies for doing that. We will be working with “UniGame”, a prototype RPG created for the Macquarie Mini Console. These same techniques apply to any and all code though, so you can take these skills anywhere.

{: .keypoint}
Combine a high-level “map” with experimentation to build your ability to modify systems.

# UniGame

We've created a complex game so you can practice working with complexity.  You are also welcome to make changes to any other parts of the console, some which are less complex.

UniGame is the start of an RPG about Uni life.  You need to know that directions are "wasd" and "z" is for taking an action.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Isw7J6ylXSA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# The high-level map

Don’t just go in completely blind!

All code is a collection of text files in a set of folders. Get a good tool to show you those files (VSCode is a good choice) and take a look around. Then just “copy out” the file hierarchy. This is the first step of sketching out the map.

Next, work out what parts are uninteresting to you, cross them out and re-do the “map”

Give yourself another 20 mins of poking around, thinking about the names of the files, the types of the files, the way they are organised, and sketch out what you see. You should use your own sketching methods, whatever works for your.

Experienced developers have notational shorthands they like to use, and developers try to use similar notations where they can when communication with each other, but here you are communicating only with yourself so just do what works.

# Experimentation

This is the bulk of the work and there are a number of tools that can help us. Some are built into VSCode, others are on the command line. I will go over each here

## Text

What you see on the screen is rarely represented one-to-one in the code, except for text! In many cases, if you can see some text on the screen that is not user-input, you might be able to find that same piece of text in the code. For example, UniGame begins with “Ok everyone”. That text is somewhere in all those files. If we find it, we might be able to start piecing together how the text display and flow works.

Two tools to help with this are:

  * “Search” (all files): I am sure you are used to searching in a file, but most IDES will let you search all open files at once. The shortcut is usually “Ctrl-Shift-F” or “Cmd-Shift-F”.
  * grep: Grep is a command line version of this with super-powers. Beyond that is ack (grep’s newer brother). Be careful of your “working directory” when using the command line.

{: .task}
Change the opening text to something more impactful.

## Extrapolation from the Map

What if I didn’t like the use of ‘Z’ for progressing? If you try the text strategy above, you will come up empty-handed. But the map you created should have a clue. When I made mine, I had a “KeyPressedManager” in it, which seems like a candidate.

I’m going to need other strategies, but I’m on the right track.

## Blind changes

But even then, the key press manager is not completely obvious.

It looks to me like the numbers on lines 29-35 control something, what can I infer from them? I know that I go left by hitting “w” so is 65 related to “w”?

{: .task}
What happens if you change 65?

## Search strategies

[Lets ask google](https://www.google.com/search?client=firefox-b-d&q=65+related+to+w). Unfortunately, not very helpful. But just adding the programming language you are using can make [all the difference](https://www.google.com/search?client=firefox-b-d&q=65+related+to+w+Java)

{: .task}
Keep a running log of which search strategies work and which don’t.

## More?

As we progress through the workshops, we will collect strategies that have worked, adding them here.