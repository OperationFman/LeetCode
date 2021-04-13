import itertools

class Solution:
    def permute(self, nums):
        x = list(itertools.permutations(nums))
        result = []
        for i in x:
            result.append(list(i))
        return result