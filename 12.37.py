word = input("Слово: ")
new_word = word[-3:] + word[3:-3] + word[:3]
print(new_word)