arr = list(map(int, input("Введите элементы массива: ").split()))
if len(arr) != len(set(arr)):
    print("В массиве есть одинаковые элементы")
else:
    print("Все элементы уникальны")