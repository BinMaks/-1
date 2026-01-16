
speeds = list(map(float, input("Введите скорости 40 автомобилей: ").split()))
speeds_sorted = sorted(speeds, reverse=True)
print(f"Два самых быстрых: {speeds_sorted[0]} и {speeds_sorted[1]}")