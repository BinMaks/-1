
grades = [int(x) for x in input("Оценки 22 учеников по иностранному языку: ").split()]
fives = sum(1 for g in grades if g == 5)
fours = sum(1 for g in grades if g == 4)
threes = sum(1 for g in grades if g == 3)
twos = sum(1 for g in grades if g == 2)
print(f"Пятерок: {fives}, четверок: {fours}, троек: {threes}, двоек: {twos}")