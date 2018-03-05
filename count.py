def count(s, c):
	counter = 0
	
	for i in s:
		if i == c:
			counter += 1

	return counter

string = input("String: ")
char = input("char: ")
print()
print("Ocorrências:", count(string, char))
