class Solution:
    def reverse(self, x):
        negative = False # Holds info on wether or not the number will be nagitive or not
        
        if x < 0: # If it is negative, make it positive with abs() and flip negative to true
            x = abs(x)
            negative = True
        # This is because the next step[ doesn;t work on negative numbers, at the end we will turn it back to negative
             
        reverse = int(str(x)[::-1]) # Reverse the positive number by converting to string and back to int
        
        if negative == True:
            reverse = -abs(reverse) # make it negative again with -abs() if it was originally
        
        if reverse <= 2147483648 and reverse >= -2147483648: # Ensure it's between -2^31 and 2^31, because rules?
            return reverse # if it is, return it.
        else:
            return 0 # if it isn't it's 0