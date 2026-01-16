arr = list(map(int, input("Массив: ").split()))
for i in range(len(arr) - 1):
    if arr[i] == arr[i+1]:
        print(f"Пара одинаковых элементов на позициях {i+1} и {i+2}")
        break
else:
    print("Нет одинаковых соседних элементов")