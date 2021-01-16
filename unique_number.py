# Given a list of numbers where every numbers occurs twice, find that unique number


# Bitwise XOR : Time Complexity : O(n)
def singleNumber(nums):
    res = 0
    for num in nums:
        res = res ^ num
    return res
