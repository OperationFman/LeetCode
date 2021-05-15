from collection import Counter

def makeAnagram(a, b):
    """ [a, b, c] & [c, b, a] """
    count_a = Counter(a) # Getting counts for each element
    count_b = Counter(b)
    count_a.subtract(count_b) # Somehow this will add any new counts and also place any from b not in a as negative???
    return sum(abs(i) for i in count_a.values()) # Makes everything positive and the total values, idk