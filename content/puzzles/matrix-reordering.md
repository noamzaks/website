---
title: Matrix Reordering
description: Given a matrix of size $ m \times n $ which contains numbers from $ 1 $ to $ n $ and each number appears exactly $ m $ times, show that one can reorder the numbers inside each column such that the resulting matrix would have the numbers $ 1 $ to $ n $ in every line.
ogDescription: Given an m by n matrix which contains numbers from 1 to n and each number appears exactly m times, show that one can reorder the numbers inside each column such that the resulting matrix would have the numbers 1 to n in every line.
date: 2021-01-01T16:00:28+02:00
tags: [graph-theory]
draft: false
---

Given a matrix of size $ m \times n $ which contains numbers from $ 1 $ to $ n $ and each number appears exactly $ m $ times, show that one can reorder the numbers inside each column such that the resulting matrix would have the numbers $ 1 $ to $ n $ in every line.

First, a (few) quick demo(s) to understand:
{{< video "Example1" >}}
{{< video "Example2" >}}
{{< video "Example3" >}}

These demos all share a single codebase which creates an animation given the input. You only need to change the `values` array. The code uses brute force to calculate the solution (which we will in the proof's animation), at a rate of around factorial twice of the row count. It means about $ 3!! = 6! = 720 $ options for $ 3 $ but it ramps up _pretty quickly_ as $ 4!! = 24! > 10 ^ {23} $.

```python
from manimlib.imports import *
import itertools


class Example(Scene):
    values = [
        [4, 2, 3, 1],
        [3, 4, 2, 1],
        [3, 2, 1, 4],
    ]
    m = len(values)
    n = len(values[0])
    padding = 2

    def construct(self):
        step = min((FRAME_WIDTH - 2*self.padding) / (self.n - 1),
                   (FRAME_HEIGHT - 2*self.padding) / (self.m - 1))
        remaining_horizontal = FRAME_WIDTH - \
            2*self.padding - (self.n - 1) * step
        remaining_vertical = FRAME_HEIGHT - 2 * \
            self.padding - (self.m - 1) * step

        matrix = []
        animations = []
        for i in range(self.m):
            row = []
            for j in range(self.n):
                text = TexMobject(self.values[i][j])
                text.move_to(self.position_for(
                    step,
                    remaining_horizontal,
                    remaining_vertical,
                    i,
                    j
                ))
                row.append(text)
                animations.append(Write(text))
            matrix.append(row)
        self.play(*animations)

        previous_values = self.values
        self.find_solution()

        highlighter_rectangle = None
        for j in range(self.n):
            if j == 0:
                highlighter_rectangle = Rectangle(
                    height=self.m*step,
                    width=step,
                    fill_opacity=0.3,
                    color=YELLOW
                )
                highlighter_rectangle.align_to(matrix[0][0], UP)
                highlighter_rectangle.align_to(matrix[0][0], LEFT)

                highlighter_rectangle.shift(step * (UP + 0.9*LEFT) / 2)

                self.play(ShowCreation(highlighter_rectangle))
            else:
                self.play(ApplyMethod(
                    highlighter_rectangle.shift, step*RIGHT))

            animations = []
            for i in range(self.m):
                if previous_values[i][j] == self.values[i][j]:
                    continue
                new_text = TexMobject(self.values[i][j])
                new_text.move_to(self.position_for(
                    step,
                    remaining_horizontal,
                    remaining_vertical,
                    i,
                    j
                ))
                animations.append(Transform(matrix[i][j], new_text))
            if len(animations) > 0:
                self.play(*animations)
        self.play(FadeOut(highlighter_rectangle))

        highlighter_rectangle = Rectangle(
            height=step,
            width=self.n*step,
            fill_opacity=0.3,
            color=YELLOW
        )
        highlighter_rectangle.align_to(matrix[0][0], UP)
        highlighter_rectangle.shift(step*0.85*UP / 2)

        self.play(ShowCreation(highlighter_rectangle))
        for i in range(1, self.m):
            self.wait(0.5)
            self.play(ApplyMethod(highlighter_rectangle.shift, step*DOWN))

        self.wait(0.5)
        self.play(FadeOut(highlighter_rectangle))
        self.wait(1)
        matrix_flat = []
        for row in matrix:
            for text in row:
                matrix_flat.append(text)
        finale = VGroup(*matrix_flat)
        self.play(Transform(finale, Square(side_length=0.3, fill_opacity=0.7)))
        self.wait(0.5)
        self.play(ApplyMethod(finale.scale, 50))
        self.play(FadeOut(finale))

    def position_for(self, step, remaining_horizontal, remaining_vertical, i, j):
        result = TOP + LEFT_SIDE
        result += step * (i * DOWN + j * RIGHT)
        result += self.padding * (DOWN + RIGHT)
        result += (remaining_horizontal * RIGHT +
                   remaining_vertical * DOWN) / 2
        return result

    def find_solution(self):
        by_columns = [list(map(lambda row: row[column], self.values))
                      for column in range(self.n)]
        all_permutations = list(map(
            lambda column: list(itertools.permutations(column)),
            by_columns
        ))

        solution = None
        for current_permutations in itertools.permutations(range(math.factorial(self.m))):
            permutated_columns = list(map(
                lambda i: all_permutations[i][current_permutations[i]], range(self.n)))
            correct_solution = True
            for row in range(self.m):
                found_value = [False for i in range(self.n)]
                for column in range(self.n):
                    found_value[permutated_columns[column][row] - 1] = True
                for value in found_value:
                    if not value:
                        correct_solution = False
                        break
                if not correct_solution:
                    break
            if correct_solution:
                solution = permutated_columns
                break

        if not solution:
            raise Exception("No solution found!")
        by_rows = [list(map(lambda column: column[row], solution))
                   for row in range(self.m)]
        self.values = by_rows
```

To be continued when I have time. Happy new year!

### Notes
- For some reason the `find_solution` method does not find a solution for following values. If you find some explanation, please let me know!

```python
values = [
    [6, 2, 1, 3, 5, 6],
    [3, 5, 6, 5, 2, 4],
    [4, 2, 3, 4, 1, 1],
]
```