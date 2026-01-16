
mass = list(map(float, input("Масса 20 предметов (кг): ").split()))
volume = list(map(float, input("Объём 20 предметов (см³): ").split()))
max_density = max(mass[i] / volume[i] for i in range(20))
print("Максимальная плотность: ", max_density, "кг/см³")