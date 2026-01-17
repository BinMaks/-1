word = input("Введите слово: ")
half = len(word) // 2
new_word = word[half:] + word[:half]
print(new_word)