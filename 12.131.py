text = input("Введите предложение (оканчивается '_'): ")
letter = input("Буква для вставки: ")
pos = text.rfind("и")
if pos != -1:
    result = text[:pos] + letter + text[pos:]
    print(result)
else:
    print("Буквы 'и' нет в предложении")