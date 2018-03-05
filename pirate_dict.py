dic = {"hotel":"fleabag inn", "sir":"matey", "student":"swabbie", "boy":"matey", "madam":"proud beauty", "professor":"foul blaggart", "restaurnat":"galley", "your":"yer", "excuse":"arr", "students":"swabbies", "are":"be", "lawyer":"foul blaggart", "the":"th`", "restroom":"head", "my":"me", "hello":"avast", "is":"be", "man":"matey"}

frase = input("Frase: ")
palavras = frase.split()
trad = ""

for i in palavras:
    trad += dic[i.lower()] + " "

print(trad.capitalize())

    

