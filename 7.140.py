areas = [float(input(f"Площадь круга {i+1}: ")) for i in range(int(input("Количество кругов: ")))]
min_area = min(areas)
radius = (min_area / 3.14159) ** 0.5
print(f"Радиус самого маленького круга: {radius:.2f}")