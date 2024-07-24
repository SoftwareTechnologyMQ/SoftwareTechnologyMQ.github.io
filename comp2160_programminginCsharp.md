---
layout: page
title: "COMP2160 Topic 1"
within: programming
---

<details class="prereq" markdown="1"><summary>Assumed Knowledge</summary>

 * Assumed topic 1
 * Assumed topic 2
 
</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes</summary>

  * LO 1
  * LO 2

</details>

## Author: 


Okay. Welcome to the Week One. Lectures for 21. 60.  this week we'll be talking about just the basics


of unity, scripting and more broadly sort of techniques that


are used in gang video games programming. We'll be breaking this up into short pieces.


 so hopefully they won't be too long for you


to watch in a single city. So basically, unity programming is the three important things you need to know. First of all, that it's an object oriented programming language,


and it uses  C Sharp, which is very similar


to Java.


So this is what we'll talk about in this lecture


is just about the object oriented programming principles behind the sharp. But if you're used to programming in Java, which hopefully you all are having done 125 or 1010,  then you should find the mood, the transition to see shop


fairies,  later videos.


We'll be talking about two other important ideas. That's how unity is component based,  and how unity is event driven. But we'll get into that more in later videos. So C sharp C Sharp is a java like language. It's really very very similar to Java.  in fact, you know you can put pages the sharpener page of Java side by side, and they look almost identical. It's created by Microsoft, and it's based on the dot net framework, and we're looking to spend a lot of time going into the details of C sharp.


Like I said, it's so similar that it shouldn't be.


You shouldn't have too much trouble picking it up The links here for the full C sharp language reference if you want to go into that or the wicked. Wikipedia has a very good and comprehensive list of differences between Java and C sharp, but I just want to


go over a couple of the ones that you're probably


encountering your day to day programming. There are a lot of deep, you know, complicated,  problems the in between the two languages that most programmers


will never actually have to worry about.


Let's give you a couple of examples of the differences


that you might encounter.  so in Java here, if you would you who


you are defining a new class, you would say public class and then the name of your class, you would


say extends And then the name of the class you're


extending. And if you were implementing interfaces, you would say implements in the name, the name of the interface or interfaces that we're using in the shop. Well, you don't have extends or implements. All you have is this colon. It's a public class, my class colon parent class interface. And you just list out any other interfaces here.


 so you can only obviously have one parent class


in there, but you doesn't really require you to sort of explicitly name.


The parent class in the interface is likewise fields the


same public infield. It was one public infield. It was one. It's exactly the same code. The only difference with regard to methods that you're really notice is that the is the naming convention that in C sharp methods begin with a capital letter or, as in Java by standard methods. Begin with a lowercase letter, and this is it won't affect the correctness of your code. You're code will still work if you if you give the methods the different capitalisation.


But like we'll talk about later in this lecture, naming


conventions are really important in making human readable code. Uh and so I will be expecting you to follow the C sharp naming conventions, which should be capitalising the


first letter of your of your method names and using


what's called pastoral case, which is where every new word


you capitalise that letter as well as opposed to this is what's called Camel case because it has a hump in the middle. I guess this is called pastoral case, I guess because


there was a traditional back in the Paschal programming language which was popular in the 19 eighties or some long time ago, um anyway hangs on in in this convention.


So, as you can see, I mean, this is really very similar and you'll find vacuum the transition not very


difficult at all.


 some other examples, some with regard to the basic


types. The enter type is the same.


The bool.


The boolean type is called bool instead of boolean, but otherwise it looks the same. It's still still has the same values are true and false. The float type is the same.


The double type Is this the same immunity?


We almost always use floats rather than doubles. So you need to get used to this syntax of naming your floats with an F on the end. Unity will complain if you don't put an F on the end.


Because by default, the value four point 55 is a


double precision floating point number. And if you want to assign a double position number


to a single precision floating point variable, some information is


going to be lost. And so it will give you an error and asking you Are you sure this is something that you do you want to do? In which case, by putting, Yes, there you say No, this is actually a floating point number. I'm not doing a conversion here.


I am just only working in floating point numbers. Unity uses floating point numbers everywhere.


I'm not sure why they don't use doubles, given that it would give them more precision.


Probably it's a memory management issue.


Anyway, the way that it looks exactly the same from


from C sharp in Java, strings again are the same.


Although Java uses capitalists for strings and C sharp uses lowercase s for strings, otherwise they work the same. And if you put any arrays C sharps is this syntax for declaring an array where you have an agent of and then you have the brackets after the end,


saying this is an array of INTs in Java.


It was possible to do this saying ages and then you put the brackets after ages. You can't do that in C Sharp list is valid syntax for both languages. This is only valid syntax in Java, so it's preferable to use this anyway. In fact, I think this is more readable. This, as ages is an array of ends and declaring the array is exactly the same. Use a new print and the number of things in


their way. So Java.


You might be familiar with the Java API Java API gives you a bunch of built in classes that general useful, including classes for list sets and maps, which you may be familiar with. So this is a list of vintages,  and you


would define it as an array list of vintages, for example, and this is a set of floats. You might. You might assign it a hash set. This is a map you might decided to hash Map. C.


Sharp has its own library, which works similarly and does


a lot of the same sorts of things. But a lot of the names are different, which is kind of annoying. So C Sharp has again has list sense and what's


called dictionaries. Dictionaries are the same as what you call maps in


Java, so a dictionary. You look up a string and it returns afloat. You know, there's just slightly different syntax here. You just have to get used to the new names


if you're using any of these classes in the shop,


one final and possibly more subtle thing.


If you've done a lot of Java programming, you'll get used to the idea of you generally want to make your fields private and then include getters and setters in order to in order to change the values in those fields. The idea behind this, rather than making the field public,


is you can.


If you make it private, then you can control the


assignment of values. For example, if we wanted to set the size of this object and we didn't want to allow size is


less than zero. If we let it made it just public, you can assign a value less than zero and no error would


occur.


Or by using getters and setters, we're able to actually


test the value that were that we want to assign


before we do it. And that code is wrong.


Let me fix that code.


There we go.  so this doesn't let you, you know, we would throw an error in Europe and showed the code, but we could do whatever was necessary to make to make


sure that you couldn't set size to less than zero. This is useful and that it protects the way that


we can set variables, but it gets really clumsy when we start using getting set all over the place. See, Sharp has want to call properties, and so we can have a private field called size, and then we can have a public property called size with the capital letter. So by default site field, start with a lower case letter and properties start with an uppercase letter. They don't have to have the same name, but in this case, it makes sense for them to have the same name.


Um and so here we have the size property, and it has a getter and setter built into it. And so the Guetta returns the private field, which is the same as the get size,  in Java and the setter sets does the aero checking and sets the value, which is the same as the set size. I'm here now.


You may wonder why this is useful. I mean, it's probably a couple more lines code here in C sharp, but where it really shows its value is when you're actually using these encodes, which is in


this example here.


If we make an object of this class and we set the size, properties can be just treated like fields


in assignments so we can do assignments we can do.


We want to set the size to 10. We can just set object dot size equals 10.


What happens when we do this is it calls the set up. The centre will check that this value is rather than equal to zero, and it will set the field appropriately.


And if we want to scale up the size by 2.5, we can just say object of size.


Times equals 25, and this will call together, get the


value multiplied by 2.5 and then call the centre to set the value in Java. If we were going to do this, we have to call, set and get explicitly and which makes much more difficult to read.


Code, right? Um and so this one in particular.


So we call object, get size, would multiply it by 2.5, and then we call object dot said size.


Exactly. The same thing is happening here.


It's just this code is just so much simpler and


easier to read. So this is a nice property in C Sharp. I tend to use properties quite often because they just make your code more readable. So one more difference that you'll come across early commonly is slight differences in how C sharp treats arrays and lists over how they handled in Java.  so, first of all, for for a raise,  we've already said the array the brackets. When you're when you're defining an array, the brackets need to go after the type rather than after the variable name,  assigning things to a raise Exactly the same. However, getting the length of an array is it's a raid at length, but in in C sharp, it's a property, and so it has a capital letter rather than a lower case. L for for a radar length in Java at least, like I've already said you can. There's the list class. You don't have to use the special capital I integer class that you do is you would use in Java if you're creating a list and the add method is the same. But its capital h ad, Because all methods start with the capital letter in In C sharp, However, there's a nice access er for for getting and setting elements of a list.  so rather than having to use the get and set methods in as you would use in Java,  you can just say list zero and both to get the value and to set the value in the same way that you would with an array. So you can basically kind of use the same syntax here for for either a list or an array or as in Java, you would have to say you explicitly call them the get and set methods, which makes your code using lists much. Nita, in my experience, the other weird thing is that where in W would use list dot size to get the number of elements in a list in C sharp, you use list dot count and again, this is a property, not a method. So it's a capital C, but there are no parentheses afterwards.  so you just got to remember that for a raise. It's a raid at length for lists, it's less dot count. But otherwise, you know, again, working with these things is much the same. So, like I said, so Java.


You'll be familiar with the Java API, which defines various


various built in classes to do lots of different things.


Similarly, C Sharp has its own built in API, which is the dot net api, which provides standard classes for


doing, you know, file I o networking mass strings collections. All of these, all of these kinds of things you


want a library for, um turns out we don't need much of it for for doing stuff in unity, because we'll actually be working more with the unity a p I. But there's a link here. If you ever need to use it in particular, probably the ones you use, most commonly the collection so list


sense maps or dictionaries.  maybe you want to use it for Phileo, although


unity generally, you generally end up using the unity methods for Phileo. Maybe you want to use it for some other some other things, some networking or things if we're doing something


advanced, but most of the time you'll be using the


unity api instead. And like I said before, your programmes need to be human, readable as well as computer readable. It's not just enough to make your programmes correct in


terms of the computer can actually execute them and that


they do the right thing. They need to be readable. And this is really important game development, because you'll inevitably would be working on a team of developers. And you need to have consistent style so that everybody is programming in a way that everyone else can read and understand. A very common practise in industry is for the company to have its own style guide, which sets standards for


how they will write their code. And this means that everybody's code looks the same, and


everybody can very easily get used to reading someone else's code. If your code every every piece of code has in the US syncretic naming and formatting, and it just gets hard to understand the code and read it.


 so,  so style guide you will.


You know, if you get a job anywhere, you'll find that they will give you their style guide and say right code according to the style, and you need to get used to being able to do that. And sometimes the style guide will disagree with your personal preferences for how to lay out your code. But really, you just need to suck it up and pay the style guide, because at the end of the day it's often more important than everybody is doing the same thing. Then you're necessarily doing what you think is best for this unit will be using our own C Sharp style guide, which I have published on the on the Island page. So on island, it's here under resource materials, and this


is based on style.


Guide that from the ray window like C sharp style guide, and I'm not going to go through this in detail now. You should make sure you read through this. It has example code and what you should know how you should make your code look naming conventions. You should follow layout conventions. You should follow, etcetera.


I will be marking this, and so you're in your


assignments. You will get a style mark, and that will be based on your ability to follow the style guide. I will be trying my best to follow the style guide myself, if any of my lectures. You notice that I have done something which has disobeyed the style guide. Let me not because it's really important that we that


we maintain a consistent style here so that our code is readable. There's actually some small differences between how I would normally


write code and how and what the style guide says.


This is based on the sort of standard C sharp. There's a fairly universal standards for house.


T H. C Sharp is formatted, and I'm used to a slightly different standards, but I'm going to be trying to write


my code according to the style guide, and you should


be doing the same.


So that's really all for this video.


Like I said, we're not going to go really deep into C sharp programming as we go through the unit. I might highlight some things that that I think you're important or you may not have encountered before. They're really the level of programming you'll be doing in unity. You won't be doing anything that's terribly unusual from what you might have done before.


And all you do need to get used to these few small quirks in terms of writing your code in


C Sharp rather than writing a job in the next lecture will be back into these other properties of unity. We'll look at what we mean by component based programming and what we mean by event driven programming. That's all for now, thank you.
