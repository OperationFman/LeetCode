# Given a signed 32-bit integer x (aka between 2147483648 and -2147483648), return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0

class Solution:
    def reverse(self, x):
        pass
        # Clue: Convert to a string, reverse, convert back and return. If it's negative, store that ahead of time then turn 
        # it back to negative at the end. Then simply check it's in range