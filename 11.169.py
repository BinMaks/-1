heights = list(map(float, input("15 ростов (убывание): ").split()))
new_height = float(input("Рост нового ученика: "))
pos = int(input("Позиция вставки (1-16): ")) - 1
heights.insert(pos, new_height)
print(heights)