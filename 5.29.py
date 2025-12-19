numbers = range(1, 751)
average = sum(numbers) / len(numbers)
print(f"Среднее арифметическое: {average:.2f}")


b = int(input("Введите b (b > 150): "))
numbers = range(150, b + 1)
average = sum(numbers) / len(numbers)
print(f"Среднее арифметическое: {average:.2f}")



a = int(input("Введите a (a < 200): "))
numbers = range(a, 201)
average = sum(numbers) / len(numbers)
print(f"Среднее арифметическое: {average:.2f}")


a = int(input("Введите a: "))
b = int(input("Введите b (b > a): "))
numbers = range(a, b + 1)
average = sum(numbers) / len(numbers)
print(f"Среднее арифметическое: {average:.2f}")