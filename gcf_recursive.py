def gcf(n1, n2):
    if n1 == n2:
        return n1
    else:
        n1 = max(n1, n2)
        n2 = min(n1, n2)
        n1 -= n2
        
        return gcf(n1, n2)

print(gcf(10, 5))
print(gcf(10, 10))
print(gcf(100, 10))

        

