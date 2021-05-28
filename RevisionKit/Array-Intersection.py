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
        matches = set(nums1) & set(nums2)
        result = []
        
        for i in matches:
            if count1[i] > 0:
                count1[i] = count1[i] - 1
                result.append(i)

        print(result)



Solution.intersect([1,2,2,2,2,2,2,2,2,3,4], [1,2,2,3,4])