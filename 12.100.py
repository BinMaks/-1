sentence = input("Введите предложение: ")
result = ''.join('ы' if i % 2 == 1 else char for i, char in enumerate(sentence))
print("Результат:", result)