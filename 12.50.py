sentence = input("Введите предложение: ")
char = input("Какой символ искать? ")
for c in sentence:
    if c == char:
        print(c)