
voltages = [float(input(f"Напряжение {i+1}-го сопротивления (В): ")) for i in range(20)]
resistances = [float(input(f"Сопротивление {i+1}-го элемента (Ом): ")) for i in range(20)]
min_current_idx = -1
min_current = float('inf')
for i in range(20):
    current = voltages[i] / resistances[i]
    if current < min_current:
        min_current = current
        min_current_idx = i + 1
print(f"Номер сопротивления с мин. током: {min_current_idx}")