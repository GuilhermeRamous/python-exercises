def remove_vowels(s):
	new_string = ""

	for position in range(len(s)):
		if s[position] not in "AaEeIiOoUu":
			new_string += s[position]

	return new_string

string = input("String: ")
print()
print(remove_vowels(string))
