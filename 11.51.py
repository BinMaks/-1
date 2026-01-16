arr = [int(x) for x in input("Введите элементы массива: ").split()]
total_sum = sum(arr)
if total_sum >= 0:
    print("Сумма элементов неотрицательна")
else:
    print("Сумма элементов отрицательна")

arr = [int(x) for x in input("Введите элементы массива: ").split()]
k1 = int(input("k1: ")) - 1
k2 = int(input("k2: ")) - 1

if 0 <= k1 < k2 < len(arr):
    partial_sum = sum(arr[k1:k2+1])
    if partial_sum >= 0:
        print("Сумма элементов с k1 по k2 неотрицательна")
    else:
        print("Сумма элементов с k1 по k2 отрицательна")
else:
    print("Неверные индексы!")