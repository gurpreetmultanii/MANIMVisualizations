from manim import *
import numpy as np
import math

class FinalVisualization(MovingCameraScene):
    def construct(self):
        self.play(self.camera.frame.animate.set_height(20))
        # Define the updated transformation matrix.
        transformation_matrix = [[2, 1],
                                 [0, 4]]
        
        ##############################
        # Part 1: Setup – Two Planes & Basis Vectors
        ##############################
        # Create the stationary (background) plane.
        stationary_plane = NumberPlane(
            x_range=[-20, 20, 1],
            y_range=[-20, 20, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            }
        )
        stationary_plane.set_z_index(0)
        
        # Create the transformable (foreground) plane.
        transform_plane = NumberPlane(
            x_range=[-20, 20, 1],
            y_range=[-20, 20, 1],
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 2,
                "stroke_opacity": 0.7,
            }
        )
        transform_plane.set_z_index(1)
        
        self.play(Create(stationary_plane), run_time=2)
        self.play(Create(transform_plane), run_time=2)
        self.wait(1)
        
        # Draw standard basis vectors on the transformable plane.
        i_vector = Arrow(ORIGIN, RIGHT, buff=0, color=RED)
        j_vector = Arrow(ORIGIN, UP, buff=0, color=GREEN)
        i_vector.set_z_index(2)
        j_vector.set_z_index(2)
        self.play(GrowArrow(i_vector), GrowArrow(j_vector), run_time=2)
        self.wait(1)
        
        ##############################
        # Part 2: Transform the Foreground Objects and then Revert
        ##############################
        # Display the transformation matrix in the upper left corner.
        matrix_tex = MathTex(
            r"T = \begin{pmatrix} 2 & 1 \\ 0 & 4 \end{pmatrix}",
            font_size=40
        )
        matrix_tex.to_corner(UL)
        self.play(Write(matrix_tex), run_time=2)
        self.wait(1)
        
        # Animate transformation of the transformable plane and basis vectors.
        self.play(
            transform_plane.animate.apply_matrix(transformation_matrix),
            i_vector.animate.apply_matrix(transformation_matrix),
            j_vector.animate.apply_matrix(transformation_matrix),
            run_time=3
        )
        self.wait(3)
        
        # Immediately revert the transformed foreground objects back to their original state.
        self.remove(transform_plane, i_vector, j_vector)
        # Recreate original transformable plane and basis vectors.
        original_plane = NumberPlane(
            x_range=[-20, 20, 1],
            y_range=[-20, 20, 1],
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 2,
                "stroke_opacity": 0.7,
            }
        )
        original_plane.set_z_index(1)
        original_i = Arrow(ORIGIN, RIGHT, buff=0, color=RED)
        original_j = Arrow(ORIGIN, UP, buff=0, color=GREEN)
        original_i.set_z_index(2)
        original_j.set_z_index(2)
        self.add(original_plane, original_i, original_j)
        transform_plane = original_plane
        i_vector = original_i
        j_vector = original_j
        self.wait(1)
        
        ##############################
        # Part 3: Random Vector with Its Span, then Transform (Except Span)
        ##############################
        # Draw a random vector w = (2,1) on the untransformed plane.
        rand_vec = Arrow(ORIGIN, [2, 1, 0], buff=0, color=BLUE)
        rand_vec.set_z_index(2)
        rand_label = MathTex(r"\vec{w}").next_to(rand_vec.get_end(), UR, buff=0.1)
        rand_label.set_z_index(2)
        
        # Draw its span as a solid line that covers the entire grid.
        # For vector (2,1), intersections with the grid occur at (20,10) and (-20,-10).
        span_line_pos = Line(ORIGIN, np.array([20, 10, 0]), color=PURPLE, stroke_width=6)
        span_line_neg = Line(ORIGIN, np.array([-20, -10, 0]), color=PURPLE, stroke_width=6)
        span = VGroup(span_line_pos, span_line_neg)
        span.set_z_index(1)
        
        self.play(GrowArrow(rand_vec), Write(rand_label), run_time=2)
        self.play(Create(span), run_time=2)
        self.wait(1)
        
        # Apply the transformation (T) to the transformable plane, the basis vectors, and the random vector.
        # (The span and stationary plane remain unchanged.)
        self.play(
            transform_plane.animate.apply_matrix(transformation_matrix),
            i_vector.animate.apply_matrix(transformation_matrix),
            j_vector.animate.apply_matrix(transformation_matrix),
            rand_vec.animate.apply_matrix(transformation_matrix),
            run_time=3
        )
        
        # Update the random vector's label to show T applied.
        transformed_rand_label = MathTex(r"T\vec{w}").next_to(rand_vec.get_end(), UR, buff=0.1)
        transformed_rand_label.set_color(BLUE)
        self.play(ReplacementTransform(rand_label, transformed_rand_label), run_time=1.5)
        self.wait(2)
        
        self.play(FadeOut(matrix_tex), run_time=1.5)
        self.wait(2)
        
        ##############################
        # Part 4: Revert to Original Setup and Apply New Transformation with Vector (1,2)
        ##############################
        # Immediately revert back to the original setup (as in Part 1) without any transitions.
        self.clear()
        
        # Recreate the stationary (background) plane.
        stationary_plane = NumberPlane(
            x_range=[-20, 20, 1],
            y_range=[-20, 20, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            }
        )
        stationary_plane.set_z_index(0)
        
        # Recreate the transformable (foreground) plane.
        transform_plane = NumberPlane(
            x_range=[-20, 20, 1],
            y_range=[-20, 20, 1],
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 2,
                "stroke_opacity": 0.7,
            }
        )
        transform_plane.set_z_index(1)
        
        # Instantly add the stationary and transformable planes.
        self.add(stationary_plane, transform_plane)
        
        # Add standard basis vectors without transition.
        i_vector = Arrow(ORIGIN, RIGHT, buff=0, color=RED)
        j_vector = Arrow(ORIGIN, UP, buff=0, color=GREEN)
        i_vector.set_z_index(2)
        j_vector.set_z_index(2)
        self.add(i_vector, j_vector)
        
        # Add the transformation matrix text in the upper left of the screen.
        matrix_tex2 = MathTex(r"T = \begin{pmatrix} 2 & 1 \\ 0 & 4 \end{pmatrix}", font_size=40)
        matrix_tex2.to_corner(UL)
        self.add(matrix_tex2)
        
        # Animate the addition of the new vector (1,2).
        new_vector = Arrow(ORIGIN, [1, 2, 0], buff=0, color=ORANGE)
        new_vector.set_z_index(2)
        self.play(GrowArrow(new_vector), run_time=2)
        
        # Animate the drawing of its span as a solid line covering the entire grid.
        # For the new vector (1,2), intersections occur at (10,20) and (-10,-20).
        new_span_line_pos = Line(ORIGIN, np.array([10, 20, 0]), color=PURPLE, stroke_width=6)
        new_span_line_neg = Line(ORIGIN, np.array([-10, -20, 0]), color=PURPLE, stroke_width=6)
        new_span = VGroup(new_span_line_pos, new_span_line_neg)
        new_span.set_z_index(1)
        self.play(Create(new_span), run_time=2)
        
        # Apply the transformation in one go to the transformable plane, the two standard basis vectors, and the new vector.
        # (The stationary plane and the new span remain unchanged.)
        self.play(
            transform_plane.animate.apply_matrix(transformation_matrix),
            i_vector.animate.apply_matrix(transformation_matrix),
            j_vector.animate.apply_matrix(transformation_matrix),
            new_vector.animate.apply_matrix(transformation_matrix),
            run_time=3
        )
        self.wait(2)
        
        ##############################
        # Part 5: Additional Vectors, Extra (2,1) Element, and Text Labels
        ##############################
        # First revert back to original setup using the provided lines.
        self.clear()
        
        # Recreate the stationary (background) plane.
        stationary_plane = NumberPlane(
            x_range=[-20, 20, 1],
            y_range=[-20, 20, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            }
        )
        stationary_plane.set_z_index(0)
        
        # Recreate the transformable (foreground) plane.
        transform_plane = NumberPlane(
            x_range=[-20, 20, 1],
            y_range=[-20, 20, 1],
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 2,
                "stroke_opacity": 0.7,
            }
        )
        transform_plane.set_z_index(1)
        
        # Instantly add the stationary and transformable planes.
        self.add(stationary_plane, transform_plane)
        
        # Add standard basis vectors without transition.
        i_vector = Arrow(ORIGIN, RIGHT, buff=0, color=RED)
        j_vector = Arrow(ORIGIN, UP, buff=0, color=GREEN)
        i_vector.set_z_index(2)
        j_vector.set_z_index(2)
        
        # Add the transformation matrix text in the upper left of the screen.
        matrix_tex2 = MathTex(r"T = \begin{pmatrix} 2 & 1 \\ 0 & 4 \end{pmatrix}", font_size=40)
        matrix_tex2.to_corner(UL)
        self.add(matrix_tex2)
        
        # --- With transitions, add 10 vectors in the direction (1,2) (and 10 in the opposite direction) ---
        pos_arrows = VGroup()
        for k in range(1, 21):
            # Each arrow has length k along the unit vector (1,2)/√5.
            arrow = Arrow(ORIGIN, k * np.array([1/math.sqrt(5), 2/math.sqrt(5), 0]), buff=0, color=ORANGE)
            arrow.set_z_index(2)
            pos_arrows.add(arrow)
            self.play(GrowArrow(arrow), run_time=0.2)
        
        neg_arrows = VGroup()
        for k in range(1, 21):
            arrow = Arrow(ORIGIN, k * np.array([-1/math.sqrt(5), -2/math.sqrt(5), 0]), buff=0, color=ORANGE)
            arrow.set_z_index(2)
            neg_arrows.add(arrow)
            self.play(GrowArrow(arrow), run_time=0.2)
        
        # --- Also, add the vectors along the x-axis in the same way ---
        x_pos_arrows = VGroup()
        for k in range(1, 21):
            arrow = Arrow(ORIGIN, k * np.array([1, 0, 0]), buff=0, color=ORANGE)
            arrow.set_z_index(2)
            x_pos_arrows.add(arrow)
            self.play(GrowArrow(arrow), run_time=0.2)
        
        x_neg_arrows = VGroup()
        for k in range(1, 21):
            arrow = Arrow(ORIGIN, k * np.array([-1, 0, 0]), buff=0, color=ORANGE)
            arrow.set_z_index(2)
            x_neg_arrows.add(arrow)
            self.play(GrowArrow(arrow), run_time=0.2)
        
        # --- Also add the solid line and a single vector in the direction (2,1) (like Part 3) ---
        arrow_21 = Arrow(ORIGIN, [2, 1, 0], buff=0, color=BLUE)
        arrow_21.set_z_index(2)
        self.play(GrowArrow(arrow_21), run_time=0.2)
        span21_line_pos = Line(ORIGIN, np.array([20, 10, 0]), color=PURPLE, stroke_width=6)
        span21_line_neg = Line(ORIGIN, np.array([-20, -10, 0]), color=PURPLE, stroke_width=6)
        span21 = VGroup(span21_line_pos, span21_line_neg)
        span21.set_z_index(1)
        self.play(Create(span21), run_time=0.2)
        
        self.wait(1)
        
        # Apply the same transformation to all objects except the stationary_plane.
        self.play(
            transform_plane.animate.apply_matrix(transformation_matrix),
            pos_arrows.animate.apply_matrix(transformation_matrix),
            neg_arrows.animate.apply_matrix(transformation_matrix),
            x_pos_arrows.animate.apply_matrix(transformation_matrix),
            x_neg_arrows.animate.apply_matrix(transformation_matrix),
            arrow_21.animate.apply_matrix(transformation_matrix),
            run_time=3
        )
        self.wait(1)
        
        # --- After the transformation, add text labels with transitions ---
        text_x = Text("Stretched by Factor of 2", font_size=50)
        text_x.next_to(x_pos_arrows[4], UP, buff=0.3)
        
        text_12 = Text("Stretched by Factor of 4", font_size=50)
        text_12.next_to(pos_arrows[1], UP, buff=0.3)
        
        text_21 = Text("Not on its Original Span", font_size=50)
        text_21.next_to(arrow_21.get_end(), RIGHT, buff=0.3)
        
        self.play(Write(text_x), Write(text_12), Write(text_21), run_time=2)
        self.wait(2)