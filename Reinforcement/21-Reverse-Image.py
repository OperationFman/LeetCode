class Solution:
    def rotate(self, matrix):
        """ [[1,2,3],[4,5,6],[7,8,9]] """
        for i in range(len(matrix)): # For each column
            for j in range(i,len(matrix)): # And each row
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j] # Swap Xs and Ys
                
        for i in range(len(matrix)): # For each comun again
            matrix[i] = matrix[i][::-1] # Do something