def allLongestStrings(inputArray):
    longs = []
    longs.append(inputArray.pop(0)) # We need something to compare, popping it removes it from the final product
    
    for i in inputArray:
        if len(i) > len(longs[0]): # If the length of an element is bigger, wipe away all others and replace
            longs = []
            longs.append(i)
        elif len(i) == len(longs[0]): # If length is the same, add element
            longs.append(i)
            
    return longs