# Bit Manipulation

## Bitwise Operator

- & (AND)

- | (OR)

- ^ (XOR)

- ~ (NOT)

- << (LEFT SHIFT)

- \>> (RIGHT SHIFT)


### AND

Only True if both input are True.

0 & 0 = 0

0 & 1 = 0

1 & 0 = 0

1 & 1 = 1

|Operation|
|:--------|
|10010110 |  
|&        |
|00110010 |
=
|00010010 |


### OR

True if any input bit is True.

0 | 0 = 0

1 | 0 = 1

0 | 1 = 1

1 | 1 = 1

|Operation|
|:--------|
|10010110 |  
|\|       |
|00110010 |
=
|10110110 |

### XOR

True if one and only one input bit is True.

O ^ 0 = 0

1 ^ 0 = 1

0 ^ 1 = 1

1 ^ 1 = 0

|Operation|
|:--------|
|10010110 |  
|&        |
|00110010 |
=
|10100100 |

### NOT

One's complement operator.

Flips the input bit.

~ 0 = 1
~ 1 = 0


### LEFT BIT SHIFT

Shift the binary digits by n, pad 0's on the right.

Each shift is a multiply by 2(unless there is overflow).

|Operation|
|:--------|
|00010110 |  
|<<       |
|00000010 | left shift by 2 == multiply by 2
=
|01011000 |


```
0b00000001 << 2 == 0b00000100 (1 << 2 = 4)

0b00000101 << 3 == 0b00101000 (5 << 3 = 40)
```


### RIGHT BIT SHIFT

Shift the binary digits by n, pad 0's on the left.

Each shift is a divide by 2 with round towards negative infinity.


|Operation|
|:--------|
|00010110 |  
|>>       |
|00000010 | right shift by 2 == divide by 2
=
|00000101 |


```
0b00010100 >> 3 == 0b00000010 (20 >> 3 = 2)

0b00000010 >> 2 == 0b00000000 ( 2 >> 2 = 0)
```
