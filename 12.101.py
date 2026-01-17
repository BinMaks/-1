sentence = input("Введите предложение: ")
result = ''.join('а' if (i + 1) % 3 == 0 else char for i, char in enumerate(sentence))
print("Результат:", result)