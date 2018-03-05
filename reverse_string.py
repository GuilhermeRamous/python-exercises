def reverse_string(string):
    if len(string) == 1:
        return string
    else:
        return string[len(string) - 1] + reverse_string(string[0:len(string) - 1])

print(reverse_string("Ola Mundo"))

