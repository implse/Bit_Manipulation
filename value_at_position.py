# define a function to find out the value of the bit of a given position

def getBit(number, bit_position):
    return (number >> bit_position) & 1

# 10 -> 1010
# right shift by 2: 10 >> 2 = 10
# 10 & 1 = 0
print(bin(10))
print(getBit(10, 2))


# 5 -> 101
# right shift by 2: 5 >> 2 = 1
# 1 & 1 = 1
print(bin(5))
print(bin(5 >> 2))
print(getBit(5, 2))
