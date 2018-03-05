def multi_string(string, n):
	resultado = ""
	for i in range(n):
		resultado += string
	return resultado

string = input("Digite sua string para a multiplicação: ")
n = int(input("Digite quantas vezes quer que sua string seja multiplicada: "))

print(multi_string(string, n))  
