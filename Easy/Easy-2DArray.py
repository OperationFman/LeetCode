def hourglassSum(arr):
    hourglass = []
    length = len(arr)-2
    for col in range(length):
        for row in range(length):
            hourglass.append(arr[col][row]+arr[col][row+1]+arr[col][row+2]+arr[col+1][row+1]+arr[col+2][row]+arr[col+2][row+1]+arr[col+2][row+2])    
    result = max(hourglass)
    return max(result)

# To make an empty 2D array easily:
rows = 8
cols = 8
array = [[0]*cols]*rows
print(array)