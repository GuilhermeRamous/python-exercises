def remove_consonants(s):
	new_string = ""

	for position in range(len(s)):
		if s[position] in "AaEeIiOoUu" or s[position] == " ":
			new_string += s[position]

	return new_string

string = input("String: ")
print(remove_consonants(string))
