def LetterCounter(s, l):
	answer = 0

	for i in range(len(s)):
		if s[i] == l:
			answer += 1

	return answer


string = input("String: ")
letter = input("Letter: ")
print()
print("Ocorrências:", LetterCounter(string, letter))
