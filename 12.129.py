word = input("Введите слово (оканчивается '_'): ")
letter = input("Буква для вставки: ")
pos = int(input("Номер буквы (с 1): ")) - 1
result = word[:pos+1] + letter + word[pos+1:]
print(result)