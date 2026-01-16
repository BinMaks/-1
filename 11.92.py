heights = [float(x) for x in input("Рост 22 учеников (отрицательные — мальчики): ").split()]
boys = [h for h in heights if h < 0]
girls = [h for h in heights if h >= 0]
avg_boys = sum(boys) / len(boys)
avg_girls = sum(girls) / len(girls)
print(f"Средний рост мальчиков: {-avg_boys}")
print(f"Средний рост девочек: {avg_girls}")