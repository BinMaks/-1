masses = [float(x) for x in input("Массы 25 человек: ").split()]
full = [m for m in masses if m > 100]
others = [m for m in masses if m <= 100]
avg_full = sum(full) / len(full)
avg_others = sum(others) / len(others)
print(f"Средняя масса полных людей: {avg_full}")
print(f"Средняя масса остальных: {avg_others}")