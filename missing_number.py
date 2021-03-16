# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


# Bit manipulation XOR
def missing_number_xor(nums):
    missing = len(nums)
    for i in range(len(nums)):
        missing ^= i ^ nums[i]
    return missing

# Test
nums = [0, 1, 2, 4]

print(missing_number_xor(nums))
