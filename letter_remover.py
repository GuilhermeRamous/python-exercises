def letter_remover(s, l):
	new_string = ""

	for i in s:
		if i != l:
			new_string += i

	return new_string

string = input("String: ")
letter = input("Letter: ")
print()
print(letter_remover(string, letter))
			
		
