import numpy as np


# Function to perform Cholesky decomposition
def cholesky_decomposition_custom(mat):
    # Check if the matrix is square
    if mat.shape[0] != mat.shape[1]:
        print("\nMatrix is not square.")

    # Check if the matrix is symmetric
    if not np.allclose(mat, mat.T):
         raise ValueError("\nMatrix is not symmetric.")


    n = mat.shape[0]
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                sum_term = mat[i, j] - np.sum(L[i, :j] ** 2)
                if sum_term < 0:
                    raise ValueError("Matrix is not positive definite.")
                L[i, j] = np.sqrt(sum_term)
            else:
                L[i, j] = (mat[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]



    return L


# Function to verify A = LL^T
def verify_cholesky_decomposition(A, L):
    return np.allclose(A, np.dot(L, L.T))


def run_cholesky_test(n):
    # Get matrix elements from the user
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i, j] = float(input(f"Enter the element at position ({i + 1}, {j + 1}): "))

    # Perform Cholesky decomposition using custom implementation
    L_custom = cholesky_decomposition_custom(A)

    # Verification
    verification_result = verify_cholesky_decomposition(A, L_custom)

    print("\nMatrix A:")
    print(A)
    print("\nCholesky Decomposition (Custom):")
    print(L_custom)
    print("\nVerification Result (A = LL^T):", verification_result)


# Example usage
if __name__ == "__main__":
    n = int(input("Enter the size of the square matrix (n): "))
    run_cholesky_test(n)
