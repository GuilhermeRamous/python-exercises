def rot13_coder(s):
	coded = ""

	for i in s:
		if ord(i) + 13 > 122 or ord(i) + 13 > 90:
			subs = 26
		else:
			subs = 0

		if i != " ":
			coded += chr(ord(i) + 13 - subs)
		else:
			coded += " "	

	return coded

string = input("String: ")
print()
print("Coded message:", rot13_coder(string))
