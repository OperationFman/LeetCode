# Given an array a that contains only numbers in the range from 1 to a.length, 
# find the first duplicate number for which the second occurrence 
# has the minimal index. In other words, if there are more than 1 duplicated numbers, 
# return the number for which the second occurrence has a smaller index than the 
# second occurrence of the other number does. If there are no such elements, return -1.

def firstDuplicate(a):
    pass
    # Clue: Reading/writing to a hastable (Set) is O(n)
    # Iterate over the array, if it's in the set (Checking is O(1)) then you found the dup, if not, add it to thr set
    setty = set()
    
    for i in a:
        if i not in setty:
            setty.add(i)
        else:
            return i

print(firstDuplicate([1,2,3,4,5,6,7,8,9,9]))
