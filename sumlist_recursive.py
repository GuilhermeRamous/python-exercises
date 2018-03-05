def sumlist(lis):
    if len(lis) == 1:
        return lis[0]
    else:
        return lis[0] + sumlist(lis[1:])

print(sumlist([2]))
print(sumlist([1, 2, 3]))

