arr = list(map(int, input("Массив: ").split()))
for i in range(len(arr) - 1):
    if arr[i] == arr[i+1]:
        print("Элементы после первой пары:", arr[i+2:])
        break
else:
    print("Нет одинаковых соседних элементов")