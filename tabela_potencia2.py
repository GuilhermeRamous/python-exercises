quantas = int(input("Digite quantas potências a tabela deve ter: "))

print("n\t2**n")
print("----\t----")

for i in range(quantas):
	print(i, "\t", 2 ** i)
