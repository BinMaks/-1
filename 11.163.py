
arr = list(map(int, input("Введите элементы: ").split()))
arr = [x for x in arr if x >= 0]
print(arr)


arr = list(map(int, input("Введите элементы: ").split()))
n = int(input("Введите n: "))
arr = [x for x in arr if x <= n]
print(arr)

arr = list(map(int, input("Введите элементы: ").split()))
n1, n2 = map(int, input("Введите n1 и n2: ").split())
arr = arr[:n1-1] + arr[n2:]
print(arr)