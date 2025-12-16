n = int(input("Введите число (1-9): "))
if 1 <= n <= 9:
    print(f"Таблица умножения на {n}:")
    for i in range(1, 10):
        print(f"{i} x {n} = {i * n}")
else:
    print("Ошибка: число должно быть от 1 до 9!")