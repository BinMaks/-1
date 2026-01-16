
prices = list(map(float, input("Введите стоимость 30 товаров: ").split()))
prices_sorted = sorted(prices, reverse=True)
print(f"Две самые дорогие стоимости: {prices_sorted[0]} и {prices_sorted[1]}")