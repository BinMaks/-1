text = input("Введите текст: ")
cleaned = text.lstrip()  # убираем начальные пробелы
digits = [(i, int(char)) for i, char in enumerate(cleaned) if char.isdigit()]
if digits:
    max_digit = max(digits, key=lambda x: x[1])
    print("Порядковый номер максимальной цифры:", max_digit[0] + 1)
else:
    print("Цифр нет")