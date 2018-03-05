def low_or_upper(string):
	if 97 <= string <= 122:
		return 0
	else:
		return 1
def cesar_encrypter(texto, key):
	resultado = ""
	alfabeto_low = "abcdefghijklmnopqrstuvwxyz"
	alfabeto_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in range(len(texto)):
		if texto[i] in alfabeto_low or texto[i] in alfabeto_upper or texto[i] == " ":
			if texto[i] == " ":
				resultado += " "
			else:
				if low_or_upper(texto[i]) == 0 and chr(ord(texto[i]) + key) in alfabeto_low:
					resultado += chr(ord(texto[i]) + key)
				elif low_or_upper(texto[i]) == 1 and chr(ord(texto[i]) + key) in alfabeto_upper:
					resultado += chr(ord(texto[i]) + key)
				else:
					resultado += chr(ord(texto[i]) + key - 26)
		else:
			return "Cifra de cesar só criptografa letras não acentuadas. Execute o programa novamente."

	return resultado

string = input("Texto: ")
num = int(input("Chave (1 a 26): ")

print(cesar_encrypter(string, num))


				
					
