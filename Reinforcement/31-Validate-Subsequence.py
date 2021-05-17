def isValidSubsequence(array, sequence):
    try:
        toRemove = [] # I trick I've found is add indexes marked for removal to a list
        sequenceCopy = sequence.copy() # Make a new copy as this will be deleted from
        
        for i, v in enumerate(array):
            if v in sequenceCopy: # If the sequence value is in the array then delete it from the copy
                sequenceCopy.pop(sequenceCopy.index(v))
            else: # otherwise it 'gets in the way' of our sequence so mark it for removal
                toRemove.append(i) # We don;t remove it here as that stuffs up running the for loop

		toRemove.sort(reverse=True) # Reversing makes it largest to smallest so we dont wreck the indexes order as we iterate
        for i in toRemove:
            array.pop(i) # Go through from descending and delete them
        
        if array == sequence: # If they match then we have a sequence, even if it's one element
            return True
        else: # If they dont then we know they wern't subsequences
            return False
    except:
        return False # If the above didn;t work it was probably False anyway