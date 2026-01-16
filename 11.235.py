
power = list(map(int, input("Мощность 30 автомобилей (л. с.): ").split()))
cost = list(map(int, input("Стоимость 30 автомобилей: ").split()))
total_cost = sum(cost[i] for i in range(30) if power[i] > 100)
print("Общая стоимость: ", total_cost)