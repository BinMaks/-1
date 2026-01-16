january_rain = [int(x) for x in input("Осадки за каждый день января (31 число): ").split()]
print(f"Общее количество осадков: {sum(january_rain)} мм")