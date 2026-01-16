arr = list(map(float, input("Введите элементы массива: ").split()))
for i in range(len(arr) - 1):
    if arr[i+1] < arr[i]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
print(f"Массив после сортировки: {arr}")
print(f"Число в последнем элементе: {arr[-1]}")