sales = [float(x) for x in input("Стоимость товаров за каждый день марта (31 день): ").split()]
s = float(input("Введите значение s: "))
high_sales_days = sum(1 for x in sales if x > s)
print(f"Дней с продажами выше {s}: {high_sales_days}")