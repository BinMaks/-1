hours = [3, 6, 9, 12, 15, 18, 21, 24]
cells = 1
for h in hours:
    cells *= 2  
    print(f"Через {h} часов: {cells} клеток")