word = input("Слово: ")
k = int(input("k: "))
new_word = word[k:] + word[:k]
print(new_word)