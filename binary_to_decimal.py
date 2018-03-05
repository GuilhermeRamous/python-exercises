binary = input("Binary: ")
decimal = 0

for i in range(len(binary)):
    decimal +=  int(binary[-1 *(i + 1)]) * 2 ** i

print(decimal)
