import turtle

def rules(ch):
	if ch == "F":
		new_ch = "F-F++F-F"
	else:
		new_ch = ch

	return new_ch

def process_string(string):
	new_str = ""

	for ch in string:
		new_str += rules(ch) 

	return new_str

def systeml(num, axiom):
	start_string = axiom
	end_string = ""

	for i in range(num):
		end_string = process_string(start_string)
		start_string = end_string

	return end_string

def draw_system(t, end_string, a, d):
	for ch in end_string:
		if ch == "F":
			t.forward(d)
		elif ch == "B":
			t.backward(d)
		elif ch == "-":
			t.left(a)
		elif ch == "+":
			t.right(a)
		else:
			print("Error",ch, "is an unknown command")

def main():
	end_string = process_string("F")
	print(end_string)
	t = turtle.Turtle()
	wn = turtle.Screen()
	

	t.up()
	t.back(200)
	t.down()
	t.speed(9)
	draw_system(t, end_string, 60, 5)

main()
