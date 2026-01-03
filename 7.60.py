
temperatures = [float(input(f"Температура за день {i+1}: ")) for i in range(30)]
count_below_zero = sum(1 for temp in temperatures if temp < 0)
print("Количество дней с температурой ниже 0°C:", count_below_zero)