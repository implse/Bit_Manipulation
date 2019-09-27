# Add Two Numbers Without The "+" Sign

def get_sum(a, b):
    while b != 0:
        # Find carry with &
        carry = a & b
        # XOR a and b, keep the sum we are working on
        a = a ^ b
        # Left shift the carry
        b = carry << 1
    return a


# Test
a = 42
b = 4
print(get_sum(a, b))
