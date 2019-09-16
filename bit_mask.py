def set_bit(x, position):
    mask = 0b1 << position
    return x | mask

def clear_bit(x, position):
    mask = 0b1 << position
    return x & ~mask

def flip_bit(x, position):
    mask = 0b1 << position
    return x ^ mask

def is_bit_set(x, position):
    shifted = x >> position
    return shifted & 0b1
