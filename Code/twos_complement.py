# Two complement : return negative n
def twos_complement(input_value, num_bits):
    mask = 2**(num_bits - 1)
    print(mask)
    return -(input_value & mask) + (input_value & ~mask)

# Test
print(twos_complement(4, 8))
