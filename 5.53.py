total = 0
power_of_2 = 4
for i in range(2, 11):
    total += power_of_2
    power_of_2 *= 2
print(f"Сумма: {total}")