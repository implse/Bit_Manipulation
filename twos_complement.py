# Two complement : return negative n
def twos_complement(input_value, num_bits):
    mask = 2**(num_bits - 1)
    print(mask)
    return -(input_value & mask) + (input_value & ~mask)

# Test
print(twos_complement(4, 8))
# for i in range(10):
#     print("Number {} in binary : {}".format(str(i), bin(i)))
#     print("Twos complement {} : {}".format(int(twos_complement(i, 8), 2), twos_complement(i, 8)))
