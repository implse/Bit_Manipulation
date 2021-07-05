# given two variables, swap their values without introducing a third variable

x = 42
y = 24

print(x, y)

# XOR algorithm

x = x ^ y
y = x ^ y
x = x ^ y

print(x, y)
