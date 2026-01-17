sentence = input("Введите предложение: ")
char = input("Какой символ считать? ")
count = sentence.count(char)
print("Количество символов '{}': {}".format(char, count))