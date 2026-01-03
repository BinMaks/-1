costs = []
while True:
    cost = float(input("Стоимость товара (0 — завершить): "))
    if cost == 0:
        break
    costs.append(cost)
total = sum(x for x in costs if x > 1000)
print("Общая стоимость дорогих товаров:", total)