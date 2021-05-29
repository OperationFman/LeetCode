def makeArrayConsecutive2(statues):
    array = sorted(statues) # Easier to iterate
    count = 0
    
    for i in range(array[0], array[-1]): # In the end we want every possible number from the smallest to the large4st
        if i not in array: # If it index doesn;t show up it means it's missing, so count it
            count += 1
            
    return count