def matrixElementsSum(matrix):
    counter = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])): # needed to iterate over the matrix
            if matrix[i][j] != 0: # If it's a number 
                if i == 0: # Row 1 will enver have a nothing above it, so might aswell count it
                    counter += matrix[i][j]
                elif matrix[i - 1][j] != 0: # This is actually redundant now, if it exists then it's valid
                    counter += matrix[i][j]
            else:
                for x in range(len(matrix)): # If a ghost is found, set all values below to 0
                    matrix[x][j] = 0
    
    return counter