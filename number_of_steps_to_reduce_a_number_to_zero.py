# Given a binary string s, return the number of steps to reduce it to zero.

# number = "1110" return 6

def reduce_to_zero(binary):
    mask = 1
    binary = int(binary, 2)
    step = 0
    while binary != 0:
        step += 1
        if binary & mask == 1:
            binary = binary  - 1
        else:
            binary = binary >> 1
    return step


print(reduce_to_zero("1110")) # 6
print(reduce_to_zero("10")) # 2
print(reduce_to_zero("1")) # 1
print(reduce_to_zero("1111")) # 7
