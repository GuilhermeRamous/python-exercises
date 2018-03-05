print("País A:")
o1 = int(input("Ouro: "))
p1 = int(input("Prata: "))
b1 = int(input("Bronze: "))
print("")

print("País B:")
o2 = int(input("Ouro: "))
p2 = int(input("Prata: "))
b2 = int(input("Bronze: "))

if o1 > o2:
	print("A")
elif o2 > o1:
	print("B")
elif p1 > p2:
	print("A")
elif p2 > p1:
	print("B")
elif b1 > b2:
	print("A")
elif b2 > b1:
	print("B")
else:
	print("Empate total")

