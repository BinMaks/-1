
heights = list(map(float, input("Введите высоты 20 вершин: ").split()))
new_height = float(input("Высота новой вершины: "))
pos = int(input("Позиция для вставки (1-21): ")) - 1
heights.insert(pos, new_height)
print(heights)