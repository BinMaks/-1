import math
R = 6350
print("Высота (км) | Расстояние до горизонта (км)")
print("-! * 40")
for h in range(1, 11):
    d = math.sqrt(2 * R * h)
    print(f"{h:10} | {d:25.2f}")