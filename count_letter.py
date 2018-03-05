def letter_count(text, letter):
"""Conta quantas vezes uma substring aparece em uma string principal"""
	count = 0
	for i in text:
		if i == letter:
			count += 1
	return count

string = input("String: ")
substring = input("Substring: ")
print("")
print("Casos de ocorrência:", letter_count(string, substring))
