
pupils = [int(x) for x in input("Введите численность учеников в 42 классах: ").split()]
total_pupils = sum(pupils)
if 1000 <= total_pupils <= 9999:
    print("Общее число учеников — четырехзначное число")
else:
    print("Общее число учеников не является четырехзначным числом")