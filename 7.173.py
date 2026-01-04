speeds = [float(input(f"Скорость {i+1}-й марки (км/ч): ")) for i in range(12)]
max_speed = max(speeds)

second_max = max(s for s in speeds if s != max_speed)
print(f"Скорость, больше которой только максимальная: {second_max} км/ч")