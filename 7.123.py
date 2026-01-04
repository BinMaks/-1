heights = [float(input()) for _ in range(15)]  # 15 ростов
new_height = float(input("Рост нового ученика: "))

place = 1
for h in heights:
    if new_height < h:
        place += 1
print("Место в списке:", place)