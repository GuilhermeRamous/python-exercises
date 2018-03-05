def gfc(n1, n2):
    if n1 == n2:
        return n1
    else:
        while n1 != n2:
            if n1 > n2:
                n1 -= n2
            else:
                n2 -= n1
        
        return n1


n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
print()
print(gfc(n1, n2))
