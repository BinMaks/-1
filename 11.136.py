
wind_directions = list(map(int, input("Введите направления ветра (1–8): ").split()))
freq = [0] * 8
for d in wind_directions:
    freq[d - 1] += 1
max_freq = max(freq)
max_dir = freq.index(max_freq) + 1
if max_dir in [1, 5, 6]:
    print("Жилой комплекс должен быть южнее комбината")
elif max_dir in [2, 7, 8]:
    print("Жилой комплекс должен быть севернее комбината")
elif max_dir == 3:
    print("Жилой комплекс должен быть западнее комбината")
elif max_dir == 4:
    print("Жилой комплекс должен быть восточнее комбината")