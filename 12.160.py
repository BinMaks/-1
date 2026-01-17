import re
text = input("Введите текст: ")
numbers = [int(num) for num in re.findall(r'\d+', text)]
if numbers:
    print("Максимальное число:", max(numbers))
else:
    print("Чисел нет")