
arr = list(map(int, input("Массив: ").split()))
count = 0
for i in range(len(arr)):
    count += (arr[i] == arr[0])
    if arr[i] != arr[0]:
        break
print("Количество равных элементов:", count)
print("Оставшиеся элементы:", arr[count:])