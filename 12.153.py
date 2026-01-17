number = input("Введите целое число: ")
digits = [int(char) for char in number if char.isdigit()]
print("Сумма цифр:", sum(digits))