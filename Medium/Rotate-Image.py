class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        newArray = []
        for _ in matrix:
            newArray.append([])
        for i in range(len(matrix)):
            for element in matrix[i]:
                newArray[matrix[i].index(element)].insert(0, element) 
        for x in range(len(matrix)):
            matrix[x] = newArray[x]

# Above isn't perfect
# Below is, Rafactor!!

class Solution2:
    def rotate(self, matrix):
		#Transposing the given matrix
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
		#Reverse the transposed matrix 
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]