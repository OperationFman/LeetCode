def isValidSubsequence(array, sequence):
    try:
        toRemove = []
        sequenceCopy = sequence.copy()
        
        for i, v in enumerate(array):
            if v in sequenceCopy:
                sequenceCopy.pop(sequenceCopy.index(v))
            else:
                toRemove.append(i)

		toRemove.sort(reverse=True)
        for i in toRemove:
            array.pop(i)
        
        if array == sequence:
            return True
        else:
            return False
    except:
        return False