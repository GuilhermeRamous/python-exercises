def rules(ch):
	if ch == "A":
		new_ch = "B"
	elif ch == "B":
		new_ch = "AB"
	else:
		new_ch = ch

	return new_ch

def process_string(string):
	new_str = ""

	for ch in string:
		new_str += rules(ch)

	return new_str

def Lsystem(num, axiom):
	start_string = axiom
	end_string = ""

	for i in range(num):
		end_string = process_string(start_string)
		start_string = end_string

	return end_string

string = input("String: ")
numIters = int(input("Número de iterações: "))
print()
print("Nova string:", Lsystem(numIters, string))
