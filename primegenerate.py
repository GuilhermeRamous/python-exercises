def prime(n):
    for i in range(n):
        if i + 1 != 1 and i + 1 != n and n % (i + 1) == 0:
            return False
        elif i == n - 1:
            return True

t = int(input(""))
string = ""
p1 = 0
p2 = 2

for i in range(t):
    string  += input()
string = string.replace(" ", "")

for i in range(t):
    for x in range(int(string[p1]), int(string[p2]))
        if prime(x):
            print(x)

    p1 += 2
    p1 += 2
    print()




    
