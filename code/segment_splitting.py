from manim import *

class SegmentSplittingExample(Scene):
    min_width = .5
    distance = .5

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