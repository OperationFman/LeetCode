from collections import Counter

def firstNotRepeatingCharacter(s):
    array = list(s) # O(n)
    
    count = dict(Counter(array)) # )(n)
    
    for i in array: # O(n)
        if count[i] == 1: # If an element in the count is 1 it'll be non-repeateing. 
            return i # Going through the array again will show that first non-repeating character
            
    return '_'
