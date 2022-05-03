#!/usr/bin/env python3

from manim import *
#  config.background_color = WHITE
#  config["background_color"] = WHITE

class Shoot(Scene):
    """Shoot test"""
    def construct(self):
       ## Making aim_scope
       circle01 = Circle(color=BLUE)
       circle02 = Circle(color=RED, fill_color=RED, fill_opacity=1)
       circle02.scale(0.1)
       line01 = Line(np.array([-1, 0, 0]), np.array([1, 0, 0]), color=RED)
       line02 = Line(np.array([0, 1, 0]), np.array([0, -1, 0]), color=RED)
       aim_scope = VGroup(circle01, circle02, line01, line02)

       ## Making Target
       target_list = []
       for i in range(3):
           for j in range(5):
               target_ij = Circle(color=YELLOW, fill_color=YELLOW, fill_opacity=0.4)
               target_ij.scale(0.4)
               target_ij.shift(np.array([-4 +j*2, -2 + i*2, 0]))
               self.play(FadeIn(target_ij))
               target_list.append(target_ij)

       self.wait(1)

       ## move & shoot animation
       def shoot_ij(i, j):
           """docstring for shoot_ij"""
           target_ij = target_list[j + i*5]
           self.play(ApplyMethod(aim_scope.next_to, target_ij, 0))
           self.play(ApplyMethod(target_ij.set_fill, GREY), ApplyMethod(target_ij.set_color, GREY))
           self.wait(0.5)

           #  ij = TextMobject("({i}, {j})", color=GREY)
           ij = Tex(f"({i}, {j})", color=GREY)
           ij.next_to(target_ij, DOWN)
           self.play(Write(ij))
           self.wait(1)
           return 0

       self.play(GrowFromCenter(aim_scope))
       self.wait(0.5)
       self.play(ApplyMethod(aim_scope.shift, DOWN*3 + LEFT*6.1))
       shoot_ij(0, 1)
       shoot_ij(2, 0)
       shoot_ij(1, 3)
       shoot_ij(0, 0)
       shoot_ij(2, 4)


class LoveDeathRobots(Scene):
    """docstring for LoveDeathRobots"""
    def construct(self):

        ## Make object
        circle01 = Circle(color=RED, fill_color=RED, fill_opacity=0.5)
        circle01.shift(np.array([-0.5, 0.5, 0]))
        circle02 = Circle(color=RED, fill_color=RED, fill_opacity=0.5)
        circle02.shift(np.array([0.5, 0.5, 0]))
        square01 = Square(color=RED, fill_color=RED, fill_opacity=0.5)
        square01.scale(0.99)
        square01.rotate(np.pi/4)
        heart = VGroup(circle01, circle02, square01)

        rec01 = Rectangle(color=RED, width=4, height=1, fill_color=RED, fill_opacity=0.5)
        rec01.rotate(np.pi/4)
        rec02 = Rectangle(color=RED, width=4, height=1, fill_color=RED, fill_opacity=0.5)
        rec02.rotate(-np.pi/4)
        cross = VGroup(rec01, rec02)

        square02 = Square(color=RED, fill_color=RED, fill_opacity=0.5)
        square02.scale(1.5)
        circle03 = Circle(color=RED, fill_color=BLACK, fill_opacity=0.5)
        circle03.scale(0.4)
        circle03.shift(np.array([-0.6, 0.4, 0]))
        circle04 = Circle(color=RED, fill_color=BLACK, fill_opacity=0.5)
        circle04.scale(0.4)
        circle04.shift(np.array([0.6, 0.4, 0]))
        ghost = VGroup(square02, circle03, circle04)

        line01 = Line(np.array([-5, 0, 0]), np.array([5, 0, 0]), color=RED)
        title = Tex(r"LOVE DEATH + ROBOTS", color=RED)
        title.scale(2)
        namespace = VGroup(line01, title)

        ## Set position
        ghost.to_edge(RIGHT)
        VGroup(line01, title).to_edge(DOWN)

        ## Show object
        self.play(Create(circle01),
                  Create(circle02),
                  Create(square01))
        self.wait(1)
        self.play(heart.animate.to_edge(LEFT))

        self.play(Create(rec01),
                  Create(rec02))
        self.wait(1)

        self.play(Create(square02))
        self.play(Create(circle03),
                  Create(circle04))
        self.wait(1)
        self.play(VGroup(heart, cross, ghost).animate.set_fill(opacity=1))
        self.wait(1)

        self.play(Create(line01))
        self.play(Transform(line01, title))
        self.wait(2)

        self.play(VGroup(heart, cross, ghost, namespace).animate.shift(np.array([0,1,0])), run_time=2)
        self.wait(2)


class HelloWorld(Scene):
    def construct(self):
        print(manimpango.list_fonts())
        text = Text("Hello world", font_size=144)
        self.add(text)
        self.wait(2)
   

class LaTeXTemplateLibrary(Scene):
    def construct(self):
        tex = Tex('Hello 你好 ', tex_template=TexTemplateLibrary.ctex, font_size=144)
        self.add(tex)
        self.wait(2)

# 设置文本大小
class Demo2(Scene):
    def construct(self):
#        WaterMark.construct(self)
        s = "Python数据之道"
        t1 = Text(s)
        t1.to_edge(UP,buff=0.5)
        t2 = Text(s).scale(2)
        t2.next_to(t1,DOWN)
        t3 = Text(s).set_width(10)
        t3.next_to(t2,DOWN)
        t4 = Text(s,font_size=40)
        t4.next_to(t3,DOWN)       
        self.add(t1)
        self.play(Write(t2))
        self.play(Create(t3))
        self.play(Write(t4))
        self.wait(1)


class HelloManim(Scene):
    """docstring for Hello_Manim"""
    def construct(self):
        ## making object
        helloworld = Tex("Hello World!", color=YELLOW)
        rectangle = Rectangle(color=BLUE)
        rectangle.surround(helloworld)

        group1 = VGroup(helloworld, rectangle)
        hellomanim = Tex("Hello Manim", color=GREEN)
        hellomanim.scale(2.5)

        ## position

        ## showing object
        self.play(Write(helloworld))
        self.wait(1)
        self.play(FadeIn(rectangle))
        self.wait(1)
        self.play(ApplyMethod(group1.scale, 2.5))
        self.wait(1)
        self.play(Transform(helloworld, hellomanim))
        self.wait(1)

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
                left_square.animate.rotate(PI/2), Rotate(right_square, angle=PI), run_time=2
                )
        self.wait()
