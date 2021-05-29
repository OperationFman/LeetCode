# Given a not-empty array, one element isn't repeated. Find it

from collections import Counter
class Solution:
    def singleNumber(self, nums):
        # Do the classic: enumerate, pop, check, insert if not
        count = Counter(nums)
        for i in count:
            if count[i] == 1:
                return i


print(Solution().singleNumber([1,1,2,2,3,3,4,5,5,6,6]))
