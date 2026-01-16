arr = list(map(int, input("Элементы списка: ").split()))
arr = [100] + arr
print(arr)

arr = list(map(int, input("Элементы списка: ").split()))
num = int(input("Число для вставки: "))
arr = [num] + arr
print(arr)

arr = list(map(int, input("Элементы списка: ").split()))
num = int(input("Число для вставки: "))
idx = int(input("Индекс: "))
arr = arr[:idx] + [num] + arr[idx:]
print(arr)