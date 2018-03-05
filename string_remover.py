"""Remove todas as ocorrências de uma determinada substring da string principal"""

def string_remover(string, removed_part):
	return string.replace(removed_part, "")

texto = input("Texto: ")
parte_removida = input("Parte que será removida: ")
print(string_remover(texto, parte_removida))
