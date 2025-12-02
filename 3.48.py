from math import remainder

y = float(input("Введите угол поворота часовой стрелки y (градусы, 0 <= y < 360): "))
if not (0 <= y < 360):
    print("Ошибка: угол должен быть в диапазоне [0, 360). ")
else:
    hours = int(y // 30)
    remainder = y % 30
    minutes = int(2 * remainder)
    print(f"Прошло: {hours} полных часов и {minutes} полных минут.")