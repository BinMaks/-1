
arr = list(map(int, input("Массив: ").split()))
for i in range(1, len(arr) - 1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        print(f"Тройка на позициях {i}, {i+1}, {i+2}: {arr[i-1]}, {arr[i]}, {arr[i+1]}")
        break
else:
    print("Нет такой тройки")