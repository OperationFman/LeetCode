def firstDuplicate(a):
    sets = set() # Uses memory
    
    for i in a: # O(n) loop throgh once
        if i in sets: #Reading a set(Hashtable) is O(1). 
            return i
        else:
            sets.add(i) # Add to hashtable, O(n)
            
    return -1
    
    #O(n) + O(1) + O(n) = O(n) # Great!
