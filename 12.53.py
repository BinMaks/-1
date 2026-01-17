sentence = input("Введите предложение: ")
char1 = input("Первый символ: ")
char2 = input("Второй символ: ")
for char in sentence:
    if char == char1 or char == char2:
        print(char)