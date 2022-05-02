#!/usr/bin/env python3

"""
this is my manim project for solar system
"""

from manim import *

class SunEarth(Scene):
    """Sun and Earth"""
    def construct(self):

        ## Make objects
        sun = Circle(color=YELLOW, fill_color=YELLOW, fill_opacity=1)
        rail_earth = Annulus(inner_radius=3.79, outer_radius=3.8, color=ORANGE)

        earth = Circle(color=BLUE, fill_color=BLUE, fill_opacity=1)
        earth.scale(0.25)
        rail_moon = Annulus(inner_radius=0.5, outer_radius=0.51, color=ORANGE)
        moon = Circle(color=GREY, fill_color=GREY, fill_opacity=1)
        moon.scale(0.1)
        emsystem = VGroup(earth, rail_moon, moon)

        ## Shift position
        moon.shift(np.array([-0.49, 0, 0]))
        emsystem.shift(np.array([-3.75, 0.9, 0]))

        ## Show objects
        self.play(FadeIn(sun))
        self.wait(1)
        self.play(GrowFromCenter(rail_earth))
        self.wait(1)
        self.play(FadeIn(emsystem))
        self.wait(2)
