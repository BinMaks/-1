
resistances = [float(x) for x in input("Сопротивления 20 элементов: ").split()]
total_resistance = 1 / sum(1/r for r in resistances)
print(f"Общее сопротивление: {total_resistance:.2f} Ом")