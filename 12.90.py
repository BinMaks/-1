sentence = input("Введите предложение: ")
for i in range(len(sentence) - 1):
    if sentence[i] == sentence[i + 1]:
        print("Порядковые номера первой пары одинаковых символов:", i + 1, i + 2)
        break
else:
    print("Пары одинаковых соседних символов нет")