
power = list(map(int, input("Мощность 30 автомобилей (л. с.): ").split()))
cost = list(map(int, input("Стоимость 30 автомобилей: ").split()))
for i in range(30):
    if power[i] <= 80:
        print(f"Стоимость автомобиля с мощностью {power[i]} л. с.: {cost[i]} руб.")