arr = list(map(int, input("Массив: ").split()))
for i in range(len(arr) - 1):
    if arr[i] % 2 == 1 and arr[i+1] % 2 == 1:
        print(f"Пара нечетных элементов на позициях {i+1} и {i+2}")
        break
else:
    print("Нет пары соседних нечетных элементов")