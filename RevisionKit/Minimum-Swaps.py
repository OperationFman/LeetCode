# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] 
# without any duplicates. You are allowed to swap any two elements. 
# Find the minimum number of swaps required to sort the array in ascending order.

def minimumSwaps(arr):
    pass
    # Clue: While loop until a sorted array matches what you're about to do
    # Go through with range(arr) -1 and do a bubble sort-style swap and incrmeent a counter
    count = 0
    sorty = sorted(arr)
    print(sorty)

    while arr != sorty:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                store = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = store
                count += 1

    print(count)

minimumSwaps([2,3,4,5,1])
    