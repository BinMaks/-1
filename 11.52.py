arr = [int(x) for x in input("Введите элементы массива: ").split()]
if 0 in arr:
    print("В массиве есть нули")
else:
    print("В массиве нет нулей")

arr = [int(x) for x in input("Введите элементы массива: ").split()]
if any(x < 0 for x in arr):
    print("В массиве есть отрицательные элементы")
else:
    print("Отрицательных элементов нет")



arr = [int(x) for x in input("Введите элементы массива: ").split()]
if all(x > 0 for x in arr):
    print("Все элементы положительные")
else:
    print("Есть неположительные элементы")


arr = [int(x) for x in input("Введите элементы массива: ").split()]
if any(x % 3 == 0 for x in arr):
    print("Есть элементы, кратные 3")
else:
    print("Нет элементов, кратных 3")


arr = [int(x) for x in input("Введите элементы массива: ").split()]
if all(x % 2 == 0 for x in arr):
    print("Все элементы четные")
else:
    print("Есть нечетные элементы")

arr = [int(x) for x in input("Введите элементы массива: ").split()]
if len(arr) != len(set(arr)):
    print("Есть повторяющиеся элементы")
else:
    print("Все элементы уникальны")


arr = [int(x) for x in input("Введите элементы массива: ").split()]
if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
    print("Массив упорядочен по возрастанию")
else:
    print("Массив не упорядочен")

