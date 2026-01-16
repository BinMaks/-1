
heights = list(map(float, input("25 ростов (убывание): ").split()))
pos1 = int(input("Позиция 1-го нового ученика (1-26): ")) - 1
pos2 = int(input("Позиция 2-го нового ученика (1-26): ")) - 1
h1 = float(input("Рост 1-го нового ученика: "))
h2 = float(input("Рост 2-го нового ученика: "))
heights.insert(pos1, h1)
heights.insert(pos2, h2)
print(heights)