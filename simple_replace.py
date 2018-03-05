def simple_replace(s, l):
	t = 0	
	new_string = ""

	if l not in s:
		return s
	else:
		for i in s:
			if i == l and t == 0:
				t += 1
			elif t == 1 or i != l:
				new_string += i

		return new_string

string = input("String: ")
letter = input("Letter: ")
print()
print("Nova string:", simple_replace(string, letter))
