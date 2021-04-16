from collections import Counter

class Solution:
    def majorityElement(self, nums):
        count = Counter(nums)
        x = count.most_common()
        return x[0][0]