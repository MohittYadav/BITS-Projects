import numpy as np


# Function to perform LU decomposition with elementary matrices
def lu_decomposition_with_elementary(mat):
    n = mat.shape[0]
    L = np.eye(n)
    U = mat.copy()

    elementary_matrices = []

    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = U[i, k] / U[k, k]
            elementary_matrix = np.eye(n)
            elementary_matrix[i, k] = -factor
            elementary_matrices.append(elementary_matrix)
            U[i, k:] -= factor * U[k, k:]

    return L, U, elementary_matrices


# Get the matrix size from the user
n = int(input("Enter the size of the square matrix (n): "))

# Get matrix elements from the user
A = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        A[i, j] = float(input(f"Enter the element at position ({i + 1}, {j + 1}): "))

L, U, elementary_matrices = lu_decomposition_with_elementary(A)

# Verification
# assert np.allclose(A, np.dot(L, U))

print("\nMatrix A:")
print(A)
print("\nLower Triangular Matrix L:")
print(L)
print("\nUpper Triangular Matrix U:")
print(U)
print("\nElementary Matrices:")
for i, matrix in enumerate(elementary_matrices):
    print(f"E{i + 1}:\n{matrix}")
