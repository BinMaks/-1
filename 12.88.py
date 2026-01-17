sentence = input("Введите предложение: ").lstrip()
first_word = sentence.split()[0]
count_o = first_word.count('о')
print("Количество букв 'о' в первом слове:", count_o)