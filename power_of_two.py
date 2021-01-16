# Check if a number is a power of two using bitwise operator

# https://stackoverflow.com/questions/57025836/how-to-check-if-a-given-number-is-a-power-of-two

# Every power of 2 has exactly 1 bit set to 1 (the bit in that number's log base-2 index).
# So when subtracting 1 from it, that bit flips to 0 and all preceding bits flip to 1.
# That makes these 2 numbers the inverse of each other so when AND-ing them, we will get 0 as the result.

# Biwise sloution
def power_of_two(n):
    return (n & (n-1) == 0) and n != 0

print(power_of_two(9))
print(power_of_two(16))
print(power_of_two(32))

# Using math
import math

def power_of_two(n):
    return math.log(n, 2).is_integer()

print(power_of_two(9))
print(power_of_two(16))
print(power_of_two(32))
