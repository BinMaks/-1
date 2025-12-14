n, a = map(int, input("Введите n (количество квартир) и a (начальный номер): ").split())
total = 0
for i in range(a, a + n):
    total += i
print(f"Сумма номеров квартир: {total}")
print(f"Сумма четная: {total % 2 == 0}")