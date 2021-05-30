# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums, target):
        for i, v in enumerate(nums):
            for j, k in enumerate(nums):
                if v + k == target and i != j:
                    return [i, j]