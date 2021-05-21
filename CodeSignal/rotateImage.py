def rotateImage(a):
    a.reverse() # O(n), reverse the values in the arrays aswell as each array in the array

    for i in range(len(a)): # O(n) & O(1) space complexity. 
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j] #Transpose all elements diagonally. Vlaues in the middle swap with themselves
    return a
