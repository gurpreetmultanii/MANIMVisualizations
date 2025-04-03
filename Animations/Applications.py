from manim import *
import numpy as np

class RepeatedTransformation(Scene):
    def construct(self):
        # Create a larger NumberPlane for better visibility of large vectors.
        plane = NumberPlane(
            x_range=[-20, 20, 1],
            y_range=[-20, 20, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        # Scale the plane to show more of the grid.
        self.add(plane.scale(0.5))

        # Display the transformation matrix in the top left corner.
        matrix_tex = MathTex(r"A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}")
        matrix_tex.to_corner(UL)
        self.add(matrix_tex)

        # Create a counter ValueTracker and counter display.
        counter_tracker = ValueTracker(0)
        counter_tex = always_redraw(lambda: MathTex(
            r"\text{Applied: }" + str(int(counter_tracker.get_value()))
        ).next_to(matrix_tex, DOWN))
        self.add(counter_tex)

        # Draw the full-screen line for eigenvector v2 (v2 = (1, -1)) in YELLOW.
        eigen2_full_line = Line(
            start=plane.c2p(20, 20),
            end=plane.c2p(-20, -20),
            color=YELLOW,
            stroke_width=2
        )
        self.add(eigen2_full_line)

        # Draw the eigenvector for v1.
        # Dominant eigenvector: v1 = (1, 1) (Eigenvalue: 3)
        eigen1_vec = Vector([1, 1], color=BLUE)
        eigen1_line = Line(
            start=plane.c2p(0, 0),
            end=plane.c2p(7, 1.2),
            color=BLUE
        )
        eigen1_label = MathTex(r"\vec{v}_1 \; \text{Eigenvalue: }3").next_to(eigen1_line.get_end(), UP)
        self.play(GrowArrow(eigen1_vec))
        self.add(eigen1_label)
        self.wait(0.5)

        # Draw the eigenvector for v2.
        # Secondary eigenvector: v2 = (1, -1) (Eigenvalue: 1)
        eigen2_vec = Vector([1, -1], color=GREEN)
        eigen2_line = Line(
            start=plane.c2p(0, 0),
            end=plane.c2p(7, -1.2),
            color=GREEN
        )
        eigen2_label = MathTex(r"\vec{v}_2 \; \text{Eigenvalue: }1").next_to(eigen2_line.get_end(), DOWN)
        self.play(GrowArrow(eigen2_vec))
        self.add(eigen2_label)
        self.wait(1)

        # Define the transformation matrix A as a NumPy array.
        A = np.array([[2, 1],
                      [1, 2]])

        # Create a group of 12 evenly spaced vectors around a circle of radius 0.5.
        vectors = VGroup()
        n = 12       # Number of vectors.
        radius = 0.5 # Circle radius.
        for i in range(n):
            angle = TAU * i / n  # TAU is 2π.
            vec = Vector([radius * np.cos(angle), radius * np.sin(angle)], color=RED)
            vectors.add(vec)

        self.add(vectors)
        self.wait(2)

        # Apply the transformation repeatedly without distorting the arrowheads.
        iterations = 5  # Number of repeated transformations.
        for _ in range(iterations):
            self.play(
                *[
                    vec.animate.put_start_and_end_on(
                        vec.get_start(),
                        # Compute the new endpoint by applying matrix A to the current endpoint's (x,y) coordinates.
                        np.append(A.dot(np.array(vec.get_end()[:2])), 0)
                    )
                    for vec in vectors
                ],
                # Increment the counter concurrently.
                counter_tracker.animate.increment_value(1),
                run_time=1
            )
            self.wait(0.75)

        self.wait(2)
