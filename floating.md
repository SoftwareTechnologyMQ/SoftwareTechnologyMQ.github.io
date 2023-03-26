---
layout: page
title: Floating-point arithmetic
within: programming
---
<details class="prereq" markdown="1"><summary>Assumed Knowledge</summary>

  * [Primitive Operations](primitive_operations)
  * [Variables](variables)
</details>

<details class="outcomes" markdown="1"><summary>Learning Outcomes</summary>

  * Truly understand and appreciate the importance of floating-point arithmetic.

</details>

{: .keypoint}
Floating-point arithmetic allows for precision.

{: .readings}

- [https://processing.org/reference/float.html](https://processing.org/reference/float.html)

- [https://processing.org/examples/integersfloats.html](https://processing.org/examples/integersfloats.html)

- Advanced :) [https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html)

## Author: Gaurav Gupta

## Motivation

Over the years, I've had a fair few spirited discussions with colleagues on whether floating-point arithmetic should be given *"screen time"* in first-year programming units, or not. I firmly belong in the camp that advocates its inclusion and promotion.

To prove that future software developers need to understand why floating-point arithmetic is critical, I present the following example with incredibly simple requirements - the two circles must travel at a regular speed, and cross at the centre, irrespective of the size of the display window.

![](./assets/images/laneCrossing.mp4)

Now, if someone can go ahead and write this program using integer arithemtic only, I'll be more than happy to eat some humble pie. Remember, the display window size can be modified from one execution to the other (600 x 400, 601 x 493, 123 x 500, 200 x 107 as some examples).