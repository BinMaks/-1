ages = [int(input(f"Возраст {i+1}-го человека: ")) for i in range(int(input("Количество людей: ")))]

min_age_idx = ages.index(min(ages))
max_age_idx = ages.index(max(ages))

if min_age_idx < max_age_idx:
    print("Самый молодой указан раньше")
else:
    print("Самый старший указан раньше")