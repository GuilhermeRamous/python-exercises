def primo(n):
	counter = 0
	for i in range(n):
		if n % (i + 1) == 0:
			counter += 1
	if counter == 2:
		return True
	else:
		return False

def mmc(n1, n2):
	div = 2
	resultado = 1
	while n1 != 1 and n2 != 1: 
		if primo(div):
			if n1 % div == 0 or n2 % div == 0:
				resultado *= div
				if n1 % div == 0:
					n1 /= div 
				if n2 % div == 0:
					n2 /= div
		elif primo(div) == False or n1 % div != 0 and n2 % div != 0:
			while primo(div) == False:
				div += 1
	return resultado

print(mmc(15, 10))
				
