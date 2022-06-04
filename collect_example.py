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


class SineCurveUnitCircle(Scene):
    # contributed by heejin_park, https://infograph.tistory.com/230
    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([-6,0,0])
        x_end = np.array([6,0,0])

        y_start = np.array([-4,-2,0])
        y_end = np.array([-4,2,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()

        self.origin_point = np.array([-4,0,0])
        self.curve_start = np.array([-3,0,0])

    def add_x_labels(self):
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )


        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)


class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        numberplane = NumberPlane()
        
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        position = arrow.get_end()
        tip_text = Text(f'{position}')
        tip_text.add_updater(lambda a: a.next_to(arrow.get_end(), RIGHT, buff=1))

        self.add(numberplane, dot, arrow, origin_text, tip_text)
        self.play(Rotate(arrow, about_point=ORIGIN, angle=TAU*2, rate_func=linear), run_time=5)
        self.wait(1)


class PMobjectExample(Scene):
    def construct(self):

        pG = PGroup()  # This is just a collection of PMobject's

        # As the scale factor increases, the number of points
        # removed increases.
        for sf in range(1, 9 + 1):
            p = PointCloudDot(density=20, radius=1).thin_out(sf)
            # PointCloudDot is a type of PMobject
            # and can therefore be added to a PGroup
            pG.add(p)

        # This organizes all the shapes in a grid.
        pG.arrange_in_grid()

        for p in pG:
            self.add(p)
            self.play(GrowFromCenter(p), run_time=8)
        self.wait(1)


class GraphExample(Scene):
    def construct(self):
        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinates()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # Axes.plot will return the graph of a function
        sin_graph = axes.plot(
            lambda x: 2 * math.sin(x),
            color=BLUE,
        )
        # By default, it draws it so as to somewhat smoothly interpolate
        # between sampled points (x, f(x)).  If the graph is meant to have
        # a corner, though, you can set use_smoothing to False
        relu_graph = axes.plot(
            lambda x: max(x, 0),
            use_smoothing=False,
            color=YELLOW,
        )
        # For discontinuous functions, you can specify the point of
        # discontinuity so that it does not try to draw over the gap.
        step_graph = axes.plot(
            lambda x: 2.0 if x > 3 else 1.0,
            discontinuities=[3],
            color=GREEN,
        )

        # Axes.plot_label takes in either a string or a mobject.
        # If it's a string, it treats it as a LaTeX expression.  By default
        # it places the label next to the graph near the right side, and
        # has it match the color of the graph
        sin_label = Tex("sin(x)").to_edge(RIGHT)
        relu_label = Tex("ReLU").to_edge(RIGHT)
        step_label = Tex("Step").to_edge(RIGHT)

        self.play(
            Create(sin_graph),
            FadeIn(sin_label),
        )
        self.wait(2)
        self.play(
            ReplacementTransform(sin_graph, relu_graph),
            FadeTransform(sin_label, relu_label),
        )
        self.wait()
        self.play(
            ReplacementTransform(relu_graph, step_graph),
            FadeTransform(relu_label, step_label),
        )
        self.wait()

        parabola = axes.plot(lambda x: 0.25 * x**2)
        parabola.set_stroke(BLUE)
        self.play(
            FadeOut(step_graph),
            FadeOut(step_label),
            Create(parabola)
        )
        self.wait()

        # You can use axes.input_to_graph_point, abbreviated
        # to axes.i2gp, to find a particular point on a graph
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(2, parabola))
        self.play(FadeIn(dot))

        # A value tracker lets us animate a parameter, usually
        # with the intent of having other mobjects update based
        # on the parameter
        x_tracker = ValueTracker(2)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )

        self.play(x_tracker.animate.set_value(4), run_time=3)
        self.play(x_tracker.animate.set_value(-2), run_time=3)
        self.wait()
