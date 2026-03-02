from manim import *

class MathViralVideo(Scene):
    def construct(self):
        # 1. Create the Hook: A simple right triangle
        triangle = Polygon(ORIGIN, 3*RIGHT, 4*UP, color=BLUE)
        labels = VGroup(
            Text("a").next_to(triangle, DOWN),
            Text("b").next_to(triangle, LEFT),
            Text("c").next_to(triangle.get_center(), UR)
        )

        self.play(Create(triangle), Write(labels))
        self.wait(0.5)
        self.add_sound("click", time_offset=0.1)  # Sound effect for appearance
        self.wait(0.5)

        # 2. Transition to the "Secret" (The Squares)
        sq_a = Square(side_length=3).next_to(triangle, DOWN, buff=0).set_fill(YELLOW, opacity=0.5)
        sq_b = Square(side_length=4).next_to(triangle, LEFT, buff=0).set_fill(GREEN, opacity=0.5)
        
        # Hypothetically building the square on the hypotenuse
        sq_c = Square(side_length=5).rotate(np.arctan(4/3))
        sq_c.move_to(triangle.get_center() + [0.8, 0.6, 0]).set_fill(RED, opacity=0.5)

        self.play(FadeIn(sq_a), FadeIn(sq_b))
        self.add_sound("pop", time_offset=0.1)  # Sound effect for squares
        self.wait(0.3)
        self.play(ReplacementTransform(VGroup(sq_a, sq_b).copy(), sq_c))
        self.add_sound("whoosh", time_offset=0.1)  # Sound effect for transformation
        
        # 3. The Big Reveal: The Formula
        formula = Text("a² + b² = c²").to_edge(UP)
        self.play(Write(formula))
        self.add_sound("reveal", time_offset=0.1)  # Sound effect for formula reveal
        self.play(Indicate(formula))
        self.wait(1)
        
        # 4. Final conclusion with emphasis
        conclusion = Text("The Pythagorean Theorem", font_size=36).to_edge(DOWN)
        self.play(Write(conclusion))
        self.add_sound("success", time_offset=0.1)  # Final success sound
        self.wait(2)