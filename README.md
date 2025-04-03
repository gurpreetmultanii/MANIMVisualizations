# MANIMVisualizations

This repository contains a series of MANIM animations that illustrate the concept of eigenvectors and eigenvalues. The **Animations** folder includes scripts for different sections of a presentation, each highlighting a unique aspect of eigenvectors, from definitions to real-world applications.

1. **Applications.py**  
   Demonstrates how repeated transformations or other engineering/real-world problems can be understood by focusing on the dominant eigenvector. Includes an example of how vectors converge to an eigenvector after multiple iterations of a matrix transformation.

2. **GeometricInterpretation.py**  
   Visualizes how a transformation matrix affects various vectors. Highlights how eigenvectors remain collinear with their original span, while non-eigenvectors are “kicked off” their span under transformation.

3. **DetailsAndIntuitionVisualization.py**  
   Provides a foundational understanding of eigenvectors, showing basic transformations using standard basis vectors and random vectors. This section helps build intuition by distinguishing how eigenvectors behave compared to non-eigenvectors.

4. **MathematicalComputation.py**  
   Demonstrates the algebraic steps for computing eigenvalues and eigenvectors—from defining the characteristic polynomial to factoring it and finding the eigenvalues, then solving for the corresponding eigenvectors.

## Getting Started

1. **Clone the Repository**
   ```
   git clone https://github.com/your_username/eigenvectors-visualization.git
    ```

2. **Navigate to the Project Directory**    
    ```
    cd eigenvectors-visualization
    ```
3. **Set up Your Python Environment**

   It is recommended to use a virtual environment (e.g., venv or conda).

   Install MANIM (Community Edition) and other required dependencies (e.g., NumPy, Sympy).
   ```
   pip install manim
   pip install numpy
   pip install sympy
   ```

   Check the Manim Community Documentation for the correct installation steps corresponding to your OS and Python version.

5. **How to Run Each Script**

    All the animation scripts are located in the Animations folder. Below is an example command to render a scene from a specific Python file:

    ```
    cd Animations
    
    manim -p -ql DetailsAndIntuitionVisualization.py DetailsAndIntuitionScene
    
    -p automatically previews the video after rendering.

    -ql renders at low quality (faster). You can use -qm or -qh for medium/high quality.

    Tip: Each file may contain multiple scenes. Replace DetailsAndIntuitionScene with the name of the scene class you want to render.
    ```

