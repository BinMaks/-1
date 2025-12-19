distance = 10
rate = 0.10


print("Пробег за день:")
for day in range(2, 11):
    distance *= 1 + rate
    print(f"День {day}: {distance:.2f} км")


total = 10 
dist = 10
for day in range(2, 8):
    dist *= 1 + rate
    total += dist
print(f"Суммарный путь за 7 дней: {total:.2f} км")