# Given an array of integers, sort the array in ascending order using the Bubble 
# Print the following three lines:
# Array is sorted in X swaps.  
# First Element: Y
# Last Element: Z
# Where X, Y, Z are numbers


def countSwaps(a):
  """ [2, 1, 3] """
    # Clue: Follow the traditional method of bubble sort and run a counter for each swap.
  count = 0
  for i in range(len(a) - 1):
    for x in range(len(a) - i - 1):
      if a[x] > a[x + 1]:
        a[x], a[x + 1] = a[x + 1], a[x]
        count += 1
  
  print("Array is sorted in " + str(count) + " swaps")
  print("First Element: " + str(a[0]))
  print("Last Element: " + str(a[-1]))


countSwaps([1,2,3,5,4,6,1,7,2])