quantas = int(input("Digite quantas potências a tabela deve mostrar: "))

print("n\t2**n")
print("----\t----")

for i in range(quantas):
	print(i, "\t", 3 ** i)
