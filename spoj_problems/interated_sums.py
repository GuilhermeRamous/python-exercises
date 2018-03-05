nums = input().split()
x = int(nums[0])
y = int(nums[1])
lista = [i for i in range(x, y + 1)]
resultado = 0

for v in lista:
    resultado += v ** 2

print(resultado)
