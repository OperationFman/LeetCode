def makingAnagrams(s1, s2):
    """ [a, b, c, d, e, f, g] & [ a, b, c] """
    big = max(list(s1), list(s2)) # We want to know the smallest since we'll be popping things from the lists
    small = min(list(s1), list(s2)) # Once the smallest is empty we knoe there's no more unique items to be 'anagramed'
    counter = 0 # Keep track of every delete
    
    while small != []: # When we iterating we delete elems. That shuffles them down one and makes them missed. 
        # So here we repeat until small is empty because every value will be popped becaused it matched or because it doesn't
        for i, v in enumerate(small): 
            if v in big: # if it's in the other array its an anagram so we delete both and move on
                small.pop(i)
                big.pop(big.index(v))
            else:
                small.pop(i) # if it's only in small then it's unique and counts toward our 'deletes'
                counter += 1
    
    counter += len(big) # Once small is empty, only uniques remain in big so every single one counts as deleted
    return counter