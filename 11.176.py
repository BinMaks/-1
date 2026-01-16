arr = list(map(int, input("Введите элементы: ").split()))
first = arr.pop(0)
arr.append(first)
print(arr)