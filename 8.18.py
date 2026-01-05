a = float(input("Введите a: "))
x = float(input("Введите x: "))
epsilon = float(input("Введите ε: "))
y_prev = a
y_curr = 0.5 * (y_prev + x / (y_prev - 1))
i = 1
while abs(y_curr**2 - y_prev**2) >= epsilon:
    y_prev = y_curr
    y_curr = 0.5 * (y_prev + x / (y_prev - 1))
    i += 1
print(f"Первый член, удовлетворяющий условию: y{i} = {y_curr}")
print(f"Номер члена: {i}")