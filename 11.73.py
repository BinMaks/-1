heights = [float(x) for x in input("Рост 22 учеников (в см): ").split()]
r = float(input("Введите значение r (в см): "))
students_below_r = sum(1 for h in heights if h <= r)
print(f"Учеников с ростом ≤ {r} см: {students_below_r}")