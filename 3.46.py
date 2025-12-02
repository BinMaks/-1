from unicodedata import digit

k = int(input("Введите k (1 <= k <= 150): "))
if k < 1 or k > 150:
    print("Ошибка: k должно быть от 1 до 150.")
else:
    n = (k - 1) // 3
    x = 101 + n
    r = (k - 1) % 3
    if r == 0:
        digit = x // 100
    elif r == 1:
        digit = (x // 10) % 10
    else:
        digit = x % 10
    print(f"{k}-я цифра: {digit}")