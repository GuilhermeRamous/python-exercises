num1 = int(input())
seq1 = input().split()
num2 = int(input())
seq2 = input().split()
result = ""

for i in range(len(seq1)):
    if seq1[i] in seq2:
        result += seq1[i] + " "

print(result)
