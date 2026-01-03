rainfall = [float(input(f"Осадки за день {i+1}: ")) for i in range(30)]
sum_even = sum(rainfall[i] for i in range(1, 30, 2))  
print("Сумма осадков за чётные дни:", sum_even)