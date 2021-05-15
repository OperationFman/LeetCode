def countSwaps(a):
  """ [2, 1, 3] """
    count = 0 # Need a way to store each swap
    ordered = sorted(a) # Good to have a reference to an actually sorted list

    while a != ordered: # If the two dont match then more sorting needs to be done
        for i in range(len(a) - 1): # We want to iterate through the entire array but not the very last one as it would be out of range of the final loop
            if a[i] > a[i + 1]: # Check if the value after is lower, if it is then swap them
                store = a[i+1] # We're overwriting the after value so we store it
                a[i +1] = a[i] # Overite the after value with the current
                a[i] = store # Overwrite the current with the stored value
                count += 1 # Increment the counter
    print("Array is sorted in " + str(count) + " swaps.") # Must convert ints to strings so we can concatenate them
    print("First Element: " + str(ordered[0])) # Might aswell use the ordered list, no real reason other than absolute confidence it'll be right
    print("Last Element: " + str(ordered[-1]))
    return
