#!/usr/bin/env python3

import math
from manim import *
#  config.background_color = WHITE
#  config["background_color"] = WHITE

class ManimCELogo(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN)
        self.add(logo)
        self.wait()


import manim
class TitleExample(Scene):
    def construct(self):
        banner = ManimBanner()
        title = Title(f"Manim version {manim.__version__}")
        self.add(banner, title)
        self.wait(2)


class StraighteningCircle(Scene):
    def construct(self):
        circle = Circle(radius=1.75, stroke_width=50).set_color_by_gradient(([GREEN, BLUE])).move_to(UP*1.5).rotate(90*DEGREES, Z_AXIS)
        line = Line(start = [-2*(math.pi), 0, 0], end = [2*math.pi, 0, 0], stroke_width=50, color=BLUE).move_to(DOWN*1.5)

        self.play(DrawBorderThenFill(circle))
        self.wait()
        self.play(ReplacementTransform(circle, line))
        self.wait()
