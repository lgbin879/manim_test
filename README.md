# manim_test
my personal manim pratice

## how to run in manim docker
docker run --rm -it  --user="$(id -u):$(id -g)" -v "$(pwd)":/manim manimcommunity/manim manim test1.py -ql
