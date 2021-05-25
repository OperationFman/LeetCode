def sumOfTwo(a, b, v):
    complements = set() # make an empty unqiue set, this makes lookups instant (Rather than 'find x in list', which is O(n))
    
    for i in a:
        complements.add(v - i) # taking a from v will show us a value that b must have in order to being a sumoftwo. Dups obviously won't be added
    
    for i in b:
        if i in complements: # For in set() is actually O(1), instant lookup
            return True
    
    return False