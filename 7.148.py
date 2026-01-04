n = int(input("Количество чисел: "))
numbers = [int(input(f"Число {i+1}: ")) for i in range(n)]

if max(numbers) - min(numbers) <= 25:
    print("Да, условие выполняется")
else:
    print("Нет, условие не выполняется")