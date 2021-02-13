from manim import *
from fractions import Fraction


class AdjacentFractionsExample(Scene):
    n = 4

    def construct(self):
        fractions = [Fraction(1, 1)]
        for denominator in range(self.n + 1):
            for numerator in range(1, denominator):
                fraction = Fraction(numerator, denominator)
                if fraction not in fractions:
                    fractions.append(Fraction(numerator, denominator))
        fractions = sorted(fractions)
        fraction_mobjects = [
            MathTex(
                r"\frac {"
                + str(fraction.numerator)
                + "} {"
                + str(fraction.denominator)
                + "}"
            ).move_to(self.expand_to_width(float(fraction)))
            for fraction in fractions
        ]
        self.play(
            *[ShowCreation(fraction_mobject) for fraction_mobject in fraction_mobjects]
        )

        for i in range(len(fractions) - 1):
            first_multiple = (
                MathTex(str(fractions[i + 1].numerator * fractions[i].denominator))
                .align_to(fraction_mobjects[i], LEFT)
                .shift(2 * DOWN)
            )
            minus = MathTex("-").next_to(first_multiple, RIGHT)
            second_multiple = MathTex(
                str(fractions[i + 1].denominator * fractions[i].numerator)
            ).next_to(minus, RIGHT)
            self.play(
                ReplacementTransform(
                    VGroup(
                        MathTex(str(fractions[i + 1].numerator))
                        .align_to(fraction_mobjects[i + 1], UP)
                        .align_to(fraction_mobjects[i + 1], LEFT),
                        MathTex(str(fractions[i].denominator))
                        .align_to(fraction_mobjects[i], DOWN)
                        .align_to(fraction_mobjects[i], LEFT),
                    ),
                    first_multiple,
                ),
            )
            self.play(
                FadeIn(minus),
                ReplacementTransform(
                    VGroup(
                        MathTex(str(fractions[i + 1].denominator))
                        .align_to(fraction_mobjects[i + 1], DOWN)
                        .align_to(fraction_mobjects[i + 1], LEFT),
                        MathTex(str(fractions[i].numerator))
                        .align_to(fraction_mobjects[i], UP)
                        .align_to(fraction_mobjects[i], LEFT),
                    ),
                    second_multiple,
                ),
            )
            self.play(
                FadeOut(first_multiple),
                FadeOut(minus),
                Transform(
                    second_multiple,
                    MathTex(
                        str(
                            fractions[i + 1].numerator * fractions[i].denominator
                            - fractions[i].numerator * fractions[i + 1].denominator
                        )
                    )
                    .move_to(first_multiple)
                    .align_to(fraction_mobjects[i], LEFT),
                ),
            )
        halmos = Square(fill_opacity=1, side_length=0.2)
        self.play(ReplacementTransform(VGroup(*self.mobjects), halmos))
        self.play(halmos.animate.scale(75), run_time=3)
        self.play(FadeOut(halmos))

    def expand_to_width(self, x: float) -> np.ndarray:
        width = self.camera.frame_width - 2
        return width * LEFT / 2 + width * x * RIGHT


class AdjacentFractionsSolution(Scene):
    a = Fraction(2, 3)
    b = Fraction(3, 4)

    def construct(self):
        plane = NumberPlane()
        self.play(ShowCreation(plane))
        a_point = self.a.denominator * RIGHT + self.a.numerator * UP
        b_point = self.b.denominator * RIGHT + self.b.numerator * UP

        self.play(
            ShowCreation(Dot().move_to(a_point)),
            ShowCreation(Line(ORIGIN, a_point)),
        )

        self.play(
            ShowCreation(Dot().move_to(b_point)),
            ShowCreation(Line(ORIGIN, b_point)),
        )

        triangle = Polygon(ORIGIN, a_point, b_point, color=WHITE, fill_opacity=0.6)
        self.play(FadeOut(plane), ShowCreation(triangle))

        self.play(
            Transform(
                triangle.copy(),
                MathTex(r"S = \frac {ad - bc} 2 = \frac 1 2").shift(3 * RIGHT + DOWN),
            )
        )
