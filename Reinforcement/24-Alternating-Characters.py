def alternatingCharacters(s):
    """ 'AABBAAAABBBB' """
    if s == '' or s == None: # If it's nothing, return nothing
        return 0

    count = 0
    array = list(s) # We want to iterate over an enumerated list rather than the string
    
    for i, v in enumerate(array): # Could be done using just the range but we're comfortable with enunmerate
        if i < len(array) - 1: # We're checking the value after i in the loop if they're the same
                                # But it will break if we check out-of-bounds, limiting i to one less stops this
            if array[i+1] == v: # Check if value after is different, if it is then we dont need to delete
                count += 1 # If it isnt, that value would be deleted
                
    return count
