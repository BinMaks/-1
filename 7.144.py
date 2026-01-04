n = int(input("Количество пар: "))
pairs = []

for _ in range(n):
    a, b = map(float, input("Введите a и b: ").split())
    pairs.append((a, b))

max_sum = max(a + b for a, b in pairs)
min_product = min(a * b for a, b in pairs)

print(f"Максимальная сумма: {max_sum}")
print(f"Минимальное произведение: {min_product}")