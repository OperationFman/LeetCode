def minimumSwaps(arr):
    """ [4,3,1,2] """
    try:
        counter = 0 # Keeps track of the swaps
        
        while arr != sorted(arr): # Compare the arrays, if it's done it'll match the sorted one
            for i in range(len(arr) - 1): # We want to compare all but the last elements since that'd be out of range
                if arr[i] > arr[i + 1]: # Do the swap
                    store = arr[i + 1]
                    arr[i + 1] = arr[i]
                    arr[i] = store
                    counter += 1 # increment the counter
                    
        return counter
    except:
        return 0 # If something goesd wrong it was probably 0 anyway