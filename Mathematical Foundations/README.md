Numerical Methods & Linear Algebra Algorithms<br>
A comprehensive collection of Python implementations for fundamental numerical methods and linear algebra algorithms used in computational mathematics and machine learning.<br>

📚 Overview<br>
This repository contains implementations of core numerical algorithms covering matrix decompositions, optimization methods, and linear system solvers. Each implementation is designed for educational purposes with clear, readable code and practical examples.<br>

🔬 Algorithms Overview<br>
1. Matrix Decompositions<br>
Cholesky Decomposition<br>

Purpose: Decomposes symmetric positive definite matrices into lower triangular matrices

Key Features:

Custom implementation without numpy.linalg.cholesky

Matrix symmetry validation

Positive definiteness checking

Result verification

LU Decomposition

Purpose: Factorizes matrices into lower and upper triangular components

Key Features:

Elementary matrices tracking

Step-by-step decomposition

Manual verification support

QR Decomposition

Purpose: Orthogonal triangular decomposition using Gram-Schmidt process

Key Features:

Manual orthogonalization

Dimension validation (m > n requirement)

Matrix condition checking

2. Optimization Algorithms<br>
Gradient Descent<br>

Purpose: Minimizes multivariate functions using gradient information

Key Features:

3D visualization of optimization path

Customizable loss functions

Learning rate configuration

Convergence tracking

Gradient Descent with Armijo's Rule

Purpose: Enhanced gradient descent with adaptive step sizes

Key Features:

Armijo condition for step size selection

Better convergence guarantees

Student ID-based randomization

Quadratic optimization examples

3. Linear Algebra Solvers<br>
Linear Systems Solver<br>

Purpose: Solves systems of linear equations using Gaussian elimination

Key Features:

Row Echelon Form (REF) computation

Reduced Row Echelon Form (RREF) computation

Null space basis identification

Particular solution finding

Power Method<br>

Purpose: Finds dominant eigenvalues and eigenvectors

Key Features:

Iterative eigenvalue approximation

Eigenvector normalization

Sequential deflation for multiple eigenvalues

Convergence history tracking

🚀 Quick Start<br>
Prerequisites<br>
Python 3.7+

NumPy

Matplotlib (for optimization visualizations)

📊 Algorithm Details<br>
Cholesky Decomposition
Complexity: O(n³)

Applications: Solving linear systems, Monte Carlo methods, Kalman filters

Input: Symmetric positive definite matrix

Output: Lower triangular matrix L where A = LLᵀ

Gradient Descent<br>
Complexity: O(k⋅n) per iteration

Applications: Machine learning, function minimization

Features: Adaptive learning rates, convergence visualization

Power Method<br>
Complexity: O(n²) per iteration

Applications: Principal component analysis, vibration analysis

Convergence: Linear, rate depends on eigenvalue separation

🎯 Educational Value<br>
This collection serves as:

Learning Resource: Understand algorithm mechanics through implementation

Reference Code: Clean, documented implementations for academic use

Algorithm Comparison: Compare different approaches to similar problems

Visualization Aid: See optimization paths and convergence behavior

🔧 Customization
Each algorithm is designed for easy modification:

Change Objective Functions: Modify C(x) in gradient descent files

Adjust Parameters: Tune learning rates, iteration counts, tolerances

Extend Functionality: Add new matrix types or convergence criteria

Integrate with Other Systems: Use as building blocks for larger applications

📈 Performance Notes<br>
Numerical Stability: Algorithms include checks for ill-conditioned problems

Efficiency: Focus on clarity over optimization; suitable for medium-sized problems

Accuracy: Includes verification steps to validate results

Visualization: Optimization algorithms include 3D plotting capabilities

🤝 Contributing<br>
This is an educational repository. Suggestions for improvements, additional algorithms, or better documentation are welcome through issues and pull requests.
