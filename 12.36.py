word = input("12-буквенное слово: ")
third = len(word) // 3
new_word = word[third*2:] + word[:third] + word[third:third*2]
print(new_word)


word = input("12-буквенное слово: ")
third = len(word) // 3
new_word = word[third:third*2] + word[third*2:] + word[:third]
print(new_word)