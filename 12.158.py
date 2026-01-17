text = input("Введите текст: ")
digits = ""
for char in text:
    if char.isdigit():
        digits += char
    else:
        if digits:
            break
print("Число:", int(digits) if digits else "Цифр нет")