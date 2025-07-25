import numpy as np


# row_mult :: np.array, float -> np.array
# multiply a NumPy array by a number
def row_mult(row, num):
    return row * num


# row_sub :: np.array, np.array -> np.array
# subtract one NumPy array from another
def row_sub(row_left, row_right):
    return row_left - row_right


# row_neg :: np.array -> np.array
# negate a NumPy array
def row_neg(row_left):
    return row_mult(row_left, -1)


# mtx_mult_row :: np.array, int, float -> np.array
# multiply a row of the matrix by a number
def mtx_mult_row(mtx, row, num):
    mtx[row] = row_mult(mtx[row], num)
    return mtx


# mtx_sub_row :: np.array, int, int -> np.array
# subtract one row from another
def mtx_sub_row(mtx, row_dest, row_src):
    mtx[row_dest] = row_sub(mtx[row_dest], mtx[row_src])
    return mtx


# mtx_neg_row :: np.array, int -> np.array
# negate a row
def mtx_neg_row(mtx, row):
    mtx[row] = row_neg(mtx[row])
    return mtx


# is_row_echelon :: np.array -> bool
# check if a matrix is in row echelon form
def is_row_echelon(mtx):
    for i, row in enumerate(mtx):
        for j in range(i):
            if mtx[i, j] != 0:
                return False
    return True


# row_echelon :: np.array -> np.array
# calculate the row echelon form of the matrix
def row_echelon(mtx):
    temp_mtx = np.copy(mtx)

    def for_echelon(rw, col):
        for i, row in enumerate(temp_mtx[col + 1:], start=col + 1):
            if rw[col] == 0:
                continue
            relation = row[col] / rw[col]
            fst_multi = row_mult(rw, relation)
            temp_mtx[i] = row_sub(row, fst_multi)

    for i in range(len(mtx)):
        active_row = temp_mtx[i]
        for_echelon(active_row, i)

    # flatten out values very close to zero
    temp_mtx = np.where(np.abs(temp_mtx) < 1e-10, 0, temp_mtx)

    return temp_mtx


# reduced_row_echelon_form :: np.array -> np.array
# calculate the reduced row echelon form of the matrix

def reduced_row_echelon_form(mtx):
    temp_mtx = row_echelon(mtx)

    for i, row in enumerate(temp_mtx[::-1]):
        if np.sum(row) == 0:
            continue
        pivot_col = np.argmax(row != 0)
        pivot_row = len(mtx) - i - 1
        for j in range(pivot_row):
            if temp_mtx[j, pivot_col] != 0:
                relation = temp_mtx[j, pivot_col] / row[pivot_col]
                fst_multi = row_mult(row, relation)
                temp_mtx[j] = row_sub(temp_mtx[j], fst_multi)

    return temp_mtx


if __name__ == "__main__":
    while True:
        try:
            # Take user input for the number of rows (m) and columns (n)
            m = int(input("Enter the number of rows (m): "))
            n = int(input("Enter the number of columns (n): "))

            # Validate that m is less than n
            if m < n:
                break
            else:
                print("Error: m must be less than n. Please try again.")
        except ValueError:
            print("Error: Please enter valid integer values for m and n.")

    while True:
        try:
            # Take user input for the entries of the matrix A
            print(f"\nEnter the elements of A ({m} x {n}):")
            A = np.zeros((m, n))
            for i in range(m):
                for j in range(n):
                    while True:
                        try:
                            entries = float(input(f"Enter the value for element at position ({i + 1}, {j + 1}): "))
                            A[i, j] = entries
                            break
                        except ValueError:
                            print("Error: Please enter a valid numerical value.")

            # Take user input for the entries of the vector b
            print(f"\nEnter the elements of b ({m} x 1):")
            b = np.zeros((m, 1))
            for i in range(m):
                while True:
                    try:
                        entries = float(input(f"Enter the value for element at position ({i + 1}, 1): "))
                        b[i, 0] = entries
                        break
                    except ValueError:
                        print("Error: Please enter a valid numerical value.")

            # Construct augmented matrix [A | b]
            augmented_matrix = np.column_stack((A, b))

            # Retry performing Row Echelon Form (REF) with the new A and b
           # print("\nRetrying Row Echelon Form (REF) with new values:")

            current_row = 0
            pivot_columns = set()  # To store pivot column indices
            for col in range(n):
                # Find the pivot row
                pivot_row = current_row
                while pivot_row < m and augmented_matrix[pivot_row, col] == 0:
                    pivot_row += 1

                # If a pivot row is found, swap it with the current row
                if pivot_row < m:
                    augmented_matrix[[current_row, pivot_row]] = augmented_matrix[[pivot_row, current_row]]

                    # Make the diagonal element non-zero
                    if augmented_matrix[current_row, col] != 0:
                        scale_factor = 1.0 / augmented_matrix[current_row, col]
                        augmented_matrix[current_row] = row_mult(
                            augmented_matrix[current_row], scale_factor
                        )

                        # Eliminate non-zero values below the pivot
                        for i in range(current_row + 1, m):
                            multiplier = augmented_matrix[i, col]
                            augmented_matrix[i] = row_sub(
                                augmented_matrix[i], row_mult(augmented_matrix[current_row], multiplier)
                            )

                        pivot_columns.add(col)  # Track pivot columns
                        current_row += 1

            print("\nPivot Columns:")
            print(list(pivot_columns))
            non_pivot_columns = [col for col in range(n) if col not in pivot_columns]
            print("\nNon-Pivot Columns:")
            print(non_pivot_columns)

            break
        except ZeroDivisionError:
            print("Error: Division by 0. Please choose different values for matrix A and/or vector b.")

    # Print REF matrix
    print("\nRow Echelon Form (REF):")
    print(augmented_matrix)

    # Identify pivot and non-pivot columns
    pivot_columns = list(pivot_columns)
    non_pivot_columns = [col for col in range(n) if col not in pivot_columns]

    # Find the particular solution
    particular_solution = np.zeros((n, 1))
    for col in non_pivot_columns:
        particular_solution[col, 0] = 1  # Set non-pivot columns to 1



    # Retry performing Reduced Row Echelon Form (RREF) with the new A and b
    #print("\nRetrying Reduced Row Echelon Form (RREF) with new values:")
    augmented_matrix = reduced_row_echelon_form(augmented_matrix)

    # Print RREF matrix with new values
    print("\nReduced Row Echelon Form (RREF):")
    print(augmented_matrix)

    # Print particular solution
    print("\nParticular Solution:")
    print(particular_solution)


    # Find solutions to Ax = 0
    null_space_basis = np.zeros((n, n - m))
    for i, col in enumerate(non_pivot_columns):
        null_space_basis[col, i] = 1  # Set non-pivot columns to 1

    # Print null space basis
    print("\nNull Space Basis:")
    print(null_space_basis)
