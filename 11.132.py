class_sizes = list(map(int, input("Введите численность 40 классов: ").split()))
max_size = max(class_sizes)
min_size = min(class_sizes)
difference = max_size - min_size
condition = difference >= 10
print(f"Разница: {difference} учеников")
print(f"В самом многочисленном классе на 10+ учеников больше: {condition}")