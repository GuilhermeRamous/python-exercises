def reverse(s):
	new_string = ""

	for i in range(len(s)):
		new_string = s[i] + new_string

	return new_string

string = input("String: ")
print()
print(reverse(string))
