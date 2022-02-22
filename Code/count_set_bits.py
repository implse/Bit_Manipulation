# Write a program to count the number of bits that are set to 1 in a positive integer.

def count_bits(n):
    num_bits = 0
    while n:
        num_bits += n & 1
        # Right Shift by 1 == divide by 2
        n = n >> 1
    return num_bits

# 74 :  0b1001010
print(count_bits(74))
# 36 : 0b100100
print(count_bits(36))
# 11 : 0b1011
print(count_bits(11))
