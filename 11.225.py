
areas = list(map(float, input("Площади (га): ").split()))
harvests = list(map(float, input("Урожаи (ц): ").split()))
total_area = sum(areas)
total_harvest = sum(harvests)
avg_yield = total_harvest / total_area
print("Средняя урожайность по области:", avg_yield, "ц/га")