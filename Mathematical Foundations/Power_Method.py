import numpy as np


def power_method(matrix, iterations):
    x = np.random.rand(matrix.shape[0])
    eigenvalue_hist = []

    for i in range(iterations):
        x = np.dot(matrix, x)
        eigenvalue = np.linalg.norm(x)
        x /= eigenvalue
        eigenvalue_hist.append(eigenvalue)

    return eigenvalue_hist, x


# Part i: Generate Random Integer Matrix C (4x3) and Compute A₁ = CC
C = np.random.randint(10, size=(4, 3))
A1 = C.T @ C
print("Matrix C:")
print(C)

print("\nMatrix A1:")
print(A1)
vals, _ = np.linalg.eig(A1)
char_eq = np.poly1d(vals[::-1])
# Using a software package, compute the characteristic equation, eigenvalues, and eigenvectors of A₁
eigenvalues_A1, eigenvectors_A1 = np.linalg.eig(A1)

# Find largest eigenvalue and eigenvector of A₁ using Power Method
lambda1_history, x1 = power_method(A1, 10)
lambda1 = lambda1_history[-1]

# Normalize eigenvector \hat{x}_{1}
x1_normalized = x1 / np.linalg.norm(x1)
# Print the first 10 iterates of lambda_2 and x2_normalized
print("\nFirst 10 iterates of lambda_1 and x1_normalized:")
for i in range(10):
    print(f"Iteration {i + 1}: Lambda_1 = {lambda1_history[i]}, x1_normalized = {x1}")

# Comparison with Part i
print("Eigenvalues from Part i:", eigenvalues_A1)
print("Eigenvalue from Power Method (Part i):", lambda1)
print("Eigenvectors from Part i:", eigenvectors_A1)
print("Eigenvector from Power Method (Part i):", x1_normalized)

# Part ii: Construct Matrix A₂ and Find Largest Eigenvalue and Eigenvector using Power Method
A2 = A1 - np.outer(x1_normalized, x1_normalized) @ A1
lambda2_history, x2 = power_method(A2, 10)
lambda2 = lambda2_history[-1]
x2_normalized = x2 / np.linalg.norm(x2)

# Print the first 10 iterates of lambda_2 and x2_normalized
print("\nFirst 10 iterates of lambda_2 and x2_normalized:")
for i in range(10):
    print(f"Iteration {i + 1}: Lambda_2 = {lambda2_history[i]}, x2_normalized = {x2}")

# Part iii: Construct Matrix A₃ and Find Largest Eigenvalue and Eigenvector using Power Method
A3 = A1 - np.outer(x1_normalized, x1_normalized) @ A1 - np.outer(x2_normalized, x2_normalized) @ A1
lambda3_history, x3 = power_method(A3, 10)
lambda3 = lambda3_history[-1]
x3_normalized = x3 / np.linalg.norm(x3)

# Print the first 10 iterates of lambda_3 and x3_normalized
print("\nFirst 10 iterates of lambda_3 and x3_normalized:")
for i in range(10):
    print(f"Iteration {i + 1}: Lambda_3 = {lambda3_history[i]}, x3_normalized = {x3}")

# Comparison with Part i
print("\nEigenvalue from Power Method (Part iii):", lambda3)
print("Eigenvector from Power Method (Part iii):", x3_normalized)
