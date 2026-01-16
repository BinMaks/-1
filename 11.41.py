arr = [int(x) for x in input("Введите элементы массива: ").split()]
s = int(input("Номер элемента (s): ")) - 1
if 0 <= s < len(arr):
    if arr[s] > 0:
        print("Элемент положительный")
    else:
        print("Элемент не положительный")
else:
    print("Неверный индекс!")


arr = [int(x) for x in input("Введите элементы массива: ").split()]
k = int(input("Номер элемента (k): ")) - 1
if 0 <= k < len(arr):
    if arr[k] % 2 == 0:
        print("Элемент четный")
    else:
        print("Элемент нечетный")
else:
    print("Неверный индекс!")


arr = [int(x) for x in input("Введите элементы массива: ").split()]
k = int(input("Номер k-го элемента: ")) - 1
s = int(input("Номер s-го элемента: ")) - 1
if 0 <= k < len(arr) and 0 <= s < len(arr):
    if arr[k] > arr[s]:
        print(f"k-й элемент ({arr[k]}) больше s-го ({arr[s]})")
    elif arr[k] < arr[s]:
        print(f"s-й элемент ({arr[s]}) больше k-го ({arr[k]})")
    else:
        print("Элементы равны")
else:
    print("Неверный индекс!")


