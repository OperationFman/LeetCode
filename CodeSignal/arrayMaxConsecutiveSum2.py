def arrayMaxConsecutiveSum2(inputArray):
    """ [2, 5, -11, 6] """
    maxSum = inputArray.pop(0)
    currSum = maxSum
    
    for i in inputArray:
        if i + currSum > i:
            currSum += i  
        else:
            currSum = i
        maxSum = max(maxSum, currSum)
    maxSum = max(maxSum, currSum)
    
    return maxSum
