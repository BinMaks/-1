arr = list(map(int, input("Введите 20 элементов массива: ").split()))
max_sum = float('-inf')
best_start_index = 0
for i in range(len(arr) - 4):
    current_sum = sum(arr[i:i+5])
    if current_sum > max_sum:
        max_sum = current_sum
        best_start_index = i
print(f"Максимальная сумма: {max_sum}")
print(f"Индексы элементов: {best_start_index}–{best_start_index+4}")
print(f"Элементы: {arr[best_start_index:best_start_index+5]}")