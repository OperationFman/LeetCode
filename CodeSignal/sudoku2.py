def sudoku2(grid):
    """ We have a partially filled sudoku puzzle. 
    There must be unqiue numbers in every line, column and 3x3 'sub-grid' """
    for line in grid: 
        if not check_unique(line): # Run every line through the checker
            return False
    
    for i in range(9): # Go down each row (Could also transpose and submit from here)
        if not check_unique([line[i] for line in grid]): #Swap columsn for rows and send them to be checked
            return False
        
    for i in range(0,9,3): # From 0 to 9 and in increments of 3
        for j in range(0, 9, 3): # Somehow grabs every value in the 3x3 grid and appends to an array for submission
            if not check_unique(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]):
                return False
            
    return True # if no falses triggered then it's legit

def check_unique(nums):
    s = set() # Empty set
    for num in nums:
        if num == '.': #Do nothing if it's a '.'
            continue 
            
        if num in s: # Add each item to the set, if it already exists then the puzzle is invalid
            return False
        s.add(num)
    return True # If it goes okay then return that the check is all g
        
