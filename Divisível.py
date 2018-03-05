def divisivel(x, y):
   return x % y == 0

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

if divisivel(n1, n2) == True:
    print(n1, "é divisível por", n2)

else:
    print(n1, "não é divisível por", n2)
