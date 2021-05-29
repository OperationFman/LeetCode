class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits) - 1 # So the loop doesnt go out of bounds
        while digits[length] == 9: # Grabs the last value (Quicker than digits[-1])
            digits[length] = 0 # make it zero
            length -= 1 # Decrement length (It's a pointer to go in reverse)
        if(length < 0):
            digits = [1] + digits
        else:
            digits[length] += 1
        return digits

# Refactor!!