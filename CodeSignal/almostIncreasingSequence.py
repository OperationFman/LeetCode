def almostIncreasingSequence(sequence):
    #Go through, remove element and see if the list is nowin order
    for i, v in enumerate(sequence):
        sequence.pop(i) # Remove the current index to test
        copy = sorted(set(sequence)) # Create a copy as a set to remove dupes (Dupes brak it anyway)
        if sequence == copy: # the sorted version will be sequencial, if the change tio sequence worked then it too will be sequential and thus match
            return True
        sequence.insert(i, v) # Put value back if not
    return False