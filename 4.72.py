x1_1, y1_1 = map(float, input("2Левый нижний угол 1-го прямоугольника (x, y): ").split())
w1, h1 = map(float, input("Ширина и высота 1-го прямоугольника: ").split())
x1_2, y1_2 = map(float, input("Левый нижний угол 2-го прямоугольника (x, y): ").split())
w2, h2 = map(float, input("Ширина и высота 2-го прямоугольника: ").split())
x2_1, y2_1 = x1_1 + w1, y1_1 + h1
x2_2, y2_2 = x1_2 + w2, y1_2 + h2
inside_2 = (x1_1 >= x1_2 and y1_1 >= y1_2 and x2_1 <= x2_2 and y2_1 <= y2_2)
inside_1 = (x1_2 >= x1_1 and y1_2 >= y1_1 and x2_2 <= x2_1 and y2_2 <= y2_1)
intersect = not (x2_1 < x1_2 or x2_2 < x1_1 or y2_1 < y1_2 or y2_2 < y1_1)
print(f"1-й прямоугольник внутри 2-го: {inside_2}")
print(f"2-й прямоугольник внутри 1-го: {inside_1}")
print(f"Прямоугольники пересекаются: {intersect}")