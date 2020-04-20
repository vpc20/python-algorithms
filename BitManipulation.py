def set_bit(n, pos):
    return bin(n | (1 << pos))


def toggle_bit(n, pos):
    return bin(n ^ (1 << pos))


def check_bit(n, pos):
    shift = 1 << pos
    return shift == n & shift


def clear_bit(n, pos):
    return bin(n & (4294967295 - (1 << pos)))


x = 0b10101010
y = 0b00000010
z = 0b11111110

# print(bin(int(0b10101010) | int(y)))
# print(bin(int(0b10101010) & int(z)))
# print(bin(int(0b10101010) & int(y)))
# print(0b11111111111111111111111111111111)

print(set_bit(x, 0))
print(clear_bit(x, 1))

print(toggle_bit(x, 0))
print(toggle_bit(x, 1))

print(check_bit(x, 0))
print(check_bit(x, 1))
print(check_bit(x, 2))
print(check_bit(x, 3))

print(0b1111111111111111111111111111111111111111111111111111111111111111)
