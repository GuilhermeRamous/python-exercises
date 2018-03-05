def reverse(string):
    new_string = ""

    for i in string:
        new_string = i + new_string
    
    return new_string

t = int(input())
string = ""
p = 0

for i in range(t):
    value = input() 
    string += value

for i in range(t):
    pal = int(string[p]) - 1
    n = 1

    while pal < int(string[p]):
        if pal + n != reverse(str(pal + n)):
            n += 1
        else:
            pal += n
            print(pal)
    p += 1


