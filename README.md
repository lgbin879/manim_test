# manim_test
my personal manim pratice

## how to run in manim docker
docker pull manimcommunity/manim
docker run --rm -it  --user="$(id -u):$(id -g)" -v "$(pwd)":/manim manimcommunity/manim manim test1.py -ql

## how to use Chinese Text
from manim import *

class LaTeXTemplateLibrary(Scene):
    def construct(self):
        tex = Tex('Hello 你好 \\LaTeX', tex_template=TexTemplateLibrary.ctex, font_size=144)
        self.add(tex)
