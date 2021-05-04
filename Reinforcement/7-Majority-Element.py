from collections import Counter # Counter is super sueful for counting commonalities on lists

class Solution:
    def majorityElement(self, nums):
        """ [3,2,3] """
        counts = Counter(nums).most_common() # counts looks like this: [(3, 2), (2, 1)]
        return counts[0][0] # counts[0] would be: (3, 2). [0] of that would be 3, and 3 is the most common
        