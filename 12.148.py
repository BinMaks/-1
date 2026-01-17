text = input("Введите текст: ")
digits = [char for char in text if char.isdigit()]
print("".join(digits))