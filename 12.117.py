word = input("Введите слово: ")
result = word[:2] + word[3:]
print(result)

word = input("Введите слово: ")
k = int(input("Номер буквы для удаления (k): ")) - 1
result = word[:k] + word[k+1:]
print(result)