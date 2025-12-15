x = float(input("Введите x для графика (а): "))
if x >= -1:
    y = 1
else:
    y = 0
print(f"y = {y}")


x = float(input("Введите x для графика (б): "))
if x < 0:
    y = 1
elif 0 <= x <= 1:
    y = 0
else:
    y = -1
print(f"y = {y}")

x = float(input("Введите x для графика (в): "))
if x <= -1 or x >= 1:
    y = 1
else:
    y = -1
print(f"y = {y}")