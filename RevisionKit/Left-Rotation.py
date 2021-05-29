# here's an array, rotate it left 3 times:
# [1, 2, 3, 4, 5]
# [2, 3, 4, 5, 1]
# [3, 4, 5, 1, 2]
# [4, 5, 1, 2, 3]

def rotLeft(a, d):
    for _ in range(d):
        a.append(a[0]) # Put first element on the back
        a.pop(0) # Delete first element
    return a

rotLeft([1, 2, 3, 4, 5], 4) # Rotate array 4 times

def rotRight(a, d):
    for _ in range(d):
        a.insert(0,a[-1])
        a.pop(-1)
    return a