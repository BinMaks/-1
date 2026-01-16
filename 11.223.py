shop1 = list(map(float, input("Продажи магазина 1 (июль-август): ").split()))
shop2 = list(map(float, input("Продажи магазина 2 (июль-август): ").split()))
total = sum(shop1) + sum(shop2)
print("Общая стоимость:", total)