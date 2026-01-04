weights = [float(input(f"Вес человека {i+1} (кг): ")) for i in range(int(input("Количество людей: ")))]
full_people = [w for w in weights if w > 100]
other_people = [w for w in weights if w <= 100]
avg_full = sum(full_people) / len(full_people)
avg_other = sum(other_people) / len(other_people)
print(f"Средняя масса полных людей: {avg_full} кг")
print(f"Средняя масса остальных людей: {avg_other} кг")