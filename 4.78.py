a, b = map(int, input("Координаты первого поля (a b): ").split())
c, d = map(int, input("Координаты второго поля (c d): ").split())
color1 = (a + b) % 2
color2 = (c + d) % 2
if color1 == color2:
    print("Поля ({}, {}) и ({}, {}) одного цвета.".format(a, b, c, d))
else:
    print("Поля ({}, {}) и ({}, {}) разного цвета.".format(a, b, c, d))