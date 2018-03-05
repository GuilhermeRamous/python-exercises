num1 = int(input())
seq1 = input().split()
num2 = int(input())
seq2 = input().split()
saida = ""

for i in range(len(seq1)):
    if seq1[i] not  in seq2:
        saida += seq1[i] + " "

print(saida)



    
