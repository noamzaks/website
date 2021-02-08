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