def replace(s, l):
	new_string = ""
	
	if l not in s:
		return s
	else:
		for i in s:
			if i != l:
				new_string += i

	return new_string

string = input("String: ")
letter = input("Letter: ")
print()
print("Nova string:", replace(string, letter))
