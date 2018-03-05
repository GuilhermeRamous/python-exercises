n1 = float(input("1° número: "))
n2 = float(input("2° número: "))
n3 = float(input("3° número: "))
n4 = float(input("4° número: "))
n5 = float(input("5° número: "))
conta1 = 1
conta2 = 1
conta3 = 1
conta4 = 1
conta5 = 1


if n1 == n2:
	conta1 += 1
if n1 == n3:
	conta1 += 1
if n1 == n4:
	conta1 += 1
if n1 == n5:
	conta1 += 1

if n2 == n1:
	conta2 += 1
if n2 == n3:
	conta2 += 1
if n2 == n4:
	conta2 += 1
if n2 == n5:
	conta2 += 1

if n3 == n1:
	conta3 += 1
if n3 == n2:
	conta3 += 1
if n3 == n4:
	conta3 += 1
if n3 == n5:
	conta3 += 1

if n4 == n1:
	conta4 += 1
if n4 == n2:
	conta4 += 1
if n4 == n3:
	conta4 += 1
if n4 == n5:
	conta4 += 1

if n5 == n1:
	conta5 += 1
if n5 == n2:
	conta5 += 1
if n5 == n3:
	conta5 += 1
if n5 == n4:
	conta5 += 1

if conta1 == conta2 and conta2 == conta3 and conta3 == conta4 and conta4 == conta5:
	print("O conjunto apresentado é unitário.")
else: 
	if max(conta1, conta2, conta3, conta4, conta5) == conta1:
		print("Moda:", n1)
	elif max(conta1, conta2, conta3, conta4, conta5) == conta2:
		print("Moda:", n2)
	elif max(conta1, conta2, conta3, conta4, conta5) == conta3:
		print("Moda:", n3)
	elif max(conta1, conta2, conta3, conta4, conta5) == conta4:
		print("Moda:", conta4)
	else:
		print("Moda:", conta5)




 

	
