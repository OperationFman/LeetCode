def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    array = [[0 for _ in range(rows)] for __ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            array[j][i] = matrix[i][j]
    return array

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
