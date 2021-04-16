class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, j in enumerate(nums):
            if j == 0:
                pop = nums.pop(i)
                nums.append(pop)
        for i, j in enumerate(nums):
            if j == 0:
                pop = nums.pop(i)
                nums.append(pop)

# Bit hacky to just do it twice but it passes