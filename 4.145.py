animals = ["Крыса", "Корова", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья"]
colors = ["Зелёный", "Красный", "Жёлтый", "Белый", "Чёрный"]
year = int(input("Введите год: "))
cycle_position = (year - 1984) % 60
animal_index = cycle_position % 12
animal = animals[animal_index]
color_index = (cycle_position // 2) % 5
color = colors[color_index]
print(f"{animal}, {color}")