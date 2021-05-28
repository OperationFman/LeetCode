# Given two integer arrays nums1 and nums2, 
# return an array of their intersection. 
# Each element in the result must appear as many times as 
# it shows in both arrays and you may return the result in any order.
from collections import Counter

class Solution:
    def intersect(nums1, nums2):
        """ nums1 = [1,2,2,1], nums2 = [2,2] """
        # Clue: Use counter and decrement as you iterate. Thus O(n)
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        for i in count1:
            if count1[i] > 0 and i in count2:
                pass


Solution.intersect([1,2,2,3], [1,3,4])