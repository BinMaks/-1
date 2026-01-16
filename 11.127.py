
prices = list(map(float, input("Стоимость 60 книг: ").split()))
min_price = min(prices)
count = prices.count(min_price)
print(f"Количество самых дешевых книг: {count}")