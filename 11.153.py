
arr = list(map(int, input("Введите 20 элементов массива: ").split()))
first_three = arr[:3]
last_three = arr[-3:]
middle = arr[3:-3]
arr = last_three + middle + first_three
print(arr)