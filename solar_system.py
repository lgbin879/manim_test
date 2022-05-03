#!/usr/bin/env python3

"""
this is my manim project for solar system
"""

from manim import *

class SunEarth(Scene):
    """Sun and Earth"""
    def construct(self):

        ## Make objects
        quote = Tex('这是我的第一个Manim作品', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=40)
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = Tex('This is my first manim product', 
                    tex_template=TexTemplateLibrary.ctex, 
                    font_size=50)
        quote2.set_color(GREEN)

        self.add(quote)
        self.play(FadeIn(quote))
        self.wait(1)
        self.play(Transform(quote, quote2), run_time=2)
        self.wait(1)
        self.play(FadeOut(quote))

        sun = Circle(color=YELLOW, fill_color=YELLOW, fill_opacity=1)
        #  rail_earth = Annulus(inner_radius=3.79, outer_radius=3.8, color=ORANGE)
        rail_earth = Circle(color=ORANGE, radius=3.5, stroke_width=1)

        earth = Circle(color=BLUE, fill_color=BLUE, fill_opacity=1)
        earth.scale(0.25)
        #  rail_moon = Annulus(inner_radius=0.5, outer_radius=0.51, color=ORANGE)
        rail_moon = Circle(color=ORANGE, radius=0.5)
        rail_moon.set_stroke(width=1)
        moon = Circle(color=GREY, fill_color=GREY, fill_opacity=1)
        moon.scale(0.1)
        emsystem = VGroup(earth, rail_moon, moon)

        ## Shift position
        moon.shift(np.array([0.49, 0, 0]))
        emsystem.shift(np.array([3.5, 0, 0]))
        #  emsystem.align_to(rail_earth)

        ## Show objects
        self.play(GrowFromCenter(sun))
        self.wait(1)
        
        self.play(Create(rail_earth))
        self.wait(1)
        
        self.play(FadeIn(earth))
        self.wait(1)
        self.play(Create(rail_moon))
        self.wait(1)
        self.play(FadeIn(moon))
        self.wait(1)

        self.play(
                Rotate(emsystem, angle=2*PI, about_point=ORIGIN, rate_func=linear),
                MoveAlongPath(moon, rail_moon),
                run_time=15, rate_func=linear
                )
        self.play(
                Rotate(emsystem, angle=2*PI, about_point=ORIGIN, rate_func=linear),
                MoveAlongPath(moon, rail_moon),
                #  always_redraw(lambda : ApplyMethod(moon.rotate, 4*PI)), #not work
                run_time=15, rate_func=linear
                )

        self.wait(1)

