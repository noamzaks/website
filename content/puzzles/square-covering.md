---
title: Square Covering
description: An odd number of $ n \times n $ squares is placed on the integer points of an infinite grid, such that any two may overlap. Show that there are at least $ n^2 $ small $ 1 \times 1 $ grid squares that are covered by an odd number of squares.
ogDescription: An odd number of n by n squares is placed on the integer points of an infinite grid, such that any two may overlap. Show that there are at least n squared small 1 by 1 grid squares that are covered by an odd number of squares.
date: 2020-12-28T11:09:28+02:00
tags: [parity, coloring]
preview: "Example"
draft: false
---

An odd number of $ n \times n $ squares is placed on the integer points of an infinite grid, such that any two may overlap. Show that there are at least $ n^2 $ small $ 1 \times 1 $ grid squares that are covered by an odd number of squares.

First, let's create an animations showing this for $ n = 3 $:
{{< video "Example" >}}

The code looks like so:

```python
from manim import *

class Example(Scene):
    def construct(self):
        # Create 3x3 squares
        one   = Square(fill_opacity=0.5, side_length=3, color=WHITE, fill_color=WHITE)
        two   = Square(fill_opacity=0.5, side_length=3, color=BLUE, fill_color=WHITE)
        three = Square(fill_opacity=0.5, side_length=3, color=RED, fill_color=WHITE)

        # Move 3x3 squares to position
        two.shift(2*DOWN+LEFT)
        three.shift(RIGHT)

        # Show the squares
        self.play(ShowCreation(one))
        self.play(ShowCreation(two))
        self.play(ShowCreation(three))

        # All grid 1x1 squares which an odd number of squares cover
        # Everything is relative to the center of the first square which is the origin
        odd_positions = [
            LEFT,
            LEFT+UP,
            2*RIGHT+UP,
            2*RIGHT,
            2*RIGHT+DOWN,
            2*DOWN,
            3*DOWN,
            3*DOWN+LEFT,
            3*DOWN+2*LEFT,
            2*DOWN+2*LEFT,
            DOWN+2*LEFT,
            2*DOWN+LEFT,
            DOWN
        ]

        # Show a yellow square in each odd position
        for position in odd_positions:
            show_odd = Square(side_length=1, fill_opacity=0.7, color=YELLOW)
            show_odd.move_to(position)
            self.play(ShowCreation(show_odd))
```

### Solution

The puzzle can be solved like so. Pick some position and color an $ n \times n $ grid in $ n $ different colors.

Then, copy that coloring to each direction, and continue until you've colored the entire plane.
The coloring can be defined like so:

$ f(x,y) = (x \mod n, y \mod n) $

This means that two squares $ (a,b), (x,y) $ share a color if $ a = x + kn $ for some $ k \in \mathbb Z $ and $ b = y + tn $ for some $ t \in \mathbb Z $.

Now, notice that each color is covered an odd number of times, hence there is a $ 1 \times 1 $ square of that color which is covered an odd number of times, because if every square of that color was covered an even number of times, the total would be even.

Because each color has a square covered an odd number of times, and there are $ n^2 $ colors, it follows that we found $ n^2 $ squares covered by an odd amount of squares.

Now let's code an animation demonstrating this solution for $ n = 3 $.
{{< video "Solution" >}}

The code for the above:

```python
from manim import *

class Solution(Scene):
    def construct(self):
        # We can't draw the entire plane, but let's color a 9x9 grid.
        colors = [
            [ORANGE, RED, BLUE],
            [TEAL, GREEN, YELLOW],
            [GOLD, PURPLE, MAROON]
        ]
        # We want to show all 81 animations at once
        animations = []
        # and keep our grid
        grid = []

        for i in range(9):
            row = []
            for j in range(9):
                FACTOR = 0.75
                square = Square(fill_opacity=0.7, color=colors[i % 3][j % 3], stroke_width=0, side_length=FACTOR)
                square.shift(FACTOR * (i * RIGHT + j * UP - 4*(RIGHT + UP))) # Move everything so it is centered.
                row.append(square)
                animations.append(ShowCreation(square))
            grid.append(row)

        self.play(*animations)

        # Create 3x3 squares
        one   = Square(fill_opacity=0.5, side_length=3 * FACTOR, color=WHITE, fill_color=WHITE)
        two   = Square(fill_opacity=0.5, side_length=3 * FACTOR, color=BLUE, fill_color=WHITE)
        three = Square(fill_opacity=0.5, side_length=3 * FACTOR, color=RED, fill_color=WHITE)

        # Move 3x3 squares to position
        two.shift(FACTOR*(2*DOWN+LEFT))
        three.shift(FACTOR*(RIGHT))

        # Show the squares
        self.play(ShowCreation(one))
        self.play(ShowCreation(two))
        self.play(ShowCreation(three))

        # Hide all squares which aren't colored some color
        animations = []
        for i in range(9):
            for j in range(9):
                if not (i % 3 == 0 and j % 3 == 0):
                    animations.append(FadeOut(grid[i][j]))
        self.play(*animations)

        # Hide all squares but the one which is covered only by the red 3x3 square
        animations = []
        for i in range(9):
            for j in range(9):
                if (i % 3 == 0 and j % 3 == 0) and not (i == 6 and j == 3):
                    animations.append(FadeOut(grid[i][j]))
        self.play(*animations)
```

Some variations of this puzzle are examined (and animated of course) over [here](../square-covering-parity-variations).

### Notes

- If all squares are exactly in the same position, we get exactly $ n^2 $ squares covered by an odd number of squares, meaning this is the best lower bound.
- Notice in the solution video, the darker blue color appears 3 times covered by an odd number of squares. As you might guess, there can be only an odd number of blue squares covered by an odd number of squares (because if there was an even amount, the total would again be even).
