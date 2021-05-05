class Solution:
    def moveZeroes(self, nums):
        """ [0,1,0,3,12] """
        zeros = [] # Place to hold all the zeros
        for i, v in enumerate(nums): # Need index and value
            if v == 0: 
                nums.pop(i) # Remove the zero from nums and add it to zeros
                zeros.append(0)
                
        for i, v in enumerate(nums): # This shouldn't be needed but do it again
            if v == 0:
                nums.pop(i)
                zeros.append(0)
        
        return nums.extend(zeros) # Adds lists together, simply adding normally doesn;t work