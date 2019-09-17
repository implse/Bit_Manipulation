# Bit Manipulation

Bitwise operations are operations that directly manipulate bits.

## Bitwise Operator

- & (AND)

- | (OR)

- ^ (XOR)

- ~ (NOT)

- << (LEFT SHIFT)

- \>> (RIGHT SHIFT)


### AND

The bitwise AND (&) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if the corresponding bits of both numbers are 1.

Only True if both input are True.

```
0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1
```

```
128| 64| 32| 16| 8 | 4 | 2 | 1 |
--------------------------------
 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 |
--------------------------------
 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | & (AND)
--------------------------------
 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
 ```

### OR

The bitwise OR (|) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of either number are 1.

True if any input bit is True.

```
0 | 0 = 0
1 | 0 = 1
0 | 1 = 1
1 | 1 = 1
```

```
128| 64| 32| 16| 8 | 4 | 2 | 1 |
--------------------------------
 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 |
--------------------------------
 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | | (OR)
--------------------------------
 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 |
```

### XOR

The XOR (^) or exclusive or operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of the two numbers are 1, but not both.

True if one and only one input bit is True.

```
O ^ 0 = 0
1 ^ 0 = 1
0 ^ 1 = 1
1 ^ 1 = 0
```

```
128| 64| 32| 16| 8 | 4 | 2 | 1 |
--------------------------------
 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 |
--------------------------------
 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | ^ (XOR)
--------------------------------
 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
```

### NOT

One's complement operator.

Flips the input bit.

```
~ 0 = 1
~ 1 = 0
```
Mathematically, this is equivalent to adding one to the number and then making it negative.

### LEFT BIT SHIFT

Shift the binary digits by n, pad 0's on the right.

Each shift is a multiply by 2(unless there is overflow).

```
128| 64| 32| 16| 8 | 4 | 2 | 1 |
--------------------------------
 O | 0 | 0 | 1 | 0 | 1 | 1 | 0 |
--------------------------------
 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | << (left shift by 2 == multiply by 2)
--------------------------------
 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 |
```

```
0b00000001 << 2 == 0b00000100 (1 << 2 = 4)

0b00000101 << 3 == 0b00101000 (5 << 3 = 40)
```


### RIGHT BIT SHIFT

Shift the binary digits by n, pad 0's on the left.

Each shift is a divide by 2 with round towards negative infinity.

```
128| 64| 32| 16| 8 | 4 | 2 | 1 |
--------------------------------
 O | 0 | 0 | 1 | 0 | 1 | 1 | 0 |
--------------------------------
 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | >> (right shift by 2 == divide by 2)
--------------------------------
 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
```

```
0b00010100 >> 3 == 0b00000010 (20 >> 3 = 2)

0b00000010 >> 2 == 0b00000000 (2 >> 2 = 0)
```
You can only do bitwise operations on an integer.

### BIT MASK

A bit mask is just a variable that aids you with bitwise operations. A bit mask can help you turn specific bits on, turn others off, or just collect data from an integer about which bits are on or off.

```
num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
  print "Bit was on"
```


1 - Create a variable num containing the number 12, or 0b1100.

2 - Create a mask with the third bit on.

3 - Use a bitwise-and operation to see if the third bit from the right of num is on.

4 - If desired is greater than zero, then the third bit of num must have been one.



Using the bitwise OR operator will turn a corresponding bit on if it is off and leave it on if it is already on.

```
num = 0b101000 # 40
mask = 0b100 # Turn third bit On
num = num | mask
num = 0b101100 # 44
```

Using the XOR operator is very useful for flipping bits. Using XOR on a bit with the number one will return a result where that bit is flipped.


```
num = 0b101000 # 40
mask = 0b111111 # Flip bits
num = num ^ mask
num = 0b10111 # 23
```

Using the left shift (<<) and right shift (>>) operators to slide masks into place.

```
num = 0b101 # 5
# Tenth bit mask
mask = (0b1 << 9)  # 0b1000000000 (512)
num = num ^ mask # 0b1000000101 (517)
```

### Two's Complement for Negative Integers

Negative numbers are written with a leading one instead of a leading zero.

So if you are using only 8 bits for your twos-complement numbers, then you treat patterns from "00000000" to "01111111" as the whole numbers from 0 to 127, and reserve "1xxxxxxx" for writing negative numbers.

Two's complement subtracts off (1<<bits) if the highest bit is 1. Taking 8 bits for example, this gives a range of 127 to -128.

find two's complement :
  - Flip all the bit. (One's complement)
  - Add 1

```
-128| 64| 32| 16| 8 | 4 | 2 | 1 | (-128) Sign bit
---------------------------------
  O | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  = 3
---------------------------------
  1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 |  = -3 in two's complement
---------------------------------
  0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  Sum (3 - 3) = 0
```
