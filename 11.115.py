prices = list(map(float, input("Введите стоимость 20 видов конфет: ").split()))
min_price = min(prices)
print(f"Самые дешевые конфеты стоят {min_price}")