# Code obtained from: https://github.com/brianamedee/Manim-Tutorials-2021/blob/main/1Tutorial_Intro.py
# Learned from Brian Amedee: https://www.youtube.com/watch?v=jFqYq9quBds

# This is a practice repo 

from manim import *
from numpy import cos

class Tute1(Scene): #ILLUSTRATING HOW TO PUT A NUMBER PLANE ON SCENE WITH A GRAPH, and a line using c2p
    def construct(self):

        backg_plane = NumberPlane(x_range=[-7,7,1], y_range=[-4,4,1])
        backg_plane.add_coordinates()
        # code = Code("Tute2Code2.py", style=Code.styles_list[12], background ="window", language = "python", insert_line_no = True,
        # tab_width = 2, line_spacing = 0.3, font="Monospace").set_width(7).to_edge(UL, buff=0)

        my_plane = NumberPlane(x_range = [-6,6], x_length = 5,
        y_range = [-10,10], y_length=5)
        my_plane.add_coordinates()
        my_plane.shift(RIGHT*3)

        my_function = my_plane.get_graph(lambda x : 0.1*(x-5)*x*(x+5), 
        x_range=[-6,6], color = GREEN_B)

        label = MathTex("f(x)=0.1x(x-5)(x+5)").next_to(
            my_plane, UP, buff=0.2)

        area = my_plane.get_area(graph = my_function, 
        x_range = [-5,5], color = [BLUE,YELLOW])

        horiz_line = Line(
            start = my_plane.c2p(0, my_function.underlying_function(-2)),
        end = my_plane.c2p(-2, my_function.underlying_function(-2)),
        stroke_color = YELLOW, stroke_width = 10)

        self.play(FadeIn(backg_plane), run_time=6)
        self.play(backg_plane.animate.set_opacity(0.2))
        self.wait()
        self.play(DrawBorderThenFill(my_plane), run_time=2)
        self.wait()
        self.play(Create(my_function), Write(label), run_time=10)
        self.wait()
        self.play(FadeIn(area), run_time = 2)
        self.wait()
        self.play(Create(horiz_line), run_time = 2)
        self.wait()

class SineCurvePlotting(Scene):
    def construct(self):

        my_plane = NumberPlane(x_range = [-0,7], x_length = 10,
                                y_range = [-1,1], y_length=3, background_line_style=None)
        my_plane.add_coordinates()
        
        cosine_function = my_plane.get_graph(lambda x : cos(x),
                            x_range=[0, 2*PI], color = GREEN_B)

        # circle_function = my_plane.get_graph(lambda x, y : x**2 + y**2 = 1,
        #                         x_range=[-1, 1], y_range=[-1, 1], color=YELLOW_A)

        self.play(DrawBorderThenFill(my_plane), run_time=2)
        self.play(Create(cosine_function), run_time=5)
        # self.play(Create(circle_function), run_time=2)

class UnitCircleAndSineCurvePlotting(Scene):
    def construct(self):
        self.e = ValueTracker(0.01)  # Tracks the end value of both functions 

        # UnitCirclePlotting
        

        # Cosine curve plotting 
        axes0 = Axes(x_range=[0, 2*PI, PI/2], x_length=3, y_range=[-1.0, 1.0, 1], y_length=2, tips=False)
        axes0.add_coordinates(
            {
                PI/2 : MathTex(r"\frac{\pi}{2}"),
                PI : MathTex("\pi"),
                3*PI/2 : MathTex(r"\frac{3 \pi}{2}"),
                2*PI : MathTex("2 \pi")
            },
            {
                -1.0 : MathTex("-1"),
                0.0 : MathTex("0"),
                1.0 : MathTex("1"),
            }
        )
        axes0.move_to([1, 2, 0])    # Location of axes 
        cosineCurveGraph = always_redraw(lambda : axes0.get_graph(lambda x : np.cos(x), x_range=[0, self.e.get_value()], color=GREEN))
        cosineCuveEndDot = always_redraw(lambda : Dot(fill_color = YELLOW, fill_opacity=0.8).scale(0.5).move_to(cosineCurveGraph.get_end()))

        # Sine curve plotting 
        axes1 = Axes(x_range=[0, 2*PI, PI/2], x_length=3, y_range=[-1.0, 1.0, 1], y_length=2, tips=False)
        axes1.add_coordinates(
            {
                PI/2 : MathTex(r"\frac{\pi}{2}"),
                PI : MathTex("\pi"),
                3*PI/2 : MathTex(r"\frac{3 \pi}{2}"),
                2*PI : MathTex("2 \pi")
            },
            {
                -1.0 : MathTex("-1"),
                0.0 : MathTex("0"),
                1.0 : MathTex("1"),
            }
        )
        axes1.move_to([1, -2, 0])    # Location of axes
        sineCurveGraph = always_redraw(lambda : axes1.get_graph(lambda x : np.sin(x), x_range=[0, self.e.get_value()], color=GREEN))
        sineCuveEndDot = always_redraw(lambda : Dot(fill_color = YELLOW, fill_opacity=0.8).scale(0.5).move_to(sineCurveGraph.get_end()))
        
        # self.play(LaggedStart(
        #             Create(axes0), run_time=3, lag_ratio=(0.5)
        # ))
        self.play(Create(axes0), Create(axes1))
        self.add(cosineCurveGraph, cosineCuveEndDot, sineCurveGraph, sineCuveEndDot)
        self.play(self.e.animate.set_value(2*PI), run_time=5, rate_functions=linear)
        self.wait(1)

