def diagonalDifference(arr):
    """ [[11, 2, 4], 
        [4, 5, 6],
        [10, 8, -12]] """
    LToR = 0
    RtoL = 0
    length = len(arr[0]) - 1 # Here it starts a 2
    
    for i, v in enumerate(arr): # only need the index, probably should just use range
        LToR += arr[i][i] #As we iterate it grabs the diagonal value
        RtoL += arr[i][length] #While going through each subarray, grabs the last one
        length -= 1 # Decrementing length brings us 'in' by one
        
    return abs(LToR - RtoL) # Works out the difference for us