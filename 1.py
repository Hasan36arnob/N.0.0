from manim import *

class MathViralVideo(Scene):
    def construct(self):
        # 1. Introduction (15 seconds)
        title = Text("The Pythagorean Theorem", font_size=48, color=YELLOW)
        subtitle = Text("Mathematics Made Visual", font_size=32, color=BLUE)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title), run_time=2)
        self.wait(1)
        self.play(Write(subtitle), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=1.5)
        
        # 2. Create the Right Triangle (20 seconds)
        triangle_title = Text("Right Triangle", font_size=36, color=WHITE).to_edge(UP)
        self.play(Write(triangle_title), run_time=1.5)
        
        triangle = Polygon(ORIGIN, 3*RIGHT, 4*UP, color=BLUE, stroke_width=4)
        labels = VGroup(
            Text("a").next_to(triangle, DOWN),
            Text("b").next_to(triangle, LEFT),
            Text("c").next_to(triangle.get_center(), UR)
        )

        self.play(Create(triangle), run_time=2)
        self.wait(1)
        self.play(Write(labels), run_time=2)
        self.wait(2)
        
        # Explain sides (15 seconds)
        explanation1 = Text("Sides: a, b (legs), c (hypotenuse)", font_size=24).to_edge(DOWN)
        self.play(Write(explanation1), run_time=2)
        self.wait(3)
        self.play(FadeOut(explanation1), run_time=1)
        
        # 3. Building the Squares (30 seconds)
        squares_title = Text("Building Squares on Each Side", font_size=36, color=WHITE).to_edge(UP)
        self.play(ReplacementTransform(triangle_title, squares_title), run_time=1.5)
        
        sq_a = Square(side_length=3).next_to(triangle, DOWN, buff=0).set_fill(YELLOW, opacity=0.5)
        sq_b = Square(side_length=4).next_to(triangle, LEFT, buff=0).set_fill(GREEN, opacity=0.5)
        
        self.play(FadeIn(sq_a), run_time=1.5)
        area_a = Text("Area = a²").next_to(sq_a, DOWN)
        self.play(Write(area_a), run_time=1.5)
        self.wait(2)
        
        self.play(FadeIn(sq_b), run_time=1.5)
        area_b = Text("Area = b²").next_to(sq_b, LEFT)
        self.play(Write(area_b), run_time=1.5)
        self.wait(3)
        
        # 4. The Hypotenuse Square (25 seconds)
        sq_c = Square(side_length=5).rotate(np.arctan(4/3))
        sq_c.move_to(triangle.get_center() + [0.8, 0.6, 0]).set_fill(RED, opacity=0.5)
        
        self.play(ReplacementTransform(VGroup(sq_a.copy(), sq_b.copy()), sq_c), run_time=2.5)
        area_c = Text("Area = c²").next_to(sq_c, UR)
        self.play(Write(area_c), run_time=1.5)
        self.wait(3)
        
        # 5. The Big Reveal (20 seconds)
        reveal_title = Text("The Magic Formula", font_size=36, color=YELLOW).to_edge(UP)
        self.play(ReplacementTransform(squares_title, reveal_title), run_time=1.5)
        
        formula = Text("a² + b² = c²", font_size=48).move_to(ORIGIN)
        self.play(Write(formula), run_time=2)
        self.wait(2)
        
        # Visual proof (15 seconds)
        proof_text = Text("3² + 4² = 5²", font_size=32, color=GREEN).next_to(formula, DOWN)
        calculation = Text("9 + 16 = 25", font_size=32, color=GREEN).next_to(proof_text, DOWN)
        
        self.play(Write(proof_text), run_time=1.5)
        self.wait(1)
        self.play(Write(calculation), run_time=1.5)
        self.wait(3)
        
        # 6. Real-world Applications (25 seconds)
        apps_title = Text("Real-World Applications", font_size=36, color=WHITE).to_edge(UP)
        self.play(ReplacementTransform(reveal_title, apps_title), run_time=1.5)
        
        applications = VGroup(
            Text("• Architecture & Construction", font_size=24),
            Text("• Navigation & GPS", font_size=24),
            Text("• Computer Graphics", font_size=24),
            Text("• Physics & Engineering", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.8)
        
        self.play(FadeOut(formula), FadeOut(proof_text), FadeOut(calculation), run_time=1.5)
        self.play(Write(applications), run_time=3)
        self.wait(5)
        
        # 7. Conclusion (15 seconds)
        conclusion_title = Text("Conclusion", font_size=36, color=YELLOW).to_edge(UP)
        self.play(ReplacementTransform(apps_title, conclusion_title), run_time=1.5)
        
        final_message = Text("One of mathematics' most beautiful theorems", font_size=28, color=BLUE)
        self.play(Write(final_message), run_time=2)
        self.wait(5)
        
        # Final fade out (5 seconds)
        self.play(
            FadeOut(conclusion_title),
            FadeOut(final_message),
            FadeOut(triangle),
            FadeOut(labels),
            FadeOut(sq_a),
            FadeOut(sq_b),
            FadeOut(sq_c),
            FadeOut(area_a),
            FadeOut(area_b),
            FadeOut(area_c),
            FadeOut(applications),
            run_time=3
        )
        self.wait(2)