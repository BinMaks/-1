import re
text = input("Введите текст: ")
numbers = re.findall(r'\d+', text)
sum_numbers = sum(int(num) for num in numbers)
print("Сумма всех чисел:", sum_numbers)