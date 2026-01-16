
x = list(map(float, input("X-координаты 20 точек: ").split()))
y = list(map(float, input("Y-координаты 20 точек: ").split()))
min_x = min(x)
max_x = max(x)
min_y = min(y)
max_y = max(y)
print("Левый нижний угол: (", min_x, ", ", min_y, ")")
print("Правый верхний угол: (", max_x, ", ", max_y, ")")