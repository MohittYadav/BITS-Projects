import numpy as np


def gram_schmidt_qr(mat):
    m, n = mat.shape

    if m <= n:
        raise ValueError("Matrix must have more rows than columns for QR decomposition.")

    Q = np.zeros_like(mat, dtype=float)
    R = np.zeros((n, n), dtype=float)

    for j in range(n):
        v = mat[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], mat[:, j])
            v = v - R[i, j] * Q[:, i]

        # Calculate the Euclidean norm without using np.linalg.norm
        norm_v = np.sqrt(np.sum(v ** 2))

        R[j, j] = norm_v
        Q[:, j] = v / norm_v

    return Q, R


# User input for dimensions
m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

# User input for matrix entries
A = np.zeros((m, n), dtype=float)
for i in range(m):
    for j in range(n):
        A[i, j] = float(input(f"Enter entry A[{i + 1},{j + 1}]: "))

# Check if m > n
if m <= n:
    raise ValueError("Number of rows (m) must be greater than number of columns (n) for QR decomposition.")

Q, R = gram_schmidt_qr(A)

print("Matrix A:")
print(A)
print("\nQ matrix:")
print(Q)
print("\nR matrix:")
print(R)
