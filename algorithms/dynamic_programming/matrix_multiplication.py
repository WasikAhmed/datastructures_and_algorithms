# Matrix Multiplication
def matrix_multiplication(matrix1, matrix2):
    m1_rows, m1_cols = len(matrix1), len(matrix1[0]),
    m2_rows, m2_cols = len(matrix2), len(matrix2[0]),

    if m1_cols != m2_rows:
        return "Error: Incompatible matrices for multiplication"

    # initializing result matrix with zeros
    result = [[0 for _ in range(m2_cols)] for _ in range(m1_rows)]

    for i in range(m1_rows):
        for j in range(m2_cols):
            for k in range(m1_cols):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


if __name__ == '__main__':
    matrix_A = [[1, 2],
                [3, 4]]
    matrix_B = [[5, 6],
                [7, 8]]

    result = matrix_multiplication(matrix_A, matrix_B)
    print(result)
