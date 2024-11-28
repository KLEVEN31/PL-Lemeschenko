def restore_matrix(array):
    n = 0
    total_elements = len(array)
    while (n * (n + 1)) // 2 < total_elements:
        n += 1
    matrix = [[0] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = array[index]
            index += 1
    for i in range(1, n):
        for j in range(i):
            matrix[i][j] = matrix[j][i]
    return matrix
def read_input(file_name):
    with open(file_name, 'r') as file:
        line = file.readline()
        array = list(map(int, line.split()))
    return array
def write_output(matrix, file_name):
    with open(file_name, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')
input_file = 'Максим_Y-244_vvod.txt'
output_file = 'Максим_Y-244_vivod.txt'
input_array = read_input(input_file)
matrix = restore_matrix(input_array)
write_output(matrix, output_file)

