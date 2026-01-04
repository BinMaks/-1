n_cars = int(input("Введите количество автомобилей: "))
cars = []
print("Введите стоимость каждого автомобиля:")
for i in range(n_cars):
    price = float(input(f"Автомобиль {i+1}: "))
    cars.append(price)
n_bikes = int(input("\nВведите количество мотоциклов: "))
bikes = []
print("Введите стоимость каждого мотоцикла:")
for i in range(n_bikes):
    price = float(input(f"Мотоцикл {i+1}: "))
    bikes.append(price)
avg_cars = sum(cars) / n_cars
avg_bikes = sum(bikes) / n_bikes  
if avg_cars > 3 * avg_bikes:
    print("\nДА - средняя стоимость автомобилей больше в 3 раза")
else:
    print("\nНЕТ - условие не выполняется")