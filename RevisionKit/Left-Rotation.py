# here's an array, rotate it left 3 times:
# [1, 2, 3, 4, 5]
# [2, 3, 4, 5, 1]
# [3, 4, 5, 1, 2]
# [4, 5, 1, 2, 3]

def rotateLeft(arr):
    # Clue Use a for loop with no value, eg for _ in range(x). Just for practice
    zip(*arr)
    print(arr)

rotateLeft([[1, 2, 3, 4, 5],
            [2, 3, 4, 5, 1], 
            [3, 4, 5, 1, 2], 
            [4, 5, 1, 2, 3]])