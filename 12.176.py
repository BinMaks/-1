sentence = input("Введите предложение из 10 слов: ")
words = sentence.split()
if len(words) != 10:
    print("Ошибка: предложение должно содержать ровно 10 слов.")
else:
    word_array = words
    print("Массив слов:", word_array)