word = input("Введите слово (оканчивается '_'): ")
letter = input("Буква для вставки: ")
pos = word.find("и")
if pos != -1:
    result = word[:pos+1] + letter + word[pos+1:]
    print(result)
else:
    print("Буквы 'и' нет в слове")