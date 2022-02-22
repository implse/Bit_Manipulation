# Define a function, check_bit4, with one argument, input, an integer.
# It should check to see if the fourth bit from the right is on.


def check_bit4(input):
    mask = 0b1000
    desired = input & mask
    print(desired)
    if desired > 0:
        return "on"
    else:
        return "off"

print(check_bit4(0b1)) # "off"
print(check_bit4(0b11011)) # "on"
print(check_bit4(0b1010)) # "on"
