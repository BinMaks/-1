import math

diameter = 10
thickness = 0.5
total_volume_cm3 = 0
for i in range(12):
    radius = diameter / 2 + i * thickness
    volume = (4/3) * math.pi * (radius ** 3)
    total_volume_cm3 += volume
total_volume_liters = total_volume_cm3 / 1000
print(f"Суммарный объём: {total_volume_liters:.2f} литров")