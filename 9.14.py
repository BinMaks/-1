revenue = []
print("Введите доход для 3 магазинов за 10 дней:")
for i in range(3):
    print(f"Магазин {i + 1}:")
    row = []
    for j in range(10):
        r = float(input(f"День {j + 1}: "))
        row.append(r)
    revenue.append(row)
total_revenue = [sum(row) for row in revenue]
max_total = max(total_revenue)
max_shop = total_revenue.index(max_total) + 1
print(f"\nМагазин с максимальным общим доходом: {max_shop} (доход: {max_total})")
daily_total = [sum(revenue[i][j] for i in range(3)) for j in range(10)]
max_daily = max(daily_total)
max_day = daily_total.index(max_daily) + 1
print(f"День с максимальным общим доходом фирмы: {max_day} (доход: {max_daily})")
max_single = max(max(row) for row in revenue)
for i, row in enumerate(revenue):
    if max_single in row:
        day = row.index(max_single) + 1
        print(f"Максимальный доход за день: магазин {i + 1}, день {day} (доход: {max_single})")
        break