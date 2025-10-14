def calculate_horizon_distance(height_meters):
    h=height_meters
    k=3.57
    distance=k*(h**0.5)
    return distance
height=float(input("Введите высоту в метрах:"))
distance=calculate_horizon_distance(height)
print(f"Расстояние до горизонта:{distance:.2f} км")