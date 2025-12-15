
a1, b1, c1 = map(float, input("Введите первую тройку чисел: ").split())
first_triple = sorted([a1, b1, c1])
mid1 = first_triple[1]
a2, b2, c2 = map(float, input("Введите вторую тройку чисел: ").split())
second_triple = sorted([a2, b2, c2])
mid2 = second_triple[1]
avg = (mid1 + mid2) / 2
print(f"Среднее арифметическое средних чисел: {avg}")