def adjacentElementsProduct(inputArray):
    largest = inputArray[0] * inputArray[1] # Might aswell grab the first two, comparing them against themself won;t change anything
    for i in range(len(inputArray) - 1): # iterate all except last element
        if inputArray[i] * inputArray[i + 1] > largest: # If they're buigger update largest
            largest = inputArray[i] * inputArray[i + 1]
    return largest