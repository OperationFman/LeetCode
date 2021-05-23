from collections import Counter

def containsDuplicates(a):
    try:
        commons = Counter(a).most_common() # O(n)
        if commons[0][1] > 1: # ordering by most common, if it's more than 1 it must repeated
            return True
        else:
            return False
    except:
        return False # Boolean catchall