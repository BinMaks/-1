
temperatures = [float(input(f"Температура {i+1}-го дня июля: ")) for i in range(31)]
sorted_temps = sorted(enumerate(temperatures, 1), key=lambda x: x[1])
print(f"Самый прохладный день: {sorted_temps[0][0]} июля,°C")
print(f"Второй самый прохладный: {sorted_temps[1]}°C")