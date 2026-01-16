arr = list(map(float, input("Введите рост 25 учеников: ").split()))
idx = int(input("Введите номер выбывшего ученика: ")) - 1
del arr[idx]
arr.append(0)
print(arr)


arr = list(map(float, input("Введите рост 25 учеников: ").split()))
height = float(input("Введите рост выбывшего ученика: "))
idx = arr.index(height)
del arr[idx]
arr.append(0)
print(arr)