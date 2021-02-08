---
title: Square Covering Variations
description: An odd number of $ m \times n $ rectangles is placed on an infinite grid, such that any two may overlap. Show that there are at least $ mn $ small $ 1 \times 1 $ grid squares that are covered by an odd number of rectangles.
ogDescription: An odd number of m by n rectangles is placed on an infinite grid, such that any two may overlap. Show that there are at least mn small 1 by 1 grid squares that are covered by an odd number of rectangles.
date: 2020-12-28T11:09:28+02:00
tags: [parity, coloring, infinity]
draft: false
---

This page contains variations of the [square covering parity](../square-covering-parity) riddle. You should read it before continuing.

### Rectangles
There are a few things that the proof did not require (hence we can generalize it). 
For example, we never _really_ used the fact that we are describing square.
The riddle can be easily described for rectangles:

An odd number of $ m \times n $ rectangles is placed on an infinite grid, such that any two may overlap.
Show that there are at least $ m \times n $ small $ 1 \times 1 $ grid squares that are covered by an odd number of squares.

Here's an animation of an example, alongside the code:

{{< video "RectangleExample" >}}

```python
from manim import *

class Example(Scene):
    def construct(self):
        # Create 2x3 rectangles
        one   = Rectangle(fill_opacity=0.5, height=2, width=3, color=WHITE, fill_color=WHITE)
        two   = Rectangle(fill_opacity=0.5, height=2, width=3, color=BLUE, fill_color=WHITE)
        three = Rectangle(fill_opacity=0.5, height=2, width=3, color=RED, fill_color=WHITE)

        # Move 2x3 rectangles to position
        # Notice that rectangles are created with their center on the origin so we do the following
        # Align left edge to the x = 0 line
        one.align_to(ORIGIN, LEFT)
        two.align_to(ORIGIN, LEFT)
        three.align_to(ORIGIN, LEFT)
        # Align bottom edges to the y = 0 line
        one.align_to(ORIGIN, DOWN)
        two.align_to(ORIGIN, DOWN)
        three.align_to(ORIGIN, DOWN)

        two.shift(DOWN+2*LEFT)
        three.shift(LEFT)

        # Show the rectangles
        self.play(ShowCreation(one))
        self.play(ShowCreation(two))
        self.play(ShowCreation(three))
        
        # All grid 1x1 squares which an odd number of squares cover
        # Everything is relative to the center of the first square which is the origin
        odd_positions = [
            2*RIGHT,
            2*RIGHT+UP,
            DOWN,
            DOWN+LEFT,
            DOWN+2*LEFT,
            2*LEFT,
            LEFT+UP,
            ORIGIN,
        ]

        # Show a yellow square in each odd position
        for position in odd_positions:
            show_odd = Square(side_length=1, fill_opacity=0.7, color=YELLOW)

            # Move to position
            show_odd.align_to(ORIGIN, LEFT)
            show_odd.align_to(ORIGIN, DOWN)

            show_odd.shift(position)
            self.play(ShowCreation(show_odd))
```

The solution directly follows.

### $ \mathbb R $

An interesting follow-up to the original question shows we can find the same bound for the area covered if we can place our rectangles (or squares) anywhere on the grid.
Here's the question:

An odd number of $ m \times n $ rectangles is placed on an infinite grid such that a rectangle may be between two gridlines.
Show that the area of the points which are covered by an odd number of rectangles is at least $ m \times n $.

As it turns out, we can solve this riddle without thoroughly understanding the definition of an area (for example, the area of $ \mathbb Q ^ 2 $ - the rational points, is 0).
Here's a fun animation (got you surprised this time, didn't I?) to demonstrate:

{{< video "RExample" >}}

```python
from manim import *

class Example(Scene):
    def construct(self):
        # Create 2x3 rectangles
        one   = Rectangle(fill_opacity=0.5, height=2, width=3, color=WHITE, fill_color=WHITE)
        two   = Rectangle(fill_opacity=0.5, height=2, width=3, color=BLUE, fill_color=WHITE)
        three = Rectangle(fill_opacity=0.5, height=2, width=3, color=RED, fill_color=WHITE)

        # Move 2x3 rectangles to position
        # Notice that rectangles are created with their center on the origin so we do the following
        # Align left edge to the x = 0 line
        one.align_to(ORIGIN, LEFT)
        two.align_to(ORIGIN, LEFT)
        three.align_to(ORIGIN, LEFT)
        # Align bottom edges to the y = 0 line
        one.align_to(ORIGIN, DOWN)
        two.align_to(ORIGIN, DOWN)
        three.align_to(ORIGIN, DOWN)

        two.shift(np.pi/2*DOWN+np.e*LEFT)
        three.shift(math.sqrt(np.e)*LEFT)

        # Show the rectangles
        self.play(ShowCreation(one))
        self.play(ShowCreation(two))
        self.play(ShowCreation(three))

        # I found no better way than brute force to do this (at least we have align_to)
        # but manim is fun nontheless :D
        r1 = Rectangle(fill_opacity=0.7, fill_color=YELLOW, height=2, width=math.sqrt(np.e))
        r1.align_to(three, RIGHT)
        r1.shift(math.sqrt(np.e) * RIGHT)
        r1.align_to(one, DOWN)

        self.play(ShowCreation(r1))

        r2 = Rectangle(fill_opacity=0.7, fill_color=YELLOW, height=np.pi/2, width=math.sqrt(np.e))
        r2.align_to(three, LEFT)
        r2.align_to(two, DOWN)
        r2.shift(2*UP)

        self.play(ShowCreation(r2))

        r3 = Rectangle(fill_opacity=0.7, fill_color=YELLOW, height=np.pi/2, width=3)
        r3.align_to(two, LEFT)
        r3.align_to(two, DOWN)

        self.play(ShowCreation(r3))

        r4 = Rectangle(fill_opacity=0.7, fill_color=YELLOW, height=(2 - np.pi/2), width=(np.e - math.sqrt(np.e)))
        r4.align_to(two, LEFT)
        r4.align_to(two, UP)

        self.play(ShowCreation(r4))

        r5 = Rectangle(fill_opacity=0.7, fill_color=YELLOW, height=(2 - np.pi/2), width=(3 - np.e))
        r5.align_to(ORIGIN, LEFT)
        r5.align_to(ORIGIN, DOWN)

        self.play(ShowCreation(r5))
```