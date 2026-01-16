dir1 = list(map(int, input("Направления ветра (исследователь 1, 30 дней): ").split()))
dir2 = list(map(int, input("Направления ветра (исследователь 2, 30 дней): ").split()))
combined = []
for i in range(30):
    combined.append(dir1[i])
print("Сводная таблица направлений ветра за июнь:", combined)
codes = {1: "северный", 2: "южный", 3: "восточный", 4: "западный",
         5: "северо-западный", 6: "северо-восточный", 7: "юго-западный", 8: "юго-восточный"}
for i, direction in enumerate(combined):
    print(f"День {i+1}: {codes[direction]}")