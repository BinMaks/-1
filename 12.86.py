sequence = input("Введите последовательность символов: ")
if len(set(sequence)) == 1: 
    print("Все символы последовательности одинаковые, количество:", len(sequence))
else:
    count = 1
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[0]:
            count += 1
        else:
            break
    print("Количество одинаковых символов в начале:", count)