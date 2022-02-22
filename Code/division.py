# Implement division without / or * operators.
def divide(x, y):
    if y == 0:
        return "Division by zero"
    quotient = 0
    # 32 bit integer assumption
    power = 32
    y_power = y << power
    # Initial remainder
    remainder = x
    while remainder >= y:
        while y_power > remainder:
            y_power >>= 1
            power -= 1
        quotient += 1 << power
        remainder -= y_power
    return quotient

# Test
#print(divide(1024, 32))
print(divide(42, 7))
