total = 0
for i in range(1, 11):
    square = i ** 2
    if i % 2 == 1:
        total -= square
    else:
        total += square
print(f"Сумма: {total}")