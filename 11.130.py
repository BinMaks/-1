arr = list(map(float, input("Введите вещественные числа: ").split()))
min_val = min(arr)
max_val = max(arr)
condition_a = (max_val - min_val) <= 25
print(f"Условие а) выполнено: {condition_a}")
condition_b = (min_val * 2) < max_val
print(f"Условие б) выполнено: {condition_b}")