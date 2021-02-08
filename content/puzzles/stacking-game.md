---
title: "Stacking Game"
description: You have $ n $ boxes organized in a circle, where each box contains a ball. You are only allowed to move two balls to adjacent boxes in opposite directions (clockwise and counter-clockwise). Given $ n $, determine if you can move all the balls to a single box.
description: You have n boxes organized in a circle, where each box contains a ball. You are only allowed to move two balls to adjacent boxes in opposite directions (clockwise and counter-clockwise). Given n, determine if you can move all the balls to a single box.
date: 2021-02-04T00:20:28+02:00
tags: [invariance, modulus]
draft: false
---

You have $ n $ boxes organized in a circle, where each box contains a ball. You are only allowed to move two balls to adjacent boxes in opposite directions (clockwise and counter-clockwise). Given $ n $, determine if you can move all the balls to a single box.

## Solution

Let us take a closer look at $ n = 2 $. 

{{< video "Two" >}}

Sadly, we are stuck! 
How about $ n = 3 $?

{{< video "Three" >}}

Hurray. After you think about it for a bit, you might indeed try to do the same for all odd $n$'s, for example:

{{< video "Seven" >}}

Here's another somewhat pleasing visual for $ n = 13 $:
{{< video "ThirteenFast" >}}

Here's the code
```python
from typing import List
from manim import *


class Two(Scene):
    def construct(self):
        dots = [
            Dot().shift(RIGHT),
            Dot().shift(LEFT),
        ]

        self.play(*[ShowCreation(dot) for dot in dots])

        self.play(
            ClockwiseTransform(dots[0], dots[1].copy()),
            ClockwiseTransform(dots[1], dots[0].copy()),
        )

        self.wait()

        self.play(
            CounterclockwiseTransform(dots[0], dots[1].copy()),
            CounterclockwiseTransform(dots[1], dots[0].copy()),
        )


class Odd(Scene):
    n = 7

    def construct(self):
        dots_by_angle: dict[float, List[Dot]] = {}
        for i in range(self.n):
            dots_by_angle[i] = [Dot().shift(rotate_vector(RIGHT, 2 * PI * i / self.n))]

        self.play(*[ShowCreation(dot[0]) for dot in dots_by_angle.values()])

        middle = int((self.n - 1) / 2)

        for i in range(middle - 1):
            angle = 2 * PI * i / self.n
            new_angle = angle + 2 * PI / self.n
            other = 2 * PI - angle - 2 * PI / self.n
            new_other = other - 2 * PI / self.n
            animations = []

            count = len(dots_by_angle[i])
            for index, dot in enumerate(dots_by_angle[i]):
                animations.append(
                    CounterclockwiseTransform(
                        dot,
                        Dot().move_to(
                            rotate_vector(
                                RIGHT * ((count - index - 1) / 2 + 3 / 2), new_angle
                            )
                        ),
                    )
                )

            animations_two = []
            count = len(dots_by_angle[self.n - i - 1])
            for index, dot in enumerate(dots_by_angle[self.n - i - 1]):
                animations_two.append(
                    ClockwiseTransform(
                        dot,
                        Dot().move_to(
                            rotate_vector(
                                RIGHT * ((count - index - 1) / 2 + 3 / 2), new_other
                            )
                        ),
                    )
                )

            count = len(animations)
            for i in range(count):
                self.play(animations[count - i - 1], animations_two[count - i - 1])

            dots_by_angle[i + 1] += dots_by_angle[i][::-1]
            dots_by_angle[self.n - i - 2] += dots_by_angle[self.n - i - 1][::-1]
            dots_by_angle[i] = []
            dots_by_angle[self.n - i - 1] = []

        animations = []
        animations_two = []
        count = len(dots_by_angle[middle - 1])
        for index, dot in enumerate(dots_by_angle[middle - 1]):
            animations.append(
                CounterclockwiseTransform(
                    dot,
                    Dot().move_to(
                        rotate_vector(
                            RIGHT * ((count - index - 1) / 2 + 3 / 2), 2 * PI * middle / self.n
                        )
                    ),
                )
            )
        for index, dot in enumerate(dots_by_angle[middle + 1]):
            animations_two.append(
                ClockwiseTransform(
                    dot,
                    Dot().move_to(
                        rotate_vector(
                            RIGHT * ((count - index - 1) / 2 + 5 / 4), 2 * PI * middle / self.n
                        )
                    ),
                )
            )
        count = len(animations)
        for i in range(count):
            self.play(animations[count-i-1], animations_two[count-i-1])
        self.wait()

        animations = []
        for dots in dots_by_angle.values():
            for dot in dots:
                animations.append(
                    dot.animate.shift(
                        rotate_vector(
                            4 * RIGHT * ((middle + 2) / 2), 2 * PI * middle / self.n
                        )
                    )
                )
        self.play(*animations)
```