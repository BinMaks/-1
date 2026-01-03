rainfall = [int(input(f"Осадки за день {i+1} мая: ")) for i in range(31)]
count_dry_days = 0
for day in rainfall:
    if day == 0:
        count_dry_days += 1
    else:
        break
print("Количество первых дней без осадков:", count_dry_days)