# You have two integer arrays, a and b, and an integer target value v. 
# Determine whether there is a pair of numbers, where one number is taken 
# from a and the other from b, that can be added together to get a sum of v. 
# Return true if such a pair exists, otherwise return false.

def sumOfTwo(a, b, v):
    pass
    # Clue: Remove the value of v from each in a and add them to a set. Each result would be waht a value in b MUST equal if it exists
    # Remember, hashtables (sets) are O(1) lookup and write, so when you search each in b if it's in that set, it's instant