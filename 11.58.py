scores = [float(x) for x in input("Оценки спортсмена (18 элементов): ").split()]
obligatory = sum(scores[:6])
optional = sum(scores[6:])

if obligatory > optional:
    print("Лучший результат по обязательной программе")
elif optional > obligatory:
    print("Лучший результат по произвольной программе")
else:
    print("Результаты равны")