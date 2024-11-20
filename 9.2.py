def transform_matrix(matrix):
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("Матрица должна быть квадратной.")
    diagonal_elements = [matrix[i][i] for i in range(n)]
    trace = sum(diagonal_elements)
    transformed_matrix = []
    for i in range(n):
        if i % 2 == 0:  
            transformed_matrix.append(
                [element / trace for element in matrix[i]]
            )
        else:  
            transformed_matrix.append(list(matrix[i]))
    
    return diagonal_elements, trace, transformed_matrix
matrix = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]
diagonal_elements, trace, transformed_matrix = transform_matrix(matrix)
print("Диагональные элементы:", diagonal_elements)
print("След матрицы:", trace)
print("Преобразованная матрица:")
for row in transformed_matrix:
    print(' '.join(map(str, row)))
