def rotateLeft(d, arr):
    """ [5, 1, 2, 3, 4] """
    for _ in range(d): # Dont need the value of i, just need to loop the specified amount of times
        arr.append(arr[0]) # Put the first value on the end
        arr.pop(0) # Delete the first value
        
    return arr # Returned after all rotations, it could go endlessly