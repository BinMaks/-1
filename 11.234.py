population = list(map(float, input("Численность 28 государств (млн жителей): ").split()))
area = list(map(float, input("Площадь 28 государств (млн кв. км): ").split()))
total_population = 0
for i in range(28):
    if area[i] > 5:
        total_population += population[i]
print(f"Общая численность государств с площадью > 5 млн кв. км: {total_population} млн жителей")