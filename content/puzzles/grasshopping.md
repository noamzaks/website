---
title: "Grasshopping"
description: A grasshopper sits in a point $ M \in \mathbb R ^ 2 $, outside of the square $ [0, 1] ^ 2 $. Each time, they face towards the origin and choose the rightmost corner of the square they are able to see (from their perspective). Then they go to the symmetric point with regard to it.
ogDescriptoin: A grasshopper sits in a point M in the plane, outside of the square [0, 1] x [0, 1]. Each time, they face towards the origin and choose the rightmost corner of the square they are able to see (from their perspective). Then they go to the symmetric point with regard to it.
date: 2021-02-09T13:27:04+02:00
draft: false
---

A grasshopper sits in a point $ M \in \mathbb R ^ 2 $, outside of the square $ [0, 1] ^ 2 $. Each time, they face towards the origin and choose the rightmost corner of the square they are able to see (from their perspective). Then they go to the symmetric point with regard to it.

That's quite a difficult explanation of their moves, so here's one without words - an example of the first 50 hops when the grasshopper starts at $ (3, 2) $:

{{< video "RotatingExample" >}}

If you like skating more than rotating you may prefer the following animation

{{< video "SlidingExample" >}}

Here's the same grasshopper playing faster over 150 hops:

{{< video "FastExample" >}}

You can create your own grasshopper animation with the following code, by customizing the `hops` variable and `time` variable (less time is faster and more hops is longer)

```python
from manim import *

def find_closest_position(position: np.ndarray) -> np.ndarray:
    if position[0] >= 0:
        if position[1] >= 0:
            if position[1] > 1:
                return UP
            return UP + RIGHT
        if position[0] >= 1:
            return UP + RIGHT
        return RIGHT
    if position[1] >= 0:
        return ORIGIN
    return RIGHT

SCALE = 3


class Grasshopper(Scene):
    starting_position = PI * RIGHT + PI * UP
    hops = 30
    time = .3

    def construct(self):
        square = Square(side_length=1/SCALE).align_to(ORIGIN, DOWN).align_to(ORIGIN, LEFT)
        distance_text = Tex("Distance: ", f"$ {np.linalg.norm(self.starting_position) :.2f} $").to_edge(DOWN)
        hopper = Dot(color=BLUE).align_to(ORIGIN, LEFT).align_to(ORIGIN, DOWN).shift(self.starting_position / SCALE)
        self.play(ShowCreation(hopper), ShowCreation(square), Write(distance_text))

        position = self.starting_position / SCALE
        for _ in range(self.hops):
            dot = find_closest_position(position*SCALE) / SCALE

            distance = np.linalg.norm(position - dot) * SCALE

            beam = Line(
                position,
                dot,
            )
            self.play(ShowCreation(beam), run_time=self.time)

            next_position = (position + 2 * (dot - position))

            self.play(
                Rotate(
                    beam,
                    180 * DEGREES,
                    about_point=dot
                ),
                CounterclockwiseTransform(
                    hopper,
                    hopper.copy().move_to(next_position),
                ),
                Transform(
                    distance_text[1],
                    Tex(f"$ {distance :.2f} $").move_to(distance_text[1]),
                ),
                run_time=3*self.time,
            )

            self.play(FadeOut(beam), run_time=self.time)

            position = next_position
```

## Solution

The solution is actually quite tricky, so it isn't available yet.