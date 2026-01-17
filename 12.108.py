word = input("Введите слово: ")
word_list = list(word)
word_list[1]= word_list[4], word_list[1]
result = ''.join(word_list)
print(result)