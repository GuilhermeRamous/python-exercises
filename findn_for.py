def find_n(s, l, n):
	t = 0

	for i in range(len(s)):
		if s[i] == l and t + 1 == n:
			return i
		elif s[i] == l:
			t += 1
		elif i == len(s) - 1:
			return - 1

string = input("String: ")
letter = input("Letter: ")
number = input("Number: ")
print()
print(find_n(string, letter, number))
			
