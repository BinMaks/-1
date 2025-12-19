a = float(input("Введите a: "))
n = int(input("Введите n: "))
result = 1
for _ in range(abs(n)):
    result *= a
if n < 0:
    result = 1 / result
print(f"a^n = {result}")