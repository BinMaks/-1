arr = list(map(int, input("Введите элементы: ").split()))
arr = [arr[i] for i in range(len(arr)) if not (i % 2 == 1 and arr[i] % 2 == 0)]
print(arr)


arr = list(map(int, input("Введите элементы: ").split()))
arr = [x for x in arr if x % 3 != 0 and x % 5 != 0]
print(arr)