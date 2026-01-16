
heights = [float(x) for x in input("Рост 30 учеников (в см): ").split()]
tall_students = sum(1 for h in heights if h > 170)
can_form_team = tall_students >= 5
print(f"Учеников выше 170 см: {tall_students}")
print(f"Можно сформировать баскетбольную команду: {can_form_team}")