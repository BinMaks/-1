price_per_kg = float(input("Введите стоимость 1 кг сыра: "))
for weight in range(50, 1001, 50):
    cost = (weight / 1000) * price_per_kg
    print(f"{weight} г = {cost:.2f} руб.")