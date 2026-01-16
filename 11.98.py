
prices = [float(x) for x in input("Стоимости 20 товаров: ").split()]
avg_price = sum(prices) / len(prices)
count = sum(1 for p in prices if p < avg_price)
print(f"Товаров со стоимостью < средней: {count}")