# Given a number N, find its binary representation using Bitwise


def decimalToBinary(n):
    binary_repr = 0
    power = 1

    while n > 0:
        last_bit = n & 1 # check if last bit is 1 or 0
        binary_repr += power * last_bit
        power *= 10
        n = n >> 1 # right shift by 1

    return binary_repr

print(decimalToBinary(1))
print(decimalToBinary(2))
print(decimalToBinary(4))
print(decimalToBinary(8))
print(decimalToBinary(16))
print(decimalToBinary(32))
print(decimalToBinary(64))
print(decimalToBinary(128))
