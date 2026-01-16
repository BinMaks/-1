arr = list(map(int, input("Упорядоченный массив: ").split()))
a = int(input("Число a: "))
print([x for x in arr if x < a])

arr = list(map(int, input("Упорядоченный массив: ").split()))
a = int(input("Число a: "))
for i in range(len(arr) - 1):
    if arr[i] < a < arr[i + 1]:
        print(f"Элементы: {arr[i]}, {arr[i + 1]}, позиции: {i}, {i + 1}")
        break


arr = list(map(int, input("Упорядоченный массив: ").split()))
a = int(input("Число a: "))
closest = min(arr, key=lambda x: abs(x - a))
print(f"Ближайший элемент: {closest}, позиция: {arr.index(closest)}")