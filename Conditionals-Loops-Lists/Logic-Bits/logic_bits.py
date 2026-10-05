a = bool(int(input("Enter 1 for True or 0 for False: ")))
b = bool(int(input("Enter 1 for True or 0 for False: ")))

# Logical operators
print("a AND b:", a and b)
print("a OR b:", a or b)
print("NOT a:", not a)

# Bitwise operators
x = 5
y = 3
print("5 & 3:", bin(x&y))
print("5 | 3:", bin(x | y))
print("5 ^ 3:", bin(x ^ y))
print("~5:", bin(~x))
print("5 << 1:", bin(x << 1))
print("5 >> 1:", bin(x >> 1))