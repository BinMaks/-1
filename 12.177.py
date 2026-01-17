sentence = input("Введите предложение: ")
words = sentence.split()
reversed_sentence = ' '.join(reversed(words))
print("Обратный порядок слов:", reversed_sentence)