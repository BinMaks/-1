x = float(input("x: "))
y = float(input("y: "))
if x > 0 and y > 0:
    quarter = 1
elif x < 0 and y > 0:
    quarter = 2
elif x < 0 and y < 0:
    quarter = 3
elif x > 0 and y < 0:
    quarter = 4
else:
    quarter = "на оси"
print(f"Точка находится в {quarter} четверти")