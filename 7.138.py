temperatures = [float(input(f"Температура дня {i+1}: ")) for i in range(30)]
max_temp = max(temperatures)
print(f"Максимальная температура: {max_temp}")