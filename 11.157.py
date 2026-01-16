arr = list(map(float, input("Введите стоимость 20 товаров: ").split()))
n = int(input("Введите n: ")) - 1
del arr[n]
arr.append(0)
print(arr)