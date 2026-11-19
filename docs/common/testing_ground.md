---
title: Testing Ground
permalink: /common/testing
parent: Common
nav_order: 4
---
<!-- Assumed Knowledge -->
{% capture topic_prereq %}
    * Something you have learnt about
{% endcapture %}
<!-- Learning Outcomes -->
{% capture topic_outcomes %}
    * Something you will learn
{% endcapture %}

{% include prereq_outcomes.html prereq=topic_prereq outcomes=topic_outcomes %}

## Adding SVG files, cleanly

{% comment %}

```
{ % include_relative assets/svgs/sampleSVG.md % }
```

{% include_relative assets/svgs/sampleSVG.md %}

## Using markdown_helper

<!-- Idk -->

@[:markdown](assets/svgs/sampleSVG.md)

@[:code_block](assets/codes/HelloWorld.java)

{% endcomment %}

<!--
better for arrays and functions
Create an array that holds the first 1000 prime numbers (a number is *prime* if it is more than or equal to 2 and is divisible by only 1 and itself).
