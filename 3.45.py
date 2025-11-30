k = int(input("Введите k (1 <= k <= 180): "))
if k < 1 or k > 180:
    print("Ошибка: k должно быть от 1 до 180.")
else:
    idx = (k - 1) // 2
    x = 10 + idx
    if k % 2 == 1:
        digit = x // 10
    else:
        digit = x % 10
    print(f"{k}-я цифра: {digit}")

