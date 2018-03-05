def primo(n):
	for i in range(n):
		if i + 1 != n and i + 1 != 1 and n % (i + 1) == 0:
			return False
		elif i == n - 1:
			return True
		
print(primo(3))
print(primo (4))
print(primo(5))
print(primo(7))

