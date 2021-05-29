# You have two integer arrays, a and b, and an integer target value v. 
# Determine whether there is a pair of numbers, where one number is taken 
# from a and the other from b, that can be added together to get a sum of v. 
# Return true if such a pair exists, otherwise return false.

def sumOfTwo(a, b, v):
    pass
    # for each in a, v - a = x (add to set)
    # for each in b if each in set return true
    checker = set()
    for i in a:
        checker.add(v - i)
    
    for j in b:
        if j in checker:
            return True

    return False

print(sumOfTwo([1,2,3], [10, 20, 30], 42))
