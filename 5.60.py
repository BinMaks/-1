a = float(input("Введите a: "))
n = int(input("Введите n: "))
result = 0
for _ in range(abs(n)):
    result += a
if n < 0:
    result = -result
print(f"Результат: {result}")