num1 = int(input())
seq1 = input().split()
num2 = int(input())
seq2 = input().split()
resultado = ""

if seq1 < seq2:
    menor = seq1
else:
    menor = seq2

for i in range(len(menor)):
    if seq1[i] == seq2[i]:
        resultado += str(i + 1) + " "

print(resultado)

