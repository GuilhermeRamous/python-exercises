a = 80000
taxa_a = 3 / 100
b = 200000
taxa_b = 1.5 / 100
anos = 0

while a < b:
	a += a * taxa_a 
	b += b * taxa_b
	anos += 1

print(anos)

