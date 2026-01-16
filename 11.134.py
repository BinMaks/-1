ages = list(map(int, input("Введите возраст людей: ").split()))
min_age = min(ages)
max_age = max(ages)
min_index = ages.index(min_age)
max_index = ages.index(max_age)
if min_index < max_index:
    print("Самый молодой указан раньше")
elif min_index > max_index:
    print("Самый старый указан раньше")
else:
    print("Самый молодой и самый старый указаны одновременно (на одной позиции)")