---
title: Demonstration Page
description: A minimal page for demonstrating project features
permalink: /demo
author: Crystal Cheung
nav_exclude: true
use_katex: true
---

This is a hidden page for demonstrating some features of the project.

See the docs/demo.md file for implementation.

All the content is intended to fit inside the main-content-wrap div at whatever width it is. Check how it will look on mobile devices with Inspect mode.

## Titles, Headings and Subheadings

# Title, made with `#`
## Heading 1, made with `##`
### Heading 2, made with `###`
#### Heading 3, made with `####`
##### Heading 4, made with `#####`
###### Heading 5, made with `######`

## Callouts

These can be modified via _config.yml

{: .warning }
> This is a warning.
>
> second paragraph

{: .highlight}
This is a highlight.

{: .note }
note

{: .keynote}
keynote

{: .readings}
Chapter 7 of [Learning Processing](http://learningprocessing.com) by Danel Shiffman.



## Exercises
{% capture my_problem %}
problem
{% endcapture %}

{% capture my_solution %}
solution
{% endcapture %}

{% include exercise.html
    title="Exercise Title"
    problem=my_problem
    solution=my_solution
%}

## Prerequisites and Outcomes as Dropdowns

<!-- Assumed Knowledge -->
{% capture topic_prereq %}
  * Point 1
  * Point 2
{% endcapture %}
<!-- Learning Outcomes -->
{% capture topic_outcomes %}
  * Point 1
  * Point 2
{% endcapture %}

{% include prereq_outcomes.html prereq=topic_prereq outcomes=topic_outcomes %}

## Youtube Videos

{% include youtube.html id="Yw6u6YkTgQ4" %}

## KaTeX

Examples taken from Numbered Systems:

* inline(`$`):

$1101_2$ is a base-2 or binary value.

* block(`$$`):

$$
0 \times n^3 + 1 \times n^2 + 1 \times n^1 + 0 \times n^0 + 1 \times n^{-1} + 0 \times n^{-2} + 1 \times n^{-3}
$$

$$
\begin{aligned}
a^2 + b^2 &= c^2 \\
E &= mc^2 \\
\int_0^\infty e^{-x^2} \, dx &= \frac{\sqrt{\pi}}{2}
\end{aligned}
$$

* inline(`\\(`, `\\)`):

\\(
0 \times n^3 + 1 \times n^2 + 1 \times n^1 + 0 \times n^0 + 1 \times n^{-1} + 0 \times n^{-2} + 1 \times n^{-3}
\\)is a base

\\(
\begin{aligned}
a^2 + b^2 &= c^2 \\
E &= mc^2 \\
\int_0^\infty e^{-x^2} \, dx &= \frac{\sqrt{\pi}}{2}
\end{aligned}
\\)

* block(`\\[`, `\\]`):

\\[
0 \times n^3 + 1 \times n^2 + 1 \times n^1 + 0 \times n^0 + 1 \times n^{-1} + 0 \times n^{-2} + 1 \times n^{-3}
\\]

\\[
\begin{aligned}
a^2 + b^2 &= c^2 \\
E &= mc^2 \\
\int_0^\infty e^{-x^2} \, dx &= \frac{\sqrt{\pi}}{2}
\end{aligned}
\\]

{: .note}
Note that the KaTeX blocks are currently exceeding the width of main-content-wrap. This will be fixed in a later update.

## D3JS

<script src="assets/js/variables-in-memory.js"></script>

<div id="variables-in-memory-animation"></div>






