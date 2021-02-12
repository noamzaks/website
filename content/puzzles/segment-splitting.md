---
title: "Segment Splitting"
description: Given a set of pairwise-disjoint intervals (such that the intersection of every pair is $ \emptyset $) in $ [0, 1] $, assuming the total length is greater than $ \frac 1 2 $, show there are two points $ a,b $ in the union of the segments such that $ |a-b| = \frac 1 {10} $.
ogDescription: Given a set of pairwise-disjoint intervals (such that the intersection of every pair is empty ) in [0, 1], assuming the total length is greater than 1/2, show there are two points a,b in the union of the segments such that |a-b| = 1/10.
date: 2021-02-12T13:41:10+02:00
draft: false
---

Given a set of pairwise-disjoint intervals (such that the intersection of every pair is $ \emptyset $) in $ [0, 1] $, assuming the total length is greater than $ \frac 1 2 $, show there are two points $ a,b $ in the union of the segments such that $ |a-b| = \frac 1 {10} $.

Here are a few examples

{{< video "Example1" >}}
{{< video "Example2" >}}
{{< video "Example3" >}}

```python
from manim import *

class SegmentSplittingExample(Scene):
    min_width = .5
    distance = .1

    def construct(self):
        import time
        np.random.seed(int(time.time()))

        intervals = [(-1, 0), (1, 2)]
        total_interval_length = 0
        while total_interval_length <= self.min_width:
            i = np.random.choice(range(len(intervals) - 1))
            a = np.random.random()
            b = np.random.random()
            x,y = sorted([a,b])
            
            length = intervals[i+1][0] - intervals[i][1]

            intervals.insert(i + 1, (
                intervals[i][1] + length * x,
                intervals[i][1] + length * y,
            ))
            
            total_interval_length += intervals[i+1][1] - intervals[i+1][0]

        lines = []
        width = self.camera.frame_width
        for interval in intervals:
            lines.append(Line(self.expand_to_width(interval[0]), self.expand_to_width(interval[1])))
        
        self.play(*[ShowCreation(line) for line in lines])

        interval_i = None
        reverse = False
        for i in range(1, len(intervals) - 1):
            shifted_interval = (intervals[i][0] + self.distance, intervals[i][1] + self.distance)
            if shifted_interval[0] >= intervals[i+1][0]:
                interval_i = i
                break
            elif shifted_interval[1] <= intervals[i+1][1]:
                interval_i = i
                reverse = True
                break
        if interval_i is None:
            raise Exception("Couldn't find points with specified distance")

        position = 1 if reverse else 0
        dot = Dot(color=BLUE).move_to(self.expand_to_width(intervals[interval_i][position]))
        shift = -self.distance if reverse else self.distance
        self.play(ShowCreation(dot))
        self.play(
            Transform(dot.copy(), Dot(color=BLUE).move_to(self.expand_to_width(intervals[interval_i][position] + shift)))            
        )
        brace = Brace(Line(self.expand_to_width(intervals[interval_i][position]), self.expand_to_width(intervals[interval_i][position] + shift)))
        self.play(
            ShowCreation(brace),
            ShowCreation(brace.get_tex(f"{self.distance}"))
        )

    def expand_to_width(self, x: float) -> np.ndarray:
        return LEFT * self.camera.frame_width / 2 + x * self.camera.frame_width * RIGHT
```

A few generalizations can be made - for example, there are 2 points such that $ |a-b| = \frac 1 {2n} $ for all $ n \in \mathbb N $. The above code also works for them! Here are a few demos.

{{< video "GeneralizationExample1" >}}
{{< video "GeneralizationExample2" >}}
{{< video "GeneralizationExample3" >}}

## Solution

Assume towards a contradiction that no such points $ a,b $ exist. Now, split the interval $ [0, 1] $ to 10 tenths, and observe the following: for each adjacent pair of tenths, the total length of the intervals is at most $ \frac 1 {10} $. 
Hence the total length in $ [0, 1] $ is at most $ 5 \times \frac 1 {10} = \frac 1 2 $, which gives a contradiction.

This is true because if we look at the first interval, by the assumption we know we can move the segments right by $ \frac 1 {10} $ and still there won't be intersections - even with the segments in the second interval. Hence, the total length in the first and second interval is at most $ \frac 1 {10} $ because the segments can be placed inside $ [\frac 1 {10}, \frac 2 {10} ] $

An animation of this will be added soon!