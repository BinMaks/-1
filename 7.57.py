rainfall = [float(input(f"Осадки за день {i+1}: ")) for i in range(28)]
sum_even = sum(rainfall[i] for i in range(1, 28, 2))  
sum_odd = sum(rainfall[i] for i in range(0, 28, 2))
print("По чётным дням выпало больше осадков, чем по нечётным:", sum_even > sum_odd)