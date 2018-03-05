def word_counter(w):
    return w.count(" ") + 1

word = input("Word: ")
print()
print("Número de palavras:", word_counter(word))
