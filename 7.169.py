
times = [float(input(f"Время на этапе {i+1} (мин): ")) for i in range(int(input("Количество этапов: ")))]

min_time_idx = times.index(min(times))
max_time_idx = times.index(max(times))

if min_time_idx < max_time_idx:
    print("Этап с первым местом был раньше этапа с последним местом")
else:
    print("Этап с первым местом был позже этапа с последним местом")