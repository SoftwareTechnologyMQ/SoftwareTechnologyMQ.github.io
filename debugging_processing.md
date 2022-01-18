---
layout: page
title: Debugging in Processing
within: programming
---

<iframe src="https://player.vimeo.com/video/140134398" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
<p><a href="https://vimeo.com/140134398">Processing 3 Debugger</a> from <a href="https://vimeo.com/processingfoundation">Processing Foundation</a> on <a href="https://vimeo.com">Vimeo</a>.</p>

<div class="task" markdown="1">
Consider the program you wrote in to [animate a blue circle](./variables.html#animated_blue_circle).  At the start of the program, it will have the value `0` and after one animation frame it will get a new value, what is that value?  After another frame, it gets another new value, what is that value?  Using the debugger, write down the first 40 values that are given to the variable `ypos`.
<details class="solution" markdown="1"><summary>solution</summary>
`ypos` will get the values `0`, `1`, `2`, `3`, through to `38`, and `39`.  The values keep going up, these are just the first 40 values.
</details>
</div>

<iframe width="560" height="315" src="https://www.youtube.com/embed/G9uDQBoHp08?list=PLRqwX-V7Uu6aFNOgoIMSbSYOkKNTo89uf" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<div class="task" markdown="1">
Use the console to _print out_ the value of `ypos` as the code from your animated blue circle is executing.  What happens to the values when the blue circle is off the screen?
<details class="solution" markdown="1"><summary>solution</summary>
A single new line is added at the start of the `draw` function that will "report" the current value in the `ypos` variable everytime an animation frame is drawn.

~~~~~
int ypos;

void setup(){
  ypos = 0;
}

void draw(){
  println(ypos);
  background(255);
  noStroke();
  fill(92, 136, 218);
  circle(width/2, ypos, 20);

  ypos++;
}
~~~~~

When the circle has gone off the bottom of the screen nothing changes!  The variable keeps going up, but the place where it will be drawn is not visible to us anymore.
</details>
</div>
