
def reverse_string(string):
    if len(string) == 1:
        return string
    else:
        return string[len(string) - 1] + reverse_string(string[0:len(string) - 1])

punctuation = [".", "...", "!", "?", ",", " "]

def palindrome_checker(string):
    for i in punctuation:
        string = string.replace(i, "")

    if string == reverse_string(string):
        return True
    else:
        return False


frase = input("Frase: ")
print()
print(palindrome_checker(frase))







