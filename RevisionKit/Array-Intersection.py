# Given two integer arrays nums1 and nums2, 
# return an array of their intersection. 
# Each element in the result must appear as many times as 
# it shows in both arrays and you may return the result in any order.
from collections import Counter

class Solution:
    def intersect(nums1, nums2):
        """ nums1 = [1,2,2,1], nums2 = [2,2] """
        # Clue: Use counter and decrement as you iterate. Thus O(n)
        count = Counter(nums1) # O(n)
        result = []

        for i in nums2: # O(n)
            if count[i] > 0: # if the counts greater than zero it means there's an intersection
                result.append(i)
                count[i] -= 1

        return result



Solution.intersect([1,2,3,4,5,6], [1,1,1,1,1,1,1,1,1])