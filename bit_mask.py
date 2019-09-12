def set_bit(x, position):
    mask = 1 << position
    return x | mask

x = 0b00000110
position = 0b00000101
# mask = 00100000


print(bin(set_bit(x, position)))
