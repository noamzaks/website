---
title: "Triangle Areas"
description: Given a group $ S $ of points $ (x,y) \in \mathbb R ^ 2 $ such that every three points in $ S $ form a triangle (aren't collinear) of area at most $ 1 $, show that there is some triangle with area at most 2 which bounds $ S $.
ogDescription: Given a group S of points (x,y) in the plane such that every three points in S form a triangle (aren't collinear) of area at most 1, show that there is some triangle with area at most 2 which bounds S.
date: 2021-02-11T16:24:22+02:00
tags: [area, min-max]
draft: false
---

Given a group $ S $ of points $ (x,y) \in \mathbb R ^ 2 $ such that every three points in $ S $ form a triangle (aren't collinear) of area at most $ 1 $, show that there is some triangle with area at most 2 which bounds $ S $.

## Solution

The idea is to look at the three points which make the triangle with the largest area, and note the following observation:

{{< video "Example1" >}}
{{< video "Example2" >}}
{{< video "Example3" >}}

You can generate similar animations with any number of points using the following

```python
from typing import Tuple
from manim import *
from itertools import combinations, permutations


def mirror_line(a, b, c) -> Line:
    direction = a - b
    return Line(c + 10 * direction, c - 10 * direction)


class TriangleAreas(Scene):
    points = 10

    def construct(self):
        import time

        np.random.seed(int(time.time()))

        S = list(
            map(
                lambda point: np.append(point * 2 - 1, [0]) * 3,
                np.random.rand(self.points, 2),
            )
        )

        max_triangle: Tuple[np.ndarray, np.ndarray, np.ndarray] = None
        max_area = -np.infty
        for x, y, z in combinations(S, 3):
            area = np.linalg.norm(np.cross(z - x, z - y))
            if area > max_area:
                max_area = area
                max_triangle = (x, y, z)

        a, b, c = max_triangle
        small_lines = [Line(a, b), Line(a, c), Line(b, c)]
        big_lines = [mirror_line(a, b, c), mirror_line(a, c, b), mirror_line(b, c, a)]

        self.play(*[ShowCreation(Dot().move_to(dot)) for dot in S])
        self.play(*[ShowCreation(line) for line in small_lines])

        for i in range(len(small_lines)):
            self.play(Transform(small_lines[i].copy(), big_lines[i]))
```