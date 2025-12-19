initial = 1000
rate = 0.02

print("Прирост за месяц:")
for month in range(1, 11):
    increase = initial * rate
    initial += increase
    print(f"Месяц {month}: {increase:.2f} руб.")


print("\nСумма вклада:")
initial = 1000
for month in range(3, 13):
    for _ in range(month):
        initial += initial * rate
    print(f"Через {month} месяцев: {initial:.2f} руб.")
    initial = 1000