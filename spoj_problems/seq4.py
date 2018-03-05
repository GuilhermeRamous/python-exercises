nums = input().split()
x = int(nums[1])
seq1 = input().split()
seq2 = input().split()
ylist = [i for i in range(-x, x + 1)]
resultado = ""
somas = []

for s1 in range(len(seq1)):
    for s2 in ylist:
        if s1 + s2 in somas:
            pass
        else:
            somas.append(s1 + s2)

for v1 in range(len(seq1)):
    for v2 in ylist:
        if seq1[v1] not in seq2:
            break
        else:
            try:
                if seq1[v1] == seq2[v1 + v2] and v1 + v2 >= 0:
                    resultado += str(v1 + 1) + " "
            except:
                pass

print(resultado)
