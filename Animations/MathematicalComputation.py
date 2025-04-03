from manim import *

class DetailedEigenvalueExample(Scene):
    def construct(self):
        # Function to display a centered group of text and math with a short pause.
        def show_group(group, wait_time=2):
            group.move_to(ORIGIN)  # Center the group on screen
            self.play(Write(group))
            self.wait(wait_time)

        # 1. Title and Introduction
        title = Text("Eigenvalues & Eigenvectors: Mathematical Computation", font_size=36)
        show_group(VGroup(title), 3)
        self.play(FadeOut(title))

        # 2. Display the matrix A with explanation
        matrix_A = MathTex(r"A=\begin{pmatrix}2 & 1\\1 & 2\end{pmatrix}", font_size=48)
        explanation_A = Text("We start with our matrix A.", font_size=28)
        group_A = VGroup(matrix_A, explanation_A).arrange(DOWN, buff=0.5)
        show_group(group_A, 3)
        self.play(FadeOut(group_A))

        # 3. Introduce the Eigenvalue Equation
        eq_intro = Text("Recall the eigenvalue equation:", font_size=28)
        eigen_eq = MathTex(r"A\mathbf{x}=\lambda\mathbf{x}", font_size=48)
        group_eq = VGroup(eq_intro, eigen_eq).arrange(DOWN, buff=0.5)
        show_group(group_eq, 3)
        self.play(FadeOut(group_eq))

        # 4. Rearranging to obtain (A - λI)x = 0
        explanation_rearr = Text("We rewrite the equation as:", font_size=28)
        rearr_eq = MathTex(r"(A-\lambda I)\mathbf{x}=\mathbf{0}", font_size=48)
        group_rearr = VGroup(explanation_rearr, rearr_eq).arrange(DOWN, buff=0.5)
        show_group(group_rearr, 3)
        self.play(FadeOut(group_rearr))

        # 5. Write (A - λI) for our specific matrix A
        explanation_matrix = Text("For our matrix A, we have:", font_size=28)
        expr_matrix = MathTex(
            r"A-\lambda I=\begin{pmatrix}2-\lambda & 1\\1 & 2-\lambda\end{pmatrix}",
            font_size=48
        )
        group_matrix = VGroup(explanation_matrix, expr_matrix).arrange(DOWN, buff=0.5)
        show_group(group_matrix, 3)
        self.play(FadeOut(group_matrix))

        # 6. Determinant Condition for Non-trivial Solutions
        explanation_det = Text(
            "Non-trivial solutions exist only if the matrix is singular.\nThus, we set its determinant to zero:",
            font_size=28, t2c={'singular': YELLOW}
        )
        det_eq = MathTex(
            r"\det\left(\begin{pmatrix}2-\lambda & 1\\1 & 2-\lambda\end{pmatrix}\right)=0", font_size=48
        )
        group_det = VGroup(explanation_det, det_eq).arrange(DOWN, buff=0.5)
        show_group(group_det, 3)
        self.play(FadeOut(group_det))

        # 7. Expand the Determinant Step-by-Step
        step1 = Text("Compute the determinant:", font_size=28)
        det_step = MathTex(r"(2-\lambda)(2-\lambda)-1\cdot1=0", font_size=48)
        group_det1 = VGroup(step1, det_step).arrange(DOWN, buff=0.5)
        show_group(group_det1, 3)
        self.play(FadeOut(group_det1))

        # self.play(FadeOut(VGroup(group_det1, group_det2, group_det3, group_det4)))

        # 8. Factor the Characteristic Polynomial
        explanation_factor = Text("Factor the quadratic polynomial:", font_size=28)
        factor_eq = MathTex(r"(\lambda-1)(\lambda-3)=0", font_size=48)
        group_factor = VGroup(explanation_factor, factor_eq).arrange(DOWN, buff=0.5)
        show_group(group_factor, 3)
        self.play(FadeOut(VGroup(explanation_factor, factor_eq)))

        # 9. Solve for Eigenvalues
        explanation_eigen = Text("Setting each factor to zero gives the eigenvalues:", font_size=28)
        eigenvalues = MathTex(r"\lambda=1 \quad \text{or} \quad \lambda=3", font_size=48)
        group_eigen = VGroup(explanation_eigen, eigenvalues).arrange(DOWN, buff=0.5)
        show_group(group_eigen, 3)
        self.play(FadeOut(VGroup(group_eigen)))

        # 10. Finding the Eigenvector for λ = 1
        eig1_title = Text("Eigenvector for λ = 1", font_size=32)
        eig1_title.to_edge(UP)
        self.play(Write(eig1_title))

        explanation_eig1 = Text(
            "Substitute λ = 1 into (A - λI)x = 0:", font_size=28
        )
        eig1_eq = MathTex(
            r"(A-I)x=\begin{pmatrix}2-1 & 1\\1 & 2-1\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix}",
            font_size=48
        )
        group_eig1 = VGroup(explanation_eig1, eig1_eq).arrange(DOWN, buff=0.5)
        group_eig1.move_to(DOWN*0.5)
        show_group(group_eig1, 3)
        self.play(FadeOut(group_eig1))

        explanation_simplify1 = Text(
            "This simplifies to the system:\n1·x + 1·y = 0", font_size=28
        )
        system1 = MathTex(r"x+y=0", font_size=48)
        group_sys1 = VGroup(explanation_simplify1, system1).arrange(DOWN, buff=0.5)
        group_sys1.move_to(DOWN*0.5)
        show_group(group_sys1, 3)
        self.play(FadeOut(group_sys1))

        explanation_evec1 = Text(
            "Any nonzero vector satisfying x + y = 0 is valid.\nFor example, choose x=1, then y=-1.",
            font_size=28
        )
        evec1 = MathTex(r"\text{Eigenvector: } \begin{pmatrix}1\\-1\end{pmatrix}", font_size=48)
        group_evec1 = VGroup(explanation_evec1, evec1).arrange(DOWN, buff=0.5)
        group_evec1.move_to(DOWN*0.5)
        show_group(group_evec1, 3)
        self.play(FadeOut(VGroup(group_evec1, eig1_title)))

        # 11. Finding the Eigenvector for λ = 3
        eig2_title = Text("Eigenvector for λ = 3", font_size=32)
        eig2_title.to_edge(UP)
        self.play(Write(eig2_title))

        explanation_eig2 = Text(
            "Now substitute λ = 3 into (A - λI)x = 0:", font_size=28
        )
        eig2_eq = MathTex(
            r"(A-3I)x=\begin{pmatrix}2-3 & 1\\1 & 2-3\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix}",
            font_size=48
        )
        group_eig2 = VGroup(explanation_eig2, eig2_eq).arrange(DOWN, buff=0.5)
        group_eig2.move_to(DOWN*0.5)
        show_group(group_eig2, 3)
        self.play(FadeOut(group_eig2))

        explanation_simplify2 = Text(
            "This gives the system:\n(-1)x + 1·y = 0", font_size=28
        )
        system2 = MathTex(r"-x+y=0", font_size=48)
        group_sys2 = VGroup(explanation_simplify2, system2).arrange(DOWN, buff=0.5)
        group_sys2.move_to(DOWN*0.5)
        show_group(group_sys2, 3)
        self.play(FadeOut(group_sys2))

        explanation_evec2 = Text(
            "A solution is found by setting x=1, which forces y=1.",
            font_size=28
        )
        evec2 = MathTex(r"\text{Eigenvector: } \begin{pmatrix}1\\1\end{pmatrix}", font_size=48)
        group_evec2 = VGroup(explanation_evec2, evec2).arrange(DOWN, buff=0.5)
        group_evec2.move_to(DOWN*0.5)
        show_group(group_evec2, 3)
        self.play(FadeOut(VGroup(eig2_title, group_evec2)))

        # 12. Conclusion
        conclusion = Text(
            "We have computed the eigenvalues λ = 1 and λ = 3\nand found their corresponding eigenvectors.",
            font_size=28
        )
        final_group = VGroup(conclusion).arrange(DOWN, buff=0.5)
        show_group(final_group, 4)

        self.play(FadeOut(final_group))