revenue = []
print("Введите доход для 3 магазинов за 10 дней:")
for i in range(3):
    print(f"Магазин {i + 1}:")
    row = []
    for j in range(10):
        r = float(input(f"День {j + 1}: "))
        row.append(r)
    revenue.append(row)
print("\nДень с максимальным доходом для каждого магазина:")
for i, row in enumerate(revenue, 1):
    max_day = row.index(max(row)) + 1
    max_income = max(row)
    print(f"Магазин {i}: день {max_day} (доход: {max_income})")
print("\nМагазин с максимальным доходом за каждый день:")
for j in range(10):
    max_income = max(revenue[i][j] for i in range(3))
    shop_index = [revenue[i][j] for i in range(3)].index(max_income) + 1
    print(f"День {j + 1}: магазин {shop_index} (доход: {max_income})")