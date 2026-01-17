text = input("Введите текст: ")
first_sentence = text.split('.')[0]
count_i = first_sentence.count('и')
print("Количество букв 'и':", count_i)