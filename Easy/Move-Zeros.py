def move_zeros(array):
    nums, zeros = [], []
    
    for i in array:
        if i == 0:
            zeros.append(0)
        else:
            nums.append(i)
            
    return nums + zeros