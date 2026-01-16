
heights = list(map(float, input("15 ростов (убывание): ").split()))
new_height = float(input("Рост нового ученика: "))
place = 1
for h in heights:
    if new_height < h:
        place += 1
    else:
        break
print(f"Место в перечне: {place}")