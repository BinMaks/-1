cars = [float(x) for x in input("Стоимости автомобилей: ").split()]
motos = [float(x) for x in input("Стоимости мотоциклов: ").split()]
avg_cars = sum(cars) / len(cars)
avg_motos = sum(motos) / len(motos)
if avg_cars > 3 * avg_motos:
    print("Средняя стоимость авто > средней стоимости мото в 3 раза")
else:
    print("Условие не выполняется")