def restore_matrix(array):
    n = 0
    while (n * (n + 1)) // 2 != len(array):
        n += 1

    matrix = [[0] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = array[index]
            matrix[j][i] = array[index]  
            index += 1
    for row in matrix:
        print(' '.join(map(str, row)))
array = [1, 2, 3, 4, 5, 6]
restore_matrix(array)
