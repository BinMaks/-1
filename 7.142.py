densities = []
for i in range(20):
    mass = float(input(f"Масса тела {i+1} (кг): "))
    volume = float(input(f"Объём тела {i+1} (см³): "))
    density = mass / volume
    densities.append(density)

max_density = max(densities)
print(f"Максимальная плотность: {max_density:.2f} кг/см³")