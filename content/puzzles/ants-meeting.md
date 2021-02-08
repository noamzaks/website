---
title: "Ants Meeting"
date: 2021-02-08T16:52:57+02:00
draft: false
---

Assume you have $ n $ ants located at some points $ x_n $ along the number line.
At each step, two of the $ n $ ants are chosen to meet each other and they both travel to the middle between them, e.g. $ x_1, x_2 \longrightarrow \frac{x_1 + x_2}{2}, \frac{x_1 + x_2}{2} $. You may even take $ \infty $ steps. What is the maximum total distance which can be achieved?

Here's an example (I'm sticking to points instead of ants) where the ants are in `[-6, 0, 4]` and the meetings are as such `[(0, 2), (0, 1), (1, 2), (0, 1), (1, 2), (0, 1), (0, 2), (1, 2), (0, 2), (0, 1)]` where 0, 1, 2 are the three ants.

{{< video "Example1" >}}

The total distance is around 12 which is suspiciously integer. If, however, the same ants meet in a more 'strategic' matter discussed later, here's another possibility.

{{< video "Example2" >}}

The meetings are `[(1, 2), (0, 2), (0, 1), (1, 2), (0, 1), (1, 2), (0, 1), (1, 2), (0, 1), (1, 2), (0, 1), (1, 2)]`. Can you guess what the optimal meeting strategy is?

As always,
```python
from manim import *

class Example(Scene):
    initial_points = [-6, 0, 4]
    meetings = [(1, 2), (0, 2), (0, 1), (1, 2), (0, 1), (1, 2), (0, 1), (1, 2), (0, 1), (1, 2), (0, 1), (1, 2)]

    def construct(self):
        distance = Tex(r"Total Distance: \ ", r"$ 0.00 $").to_edge(UP)
        total_distance = 0

        ants = [] # This is symbolic. They are dots.
        for point in self.initial_points:
            ants.append(SmallDot().move_to(RIGHT * point))

        self.play(*[ShowCreation(ant) for ant in ants], Write(distance))

        for meeting in self.meetings:
            a,b = ants[meeting[0]], ants[meeting[1]]
            middle = (a.get_center() + b.get_center()) / 2 * RIGHT # Normalize upward direction
            total_distance += abs(a.get_center()[0] - b.get_center()[0])
            self.play(
                a.animate.move_to(middle + UP / 3),
                b.animate.move_to(middle),
                Transform(
                    distance[1],
                    Tex(f"$ {total_distance :.2f} $").move_to(distance[1])
                )
            )
```

## Solution

Coming later