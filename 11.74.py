arr = [int(x) for x in input("Введите элементы массива: ").split()]
a, b = map(int, input("Введите a и b (a < b): ").split())
count_in_range = sum(1 for x in arr if a <= x <= b)
print(f"Элементов в диапазоне [{a}, {b}]: {count_in_range}")