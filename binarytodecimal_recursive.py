def binary_to_decimal(n):
    n = str(n)

    if len(n) == 1:
        return int(n)
    else:
        return int(n[0]) * 2 ** (len(n) - 1) + binary_to_decimal(int(n[1:]))

print(binary_to_decimal(10))
print(binary_to_decimal(11))
print(binary_to_decimal(100))
