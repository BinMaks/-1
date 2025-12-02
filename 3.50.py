h = int(input("Введите часы (h, 1-12): "))
m = int(input("Введите минуты (m, 0-59): "))
if not (1 <= h <= 12) or not (0 <= m <= 59):
    print("Ошибка: h должно быть от 1 до 12, m от 0 до 59.")
else:
    dt_coincide = (60 * h - 11 * m)/11