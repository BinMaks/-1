prices = list(map(float, input("Стоимость 30 видов конфет: ").split()))
min_price = min(prices)
first_cheap = prices.index(min_price) + 1
print(f"Первый самый дешевый (номер): {first_cheap}")
last_cheap = len(prices) - prices[::-1].index(min_price)
print(f"Последний самый дешевый (номер): {last_cheap}")