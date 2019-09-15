# You are given an array of integers in which every element appears twice, except for one.
# Find the element that only appears one time.
# Your solution should have a linear runtime complexity (O(n)).

def singleNumber(nums):
    res = 0
    for num in nums:
        res = res ^ num
    return res
