N = 100
distance = 0
total_path = 0
for i in range(1, N + 1):
    step = 1 / i
    if i % 2 == 1:
        distance -= step
        total_path += step
    else:
        distance += step
        total_path += step
print(f"Расстояние от дома после {N} этапов: {distance:.6f} км")
print(f"Общий пройденный путь: {total_path:.6f} км")