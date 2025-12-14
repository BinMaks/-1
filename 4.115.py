nums = list(map(int, input("Введите шесть чисел: ").split()))
sum_pos = 0
for num in nums:
    if num > 0:
        sum_pos += num
print(f"Сумма положительных: {sum_pos}")