price_per_kg = float(input("Введите стоимость 1 кг конфет: "))
for weight in range(100, 2001, 100):
    cost = (weight / 1000) * price_per_kg
    print(f"{weight} г = {cost:.2f} руб.")