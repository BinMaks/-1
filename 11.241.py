
distance = list(map(float, input("Расстояние 25 автомобилей (км): ").split()))
time = list(map(float, input("Время 25 автомобилей (ч): ").split()))
min_speed = min(distance[i] / time[i] for i in range(25))
print("Минимальная средняя скорость: ", min_speed, "км/ч")