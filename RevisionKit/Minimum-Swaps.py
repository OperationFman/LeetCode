# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] 
# without any duplicates. You are allowed to swap any two elements. 
# Find the minimum number of swaps required to sort the array in ascending order.

def minimumSwaps(arr):
    # Clue: While loop until a sorted array matches what you're about to do
    # Go through with range(arr) -1 and do a bubble sort-style swap and incrmeent a counter
    res = 0
    arr = [x-1 for x in arr] # Reduces everything by 1 for some reason
    value_idx = {x:i for i, x in enumerate(arr)}
    for i, x in enumerate(arr):
        if i != x:
            to_swap_idx = value_idx[i]
            arr[i], arr[to_swap_idx] = i, x
            value_idx[i] = i
            value_idx[x] = to_swap_idx
            res += 1
    print(res)
    return res

minimumSwaps([2,3,4,5,1])
    