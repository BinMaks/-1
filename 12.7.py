surname1 = input("Первая фамилия: ")
surname2 = input("Вторая фамилия: ")
if len(surname1) > len(surname2):
    print("Первая фамилия длиннее")
elif len(surname1) < len(surname2):
    print("Вторая фамилия длиннее")
else:
    print("Фамилии одинаковой длины")