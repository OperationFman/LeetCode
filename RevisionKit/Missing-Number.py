# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums):
        # They're all unique. Try an do it in O(n), originally you had it O(n^2)
        count = 0
        sorty = sorted(nums)
        for i in sorty:
            if i != count:
                return count
            else:
                count += 1
        return count