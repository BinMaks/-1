arr = list(map(int, input("Введите элементы: ").split()))
last = arr.pop()
arr.insert(0, last)
print(arr)