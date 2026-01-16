speeds = list(map(float, input("Введите скорости 40 автомобилей: ").split()))
max_speed = max(speeds)
first_fastest = speeds.index(max_speed) + 1
print(f"Первый самый быстрый (номер): {first_fastest}")
last_fastest = len(speeds) - speeds[::-1].index(max_speed)
print(f"Последний самый быстрый (номер): {last_fastest}")