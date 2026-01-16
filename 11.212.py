arr = list(map(int, input("Массив: ").split()))
for i in range(len(arr) - 1):
    if arr[i] > arr[i+1]:
        print(f"Массив неупорядочен, первый нарушающий элемент на позиции {i+1}: {arr[i]}")
        break
else:
    print("Массив упорядочен по возрастанию")