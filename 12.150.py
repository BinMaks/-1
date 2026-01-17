text = input("Введите текст: ")
digits = [int(char) for char in text if char.isdigit()]
if digits:
    print("Сумма цифр:", sum(digits))
    print("Максимальная цифра:", max(digits))
else:
    print("Цифр нет")