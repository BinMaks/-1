print("Введите стоимость одной штуки для 5 видов товара:")
prices = [float(input(f"Товар {i + 1}: ")) for i in range(5)]
sales = []
print("\nВведите количество проданных товаров для 5 видов за 6 дней:")
for i in range(5):
    print(f"Товар {i + 1}:")
    row = []
    for j in range(6):
        count = int(input(f"День {j + 1}: "))
        row.append(count)
    sales.append(row)
total_income_per_item = [sum(prices[i] * sales[i][j] for j in range(6)) for i in range(5)]
print("\nОбщий доход по каждому виду товара:")
for i, income in enumerate(total_income_per_item, 1):
    print(f"Товар {i}: {income} руб.")
daily_income = [sum(prices[i] * sales[i][j] for i in range(5)) for j in range(6)]
print("\nОбщий доход за каждый день:")
for j, income in enumerate(daily_income, 1):
    print(f"День {j}: {income} руб.")
total_income = sum(daily_income)
print(f"\nОбщий доход магазина за 6 дней: {total_income} руб.")
max_income_item = total_income_per_item.index(max(total_income_per_item)) + 1
print(f"\nВид товара с максимальным доходом: {max_income_item}")
max_income_day = daily_income.index(max(daily_income)) + 1
print(f"День с максимальным доходом: {max_income_day}")
a = float(input("Введите пороговое значение a (руб.): "))
days_above_a = sum(1 for income in daily_income if income > a)
print(f"Количество дней с доходом выше {a} руб.: {days_above_a}")