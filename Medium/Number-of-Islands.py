class Solution:
    def numIslands(self, grid):
        count = 0 # Will return the count of islands
        
        for i in range(len(grid)):
            for j in range(len(grid[i])): # only way to traverse a matrix
                if grid[i][j] == "1": # The first time we see a one we want to find all connecting 1's (Without tirggering the count)
                    count += 1
                    self.recurs(grid, i, j) # Start the first recursion. When it swaps all attached 1's to 0's we'll keep checking for a fresh '1'
        return count
    
    def recurs(self, grid, i, j): 
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0": # 3. Once all connecting values are 0, back out
            return # Entire island will be converted to 0. Breaks the recursion
        else:
            grid[i][j] = "0" # 1. Convert 1 to a zero
            self.recurs(grid, i+1, j) # 2. Check all connecting values and convert them
            self.recurs(grid, i-1, j)
            self.recurs(grid, i, j-1)
            self.recurs(grid, i, j+1)