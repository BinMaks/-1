y = float(input("Введите y: "))
if y > 2:
    f = 2
elif 0 < y <= 2:
    f = 0
else:
    f = -5 * y
print(f"f(y) = {f}")