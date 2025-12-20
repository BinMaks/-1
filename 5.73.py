import math
length = 4.5
initial_distance = 3
step = 0.2
distance = initial_distance
print("Расстояние от стены (м) | Угол с полом (градусы)")
print("-! * 40")
while distance <= length:
    height = math.sqrt(length ** 2 - distance ** 2)
    angle_rad = math.atan(height / distance)
    angle_deg = math.degrees(angle_rad)
    print(f"{distance:8.2f}               | {angle_deg:10.2f}")
    distance += step