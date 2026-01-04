
distances = [float(input(f"Расстояние {i+1}-го авто (км): ")) for i in range(25)]
times = [float(input(f"Время {i+1}-го авто (ч): ")) for i in range(25)]

max_speed_idx = -1
max_speed = -1
for i in range(25):
    speed = distances[i] / times[i]
    if speed > max_speed:
        max_speed = speed
        max_speed_idx = i + 1

print(f"Номер авто с макс. средней скоростью: {max_speed_idx}")