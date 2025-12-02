from math import remainder

y = float(input("Введите угол часовой стрелки y (градусы, 0 < y <= 360): "))
if not (0 < y <= 360):
    print("Ошибка: угол должен быть в диапазоне (0, 360] ")
else:
    hours = int(y // 30)
    remainder_y = y % 30
    minutes = int(2 * remainder_y)
    angle_minute = (12 * y) % 360
    print(f"Угол минутной стрелки: {angle_minute:.1f}")
    print(f"Прошло: {hours} полных часов и {minutes} полных минут.")
