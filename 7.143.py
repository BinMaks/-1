population = []
area = []
for i in range(16):
    pop = float(input(f"Численность населения {i+1}-го государства (млн): "))
    ar = float(input(f"Площадь {i+1}-го государства (тыс. кв. км): "))
    population.append(pop)
    area.append(ar)
density = [population[i] / area[i] for i in range(16)]
min_density = min(density)
print(f"Минимальная плотность населения: {min_density:.2f} млн/тыс. кв. км")