# Given an array nums of size n, return the majority element.
from collections import Counter

def majorityElement(nums):
    # You know how to use Counter for this
    count = Counter(nums).most_common()
    print(count[0][0])

array = [1,2,2,3,3,3,3,3]
majorityElement(array)
        