arr = [1, 2, 3, 4, 5]
index = int(input("Введите индекс: "))
if 0 <= index < len(arr):
    print(f"Элемент по индексу {index}: {arr[index]}")
else:
    print("Индекс вне диапазона!")