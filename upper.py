def upper(string):
	upper_string = ""
	counter = 0
	for i in range(len(string)):
		upper_string += chr(ord(string[i]) - 32)

		if ord(string[i]) < 97 or ord(string[i]) > 122:
			counter += 1  
	
	if counter > 0:
		return "Os caracteres de entrada devem ser somente letras minúsculas. Execute o programa novamente."
	else:
		return upper_string

text = input("String: ")
print(upper(text)) 
