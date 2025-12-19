n = int(input("Введите n (n > 2): "))
if n > 2:
    sum_products = sum(i * (i + 1) for i in range(1, n))
    print(f"Сумма произведений: {sum_products}")
else:
    print("Ошибка: n должно быть больше 2")